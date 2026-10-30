#!/usr/bin/env python3
"""fm-skill-surface.py - inventory every SKILL.md visible to agents on this machine.

Usage:
  bin/fm-skill-surface.py [--json] [--root <scope>=<dir> ...]
  bin/fm-skill-surface.py --help

The skill-analyzer skill uses this to compare an external skill against the
installed surface. It is read-only and dependency-free (Python 3 stdlib).

Default roots, in order (a root that does not exist is skipped):
  firstmate          <code root>/.agents/skills (the repo this script lives in)
  user-agents        ~/.agents/skills
  user-claude        ~/.claude/skills
  user-codex         ~/.codex/skills
  user-pi            ~/.pi/agent/skills
  project:<name>     <home>/projects/<name>/.agents/skills and .claude/skills
where <home> is $FM_HOME when set, else the code root.
Any --root replaces the whole default list; repeat it for several roots.

Every directory under a root that holds a SKILL.md is one candidate.
A candidate whose SKILL.md resolves (realpath) to a file already listed is
dropped, so a symlinked root or skill yields one entry. A candidate whose
content matches an earlier listed file byte for byte is kept and flagged
same-content-as:<scope> of that earlier entry.

Frontmatter is parsed minimally: plain, single- or double-quoted scalars with
indented continuation lines, folded (>, >-) and literal (|, |-) block scalars,
and one level of nested mapping (for example metadata:).

Output (stdout):
  TSV (default): header line, then one row per skill with columns
    scope name dir description model_invocation lines bytes flags
  Tabs and newlines inside a description are replaced by spaces; flags is a
  comma-separated list or "-".
  After the rows, when distinct files share a name, a blank line and
    NAME COLLISIONS (distinct content, same name):
    <name>: <scope>=<dir>; <scope>=<dir>...
  are printed to stderr.
  --json: one object {"skills": [...], "collisions": [...]} where each skill
  has the TSV columns as keys (flags as a list, lines and bytes as integers)
  and each collision is {"name": ..., "entries": [{"scope", "dir"}, ...]}.

model_invocation is explicit-only when disable-model-invocation is true,
otherwise auto.

Flags:
  no-frontmatter            the file does not start with a --- block
  unterminated-frontmatter  the --- block never closes
  missing-name              frontmatter has no name
  missing-description       frontmatter has no description (Pi will not load it)
  name!=dir                 name differs from the parent directory
  description>1024          description exceeds the spec limit
  broad-trigger:<a|b>       description contains broad trigger phrases
  same-content-as:<scope>   identical bytes to an earlier entry

Exit status: 0 on success, 2 on a usage error.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys

BROAD_PHRASES = (
    "any change",
    "before merging",
    "always",
    "any task",
    "whenever",
    "every time",
    "all code",
)
COLUMNS = ("scope", "name", "dir", "description", "model_invocation", "lines", "bytes", "flags")
KEY_RE = re.compile(r"^([A-Za-z][\w-]*):(?:\s+(.*)|\s*)$")
CHILD_RE = re.compile(r"^\s+([A-Za-z][\w-]*):\s*(.*)$")
FRONT_RE = re.compile(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", re.S)


def usage_error(message: str) -> None:
    print(f"fm-skill-surface.py: {message}", file=sys.stderr)
    print("Try: fm-skill-surface.py --help", file=sys.stderr)
    sys.exit(2)


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        inner = value[1:-1]
        if value[0] == "'":
            return inner.replace("''", "'")
        return inner.replace('\\"', '"').replace("\\\\", "\\")
    return value


def parse_frontmatter(text: str):
    """Return (mapping or None, error flag or None)."""
    if not text.startswith("---"):
        return None, "no-frontmatter"
    match = FRONT_RE.match(text)
    if not match:
        return None, "unterminated-frontmatter"
    lines = match.group(1).splitlines()
    data: dict = {}
    i = 0
    while i < len(lines):
        km = KEY_RE.match(lines[i])
        if not km:
            i += 1
            continue
        key, value = km.group(1), (km.group(2) or "").strip()
        i += 1
        if value in (">", ">-", ">+", "|", "|-", "|+"):
            block = []
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                block.append(lines[i].strip())
                i += 1
            parts = [b for b in block if b]
            data[key] = (" " if value.startswith(">") else "\n").join(parts)
            continue
        if value == "":
            child: dict = {}
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                cm = CHILD_RE.match(lines[i])
                if cm:
                    child[cm.group(1)] = unquote(cm.group(2))
                i += 1
            data[key] = child if child else ""
            continue
        parts = [value]
        while i < len(lines) and lines[i].startswith((" ", "\t")) and lines[i].strip():
            parts.append(lines[i].strip())
            i += 1
        data[key] = unquote(" ".join(parts))
    return data, None


def default_roots() -> list[tuple[str, str]]:
    code_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    home = os.path.expanduser("~")
    fm_home = os.environ.get("FM_HOME") or code_root
    roots = [
        ("firstmate", os.path.join(code_root, ".agents", "skills")),
        ("user-agents", os.path.join(home, ".agents", "skills")),
        ("user-claude", os.path.join(home, ".claude", "skills")),
        ("user-codex", os.path.join(home, ".codex", "skills")),
        ("user-pi", os.path.join(home, ".pi", "agent", "skills")),
    ]
    projects = os.path.join(fm_home, "projects")
    if os.path.isdir(projects):
        for name in sorted(os.listdir(projects)):
            for sub in (".agents", ".claude"):
                roots.append((f"project:{name}", os.path.join(projects, name, sub, "skills")))
    return roots


def walk_skill_dirs(root: str):
    """Yield directories under root holding a SKILL.md, following symlinks once."""
    visited: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(root, followlinks=True):
        real = os.path.realpath(dirpath)
        if real in visited:
            dirnames[:] = []
            continue
        visited.add(real)
        dirnames.sort()
        if "SKILL.md" in filenames:
            yield dirpath


def inventory(roots: list[tuple[str, str]]):
    rows = []
    seen_real: set[str] = set()
    seen_hash: dict[str, str] = {}
    for scope, root in roots:
        if not os.path.isdir(root):
            continue
        for dirpath in walk_skill_dirs(root):
            path = os.path.join(dirpath, "SKILL.md")
            real = os.path.realpath(path)
            if real in seen_real:
                continue
            seen_real.add(real)
            try:
                with open(path, "rb") as handle:
                    raw = handle.read()
            except OSError:
                continue
            text = raw.decode("utf-8", errors="replace")
            fm, err = parse_frontmatter(text)
            flags = [err] if err else []
            fm = fm or {}
            name = fm.get("name", "")
            name = name if isinstance(name, str) else ""
            desc = fm.get("description", "")
            desc = desc if isinstance(desc, str) else ""
            if not err and not name:
                flags.append("missing-name")
            if not err and not desc:
                flags.append("missing-description")
            if name and name != os.path.basename(os.path.normpath(dirpath)):
                flags.append("name!=dir")
            if len(desc) > 1024:
                flags.append("description>1024")
            lowered = desc.lower()
            broad = [p for p in BROAD_PHRASES if re.search(r"\b" + re.escape(p) + r"\b", lowered)]
            if broad:
                flags.append("broad-trigger:" + "|".join(broad))
            digest = hashlib.sha256(raw).hexdigest()
            if digest in seen_hash:
                flags.append("same-content-as:" + seen_hash[digest])
            else:
                seen_hash[digest] = scope
            invocation = str(fm.get("disable-model-invocation", "")).strip().lower()
            rows.append(
                {
                    "scope": scope,
                    "name": name,
                    "dir": dirpath,
                    "description": desc,
                    "model_invocation": "explicit-only" if invocation == "true" else "auto",
                    "lines": text.count("\n") + (0 if text.endswith("\n") or not text else 1),
                    "bytes": len(raw),
                    "flags": flags,
                    "_hash": digest,
                }
            )
    by_name: dict[str, list[dict]] = {}
    for row in rows:
        if row["name"]:
            by_name.setdefault(row["name"], []).append(row)
    collisions = []
    for name, entries in by_name.items():
        if len({e["_hash"] for e in entries}) > 1:
            collisions.append(
                {"name": name, "entries": [{"scope": e["scope"], "dir": e["dir"]} for e in entries]}
            )
    for row in rows:
        del row["_hash"]
    return rows, collisions


def main(argv: list[str]) -> int:
    as_json = False
    roots: list[tuple[str, str]] = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg in ("-h", "--help"):
            print(__doc__.strip())
            return 0
        if arg == "--json":
            as_json = True
        elif arg == "--root" or arg.startswith("--root="):
            if arg == "--root":
                i += 1
                if i >= len(argv):
                    usage_error("--root needs <scope>=<dir>")
                spec = argv[i]
            else:
                spec = arg[len("--root="):]
            scope, sep, directory = spec.partition("=")
            if not sep or not scope or not directory:
                usage_error(f"--root needs <scope>=<dir>, got '{spec}'")
            roots.append((scope, directory))
        else:
            usage_error(f"unknown argument '{arg}'")
        i += 1
    rows, collisions = inventory(roots or default_roots())
    if as_json:
        print(json.dumps({"skills": rows, "collisions": collisions}, indent=1))
        return 0
    print("\t".join(COLUMNS))
    for row in rows:
        cells = []
        for column in COLUMNS:
            value = row[column]
            if column == "flags":
                value = ",".join(value) or "-"
            cells.append(re.sub(r"[\t\r\n]+", " ", str(value)))
        print("\t".join(cells))
    if collisions:
        print("", file=sys.stderr)
        print("NAME COLLISIONS (distinct content, same name):", file=sys.stderr)
        for item in collisions:
            joined = "; ".join(f"{e['scope']}={e['dir']}" for e in item["entries"])
            print(f"  {item['name']}: {joined}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
