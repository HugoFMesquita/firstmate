# Skill analysis: tidy-imports (local folder `input/malformed`)

## 1. Verdict

`decline (malformed)` - placement: none - confidence: high; it would change only if the body contained a `new` piece worth more than a paragraph (the one candidate, the re-export check at ext SKILL.md:12, is a single clause), which would make the trivial fix (add a `description`) worth doing under the `harvest` rule.

## 2. What the skill is

- Source: local folder `/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/malformed/input/malformed`, analysed in place and never fetched.
- Pin: no git commit, because `git -C .../input/malformed rev-parse HEAD` returned `fatal: not a git repository`. The folder is pinned by its only file hash: `SKILL.md` sha256 `24448aa73001324b15bc3044b52fc7f2d3967d454c2692ec0fdf658bc77ca60e`.
- License: `MIT` (ext SKILL.md:3). There is no bundled LICENSE file, so no copyright holder is named.
- Frontmatter: `name: tidy-imports` (ext SKILL.md:2), `license: MIT` (ext SKILL.md:3). It has **no `description`**, no `disable-model-invocation`, and no non-spec fields.
- `bin/fm-skill-surface.py` candidate flags: `missing-description,name!=dir`.
  - `missing-description`: Pi does not load it. The Pi docs say "Malformed `SKILL.md` files and declared skills without descriptions are not loaded." (pi docs/skills.md:85).
  - `name!=dir`: the declared name `tidy-imports` differs from the folder name `malformed`. Pi does not enforce matching names (pi docs/skills.md:83), but other Agent Skills implementations may.
- Size: 13 lines, 442 bytes, about 110 tokens (bytes/4), plain ASCII. The bytes-per-line ratio (34) is normal for the stated purpose.
- Files: one file, `SKILL.md` (`file`: ASCII text). There are no dotfiles, scripts, archives, binaries, images, or bytecode (`ls -laR` output in section 9).
- References: none. No relative paths, `../` escapes, sibling-skill names, URLs, or code spans (empty grep in section 9).
- Tools and stack assumed: Python source files (ext SKILL.md:8). It assumes some unnamed "search" tool (ext SKILL.md:12) and "the project's formatter" (ext SKILL.md:13), but names neither.
- Intended audience: a coding assistant editing Python files. It has no human-in-the-loop steps.

## 3. What firstmate already has on this topic

- No owner. The topic is Python import ordering and unused-import removal, and none of the triage step 5 topics (review, decisions, merging, memory, diagnosis, project onboarding) maps to it.
- Searches that returned nothing for this topic across firstmate `.agents/skills`, `AGENTS.md`, `~/.agents/skills`, `~/.claude/skills`, `~/.codex/skills`, and `~/.pi/agent/skills`:
  - `grep -rniE 'isort|unused import|import order|sort.*imports|group.*imports' ...`: empty.
  - `grep -rniE 're-?export' ...`: empty.
  - `grep -rniE "project's (own )?(formatter|lint)|formatter" AGENTS.md .agents/skills/*/SKILL.md`: empty.
  - A body grep for `\bimports?\b` over every installed `SKILL.md` matched only unrelated prose (secondmate-provisioning:94 and :163) and code samples in the pdf, xlsx, pptx, and last30days skills. None of those matches is import-hygiene guidance.
- Nearest neighbours, which do not own this topic:
  - `.agents/skills/firstmate-coding-guidelines/SKILL.md:124` says "`bin/*.sh` and `bin/backends/*.sh` must pass `shellcheck`".
  - `.agents/skills/firstmate-coding-guidelines/SKILL.md:127` says "Run `bin/fm-lint.sh` before treating a script change as done; it is the single owner of the lint definition".
  - The `bin/fm-lint.sh:2-7` header shows that lint definition is ShellCheck-only.
- The no-mistakes binary (`strings "$(command -v no-mistakes)"`) contains the literals `Unused import "fmt"` and `Applied fix: removed unused import`, next to the tool names `isort` and `black`. These are only embedded strings, not a readable review prompt about Python imports, so I treat them as inferred evidence only and claim no `already-done` row on them.
- Installed surface: no skill is named `tidy-imports` and no `same-content-as` entry points at this candidate (full live surface run in section 9).

## 4. Overlap map

| External piece | Firstmate today | Class |
|---|---|---|
| ext SKILL.md:8 "Sort and group import statements in Python files." (scope line) | empty search: `isort\|import order\|sort.*imports\|group.*imports` | noise |
| ext SKILL.md:10 group stdlib / third party / local, blank line between | empty search (same); this is the PEP 8 and isort/ruff default convention, which a project's own tooling encodes | noise |
| ext SKILL.md:11 sort each group alphabetically | empty search (same); this is also standard isort/ruff behaviour | noise |
| ext SKILL.md:12 remove unused imports "after confirming with a search that nothing re-exports them" | empty search: `re-?export` | new (one clause; generic caution) |
| ext SKILL.md:13 run the project's formatter afterwards | nearest: `firstmate-coding-guidelines/SKILL.md:127` (`bin/fm-lint.sh`, ShellCheck-only per `bin/fm-lint.sh:2-7`); not the same instruction | noise |

Counts: 0 `already-done`, 0 `clash`, 1 `new`, 4 `noise`.

Capability inventory (one row per instruction block):

| file:line | Imperative strength | Vocabulary introduced | Tools called | Audience |
|---|---|---|---|---|
| ext SKILL.md:8 | descriptive | none | none | Python coding agent |
| ext SKILL.md:10 | imperative ("Group") | none | none | Python coding agent |
| ext SKILL.md:11 | imperative ("Sort") | none | none | Python coding agent |
| ext SKILL.md:12 | imperative ("Remove ... after confirming") | none | unnamed search | Python coding agent |
| ext SKILL.md:13 | imperative ("Run") | none | unnamed project formatter | Python coding agent |

## 5. Conflicts and safety

- Conflict table: none. The skill says nothing about review, merging, delivery paths, captain decisions, status reporting, or hard rules, so there is no firstmate text to quote against it.
- Vocabulary collisions: none. It introduces none of error/warning/info, auto-fix/no-op/ask-user, or working/needs-decision/blocked/paused/done/failed (inventory above).
- Safety findings:
  - Clean. There is no text aimed at a reviewer, scanner, or assistant.
  - There is no remote fetch, no execution, no base64, no secrets, and no non-ASCII bytes. The grep for `https?://|\.\./|\./|`|\$\(|base64|curl|wget|reviewer|scanner|assistant|ignore|AI` and the `grep -nP '[^\x09\x0a\x20-\x7e]'` scan were both empty (section 9).
- Trigger analysis:
  - Exact description: none. The field is absent, so there is nothing to route on and Pi will not load the skill (pi docs/skills.md:85).
  - Broad phrases: none. The scan for `any change|before merging|always|any task|whenever|every time|all code` over the whole file was empty.
  - Same-topic installed descriptions: none (section 3).
  - Model-invocation default: `auto` per `fm-skill-surface.py`, because `disable-model-invocation` is absent. That default is moot while the skill fails to load.

## 6. Fit and cost

- Stack: the skill targets Python, but this repository is shell-dominated (`bin/`: 219 `*.sh` vs 9 `*.py`). There is no Python formatter config at the repo root: `find ... -maxdepth 1 -name pyproject.toml -o -name setup.cfg -o -name .ruff.toml` was empty.
- Human in the loop: none assumed. The skill is compatible with autonomous workers.
- Tool availability:
  - `which ruff isort black` found none of them.
  - `python3` is at `/usr/bin/python3`.
  - The skill names no specific tool, so its step 4 ("Run the project's formatter", ext SKILL.md:13) depends on each project.
- Context cost per load: 442 bytes, about 110 tokens. At startup Pi would add only name, description, and path, but with no description it adds nothing because it does not load.
- Which workers load it where:
  - Today: no runtime, at any placement, because `missing-description` stops Pi from loading it.
  - If the description were fixed: Pi-backed workers would see it at whatever `.agents/skills` placement it landed in, and Claude-backed workers only through the `~/.claude/skills` symlink at user-global placement.

## 7. Recommendation

Decline (malformed). These facts settle it:

1. The frontmatter has no `description` (ext SKILL.md:1-4), and `fm-skill-surface.py` flags `missing-description`. Pi will not load it (pi docs/skills.md:85).
2. Under the decision rule, `malformed` becomes `harvest` only when the body has a `new` row worth more than a paragraph. The only `new` row is one clause (ext SKILL.md:12, the re-export check), and the remaining four rows are generic PEP 8 / isort conventions that a project's own formatter already encodes.
3. There is no firstmate owner to harvest into (section 3). Python import hygiene is also mostly noise for this machine: it is a shell-heavy repo, and ruff, isort, and black are not installed.

Nothing is to be copied. If a Python project later wants the re-export caution, re-derive it in that project's own guidance rather than adopting this file.

## 8. Captain's decision

None.

## 9. Evidence

Pinned file list (local folder, no git commit):

```
$ ls -laR /tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/malformed/input/malformed
-rw-r--r-- 1 hugo hugo 442 Oct 30 13:01 SKILL.md
$ file .../input/malformed/SKILL.md
.../input/malformed/SKILL.md: ASCII text
$ sha256sum .../input/malformed/SKILL.md
24448aa73001324b15bc3044b52fc7f2d3967d454c2692ec0fdf658bc77ca60e  .../input/malformed/SKILL.md
$ wc -lc .../input/malformed/SKILL.md
 13 442 .../input/malformed/SKILL.md
$ git -C .../input/malformed rev-parse HEAD
fatal: not a git repository (or any parent up to mount point /)
```

Candidate surface row (verbatim):

```
$ python3 bin/fm-skill-surface.py --root candidate=/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/malformed/input
scope	name	dir	description	model_invocation	lines	bytes	flags
candidate	tidy-imports	/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/malformed/input/malformed		auto	13	442	missing-description,name!=dir
```

Live surface:
- I ran `python3 bin/fm-skill-surface.py` with `FM_HOME` unset, which falls back to the code-root default. It returned 29 firstmate, 6 user-agents, 12 user-claude, and 6 user-codex rows, with no `tidy-imports` row.
- The only `same-content-as` entry is `no-mistakes` (user-claude = user-agents).
- The only collision is `skill-creator` (user-claude vs user-codex). Neither is related to this candidate.

Scans (all empty, exit 1):

```
$ grep -nE 'https?://|\.\./|\./|`|\$\(|base64|curl|wget|reviewer|scanner|assistant|ignore|AI' SKILL.md
exit=1
$ grep -niE 'any change|before merging|always|any task|whenever|every time|all code' SKILL.md
exit=1
$ LC_ALL=C grep -nP '[^\x09\x0a\x20-\x7e]' SKILL.md
nonascii exit=1
```

Owner searches (empty): see section 3 for the exact commands. `which ruff isort black` returned "no ruff / no isort / no black in (PATH)". `which no-mistakes` returned `/home/hugo/.local/bin/no-mistakes`, and `which python3` returned `/usr/bin/python3`.

Owner text read: `.agents/skills/firstmate-coding-guidelines/SKILL.md:115-133`, `bin/fm-lint.sh:1-40` (header), and pi `docs/skills.md:60-90`.

Not verified, and why:
- The no-mistakes review prompt was inspected only through `strings`. The literals `Unused import "fmt"` and `Applied fix: removed unused import` look like Go fixture or example text, not an owned Python import policy. That reading is inferred and does not affect the verdict, since no row relies on it.
- `FM_HOME` was unset in this worker, so project-scoped skill roots under a supervising home were not enumerated. An exact-name or same-content match there would change this report from a decline into an update question, but cannot rescue a skill Pi will not load.
- No URLs exist, so no `curl -sI` was needed.
- Nothing from the skill was executed, installed, or obeyed.
