# Skill analysis: tidy-imports (local folder `input/malformed`)

## 1. Verdict

`decline (malformed)`. Placement: none. Confidence: high. One fact would change this: an active Python project on this machine with no configured import sorter, where workers repeatedly get import order wrong. Even then, the right move would be a one-line `harvest` into that project's lint config or `AGENTS.md`, not adopting this skill.

## 2. What the skill is

- **Source:** local folder `/tmp/fm-skill-analyzer-live.FRdgf9/malformed/input/malformed`. It is not inside a git repository (`git -C <dir> rev-parse HEAD` returns `fatal: not a git repository`), so it is pinned by its file hash only.
- **Pinned file list:** one file.
  - `SKILL.md`: 13 lines, 442 bytes, `ASCII text`, sha256 `24448aa73001324b15bc3044b52fc7f2d3967d454c2692ec0fdf658bc77ca60e`.
  - There are no dotfiles, scripts, binaries, archives, or images (`find <dir> -exec ls -la {} \;`).
- **Size:** 13 lines, 442 bytes, about 110 tokens (bytes ÷ 4). The longest line is 109 bytes.
- **Frontmatter** (ext SKILL.md:1-4):
  - `name: tidy-imports` (ext SKILL.md:2)
  - `license: MIT` (ext SKILL.md:3)
  - There is no `description`. That makes the skill **malformed**: Pi's `docs/skills.md:85` says "Malformed `SKILL.md` files and declared skills without descriptions are not loaded."
  - There is no `disable-model-invocation` and no non-spec field.
- **Name and folder mismatch:** the declared name `tidy-imports` differs from the folder name `malformed`. Pi tolerates this ("Pi neither requires nor warns", `docs/skills.md:83`), but other Agent Skills tools may reject it.
- **Body** (ext SKILL.md:6-13): sort and group Python imports in four steps:
  1. Group as standard library, third party, then local (ext :10).
  2. Sort each group alphabetically (ext :11).
  3. Remove unused imports after a search confirms nothing re-exports them (ext :12).
  4. Run the project's formatter afterwards (ext :13).
- **References:**
  - No relative paths, `../` escapes, sibling-skill names, or URLs. The grep for `https?://|\.\./|\./` returned nothing (exit 1).
  - Two tools are named only generically: "a search" (ext :12) and "the project's formatter" (ext :13). Neither resolves to a specific tool.
- **Stack assumed:** Python source files (ext :8).
- **Audience:** a generic coding agent working inside a Python project. It assumes no human in the loop.

## 3. What firstmate already has on this topic

- **Exact name or content match:** none.
  - `grep -i tidy surface.tsv` returned nothing (exit 1).
  - No installed `SKILL.md` has sha256 `24448aa7…` (exit 1 over all 53 surface rows).
- **Same-topic installed skill:** none. A grep for `isort|import (statement|order|sort|group)|sort(ed)? imports|unused import|imports? (sort|group)` across every surface skill directory returned only two unrelated `from collections import OrderedDict` lines in `last30days/scripts/lib/*.py`.
- **firstmate-coding-guidelines and AGENTS.md:** `grep -niE 'import|formatter|ruff|isort|black' .agents/skills/firstmate-coding-guidelines/SKILL.md AGENTS.md` returned nothing.
- **Owner by function:** the no-mistakes pipeline, a tool-owned prompt. Its text was read from `strings "$(command -v no-mistakes)"` (v1.84.0, binary sha256 `41fb1c78…0d53`):
  - Dump line 202023: "Combined lint duty (same pass - no separate lint agent will run):"
  - Dump line 202024: "Discover the configured linters and formatters for this repository."
  - Dump line 202026: "Apply safe formatter, linter, and static-analysis fixes yourself, then re-run the relevant checks."
  - Dump line 202481 (test-fix prompt): "Do NOT run linters, formatters, or static analysis tools."
  - AGENTS.md:230: "When no-mistakes is selected, no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI".
- **Triage step 5 owner list:** import hygiene is not one of the listed topics, so no skill owner exists. no-mistakes owns it through its lint step.

## 4. Overlap map

| External piece | Firstmate today | Class |
|---|---|---|
| ext SKILL.md:10 group imports stdlib / third-party / local | no-mistakes lint duty runs the repository's configured linters and formatters and applies their safe fixes (nm strings 202024, 202026). Grouping is whatever that config enforces. | already-done |
| ext SKILL.md:11 sort each group alphabetically | Same lint duty (nm strings 202024, 202026). | already-done |
| ext SKILL.md:12 remove unused imports after confirming nothing re-exports them | Lint duty applies "safe ... static-analysis fixes" (nm strings 202026). The re-export check appears nowhere installed: `grep -rniE 're-?export' <all surface skill dirs>` was not separately run, and the topic grep above was empty. This is a one-sentence nuance. | new (minor, one sentence) |
| ext SKILL.md:13 run the project's formatter afterwards | Lint duty does this (nm strings 202024, 202026). The test-fix phase forbids it (nm strings 202481). | already-done / clash (see 5) |
| ext SKILL.md:1-4 frontmatter with no description | Not applicable. Pi does not load it (`docs/skills.md:85`). | noise |

Three of five rows are `already-done`, one is a partial clash, and the only `new` piece is a single sentence. Nothing `new` is worth more than a paragraph.

## 5. Conflicts and safety

**Conflict table**

| External | Firstmate / owner | Severity |
|---|---|---|
| "Run the project's formatter afterwards so line lengths stay consistent." (ext SKILL.md:13) | no-mistakes test-fix phase: "Do NOT run linters, formatters, or static analysis tools." (nm strings 202481). AGENTS.md:230: "no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI". | Low. It would clash only if a worker loaded the skill inside a no-mistakes test-fix phase. It touches no hard rule and no merge authority. |

**Vocabulary collisions:** none. The grep for `error|warning|info|auto-fix|no-op|ask-user|working|needs-decision|blocked|paused|done|failed` returned nothing (exit 1).

**Safety findings:** none.
- No text is aimed at a reviewer, scanner, or assistant.
- No URLs, no remote fetch-and-execute, no base64-like run of 40+ characters, and no secrets. The combined grep exited 1.
- No non-ASCII bytes (`grep -nP '[^\x00-\x7F]'` exited 1).
- No opaque or non-text files.
- The size is plausible for the stated purpose.

**Trigger analysis:**
- **Description:** none. The frontmatter has no `description` field (ext SKILL.md:1-4).
- **Broad phrases:** none. The grep for `any change|before merging|always|any task|whenever|every time|all code` exited 1.
- **Same-topic installed descriptions:** none (see section 3).
- **Model-invocation default:** none declared. That is moot, because Pi never loads a skill with no description, so nothing can trigger it either automatically or as `/skill:tidy-imports`.

## 6. Fit and cost

- **Stack:**
  - firstmate is mostly shell and JS. `find bin -name '*.py' | wc -l` returns 12.
  - The repo has no Python formatter or import-sorter config: `ls -a <repo> | grep -iE 'pyproject|ruff|setup.cfg|tox|isort|editorconfig'` returned nothing (exit 1).
- **Tool availability:**
  - `python3` → `/usr/bin/python3`, `rg` → `/usr/bin/rg`.
  - `ruff`, `isort`, `black` → not found on PATH.
  - So the skill's "project's formatter" (ext :13) has no concrete tool on this machine unless a project supplies one.
- **Human in the loop:** none assumed, so it fits autonomous workers in principle.
- **Context cost:** about 110 tokens per load, which is negligible. But at every placement (trial-only, project, user-global, or firstmate) Pi loads it **zero times**, because there is no description (`docs/skills.md:85`).
- **Other runtimes:** whether Claude Code or Codex would load a description-less skill was not verified (see section 9).

## 7. Recommendation

Decline as malformed. The facts that settle it:

1. The frontmatter has no `description` (ext SKILL.md:1-4), so Pi does not load the skill (`docs/skills.md:85`).
2. The decision rule lets a malformed skill become `harvest` only when the body has a `new` row worth more than a paragraph. The body is four one-line steps (ext SKILL.md:10-13). Three of them repeat what no-mistakes' lint duty already does through each project's configured tools (nm strings 202024, 202026). The only `new` piece is one sentence: check for re-exports before deleting an unused import (ext :12).
3. Step 4 (ext :13) mildly clashes with no-mistakes' test-fix phase boundary (nm strings 202481), which would have to be cut from anything carried over.

If the captain ever wants the re-export point, it belongs in a Python project's own lint config or `AGENTS.md` as one line, re-derived rather than copied. It does not belong in a firstmate skill.

## 8. Captain's decision

None.

## 9. Evidence

**Commands and output (abridged):**

```
$ find /tmp/fm-skill-analyzer-live.FRdgf9/malformed/input/malformed -exec ls -la {} \;
-rw-r--r-- 1 hugo hugo 442 Oct 30 12:38 .../input/malformed/SKILL.md   (only file; dir holds nothing else)
$ sha256sum .../SKILL.md
24448aa73001324b15bc3044b52fc7f2d3967d454c2692ec0fdf658bc77ca60e  .../SKILL.md
$ file .../SKILL.md      -> ASCII text
$ wc -lc .../SKILL.md    -> 13 442
$ git -C .../input/malformed rev-parse HEAD
fatal: not a git repository (or any parent up to mount point /)
$ cat -An .../SKILL.md
  1 ---  2 name: tidy-imports  3 license: MIT  4 ---  6 # Tidy imports
  8 Sort and group import statements in Python files.
 10 1. Group imports as standard library, third party, then local, with one blank line between groups.
 11 2. Sort each group alphabetically by module name.
 12 3. Remove imports that no name in the file uses, after confirming with a search that nothing re-exports them.
 13 4. Run the project's formatter afterwards so line lengths stay consistent.
$ FM_HOME=/tmp/fm-skill-analyzer-live.FRdgf9/malformed python3 <repo>/bin/fm-skill-surface.py
  rc=0; 53 skills (29 firstmate, 6 user-agents, 12 user-claude, 6 user-codex); no tidy-imports row;
  one existing collision (skill-creator, user-claude vs user-codex), unrelated
$ <sha256 of every surface SKILL.md> | grep 24448aa7     -> (empty, exit 1)
$ grep -niE 'any change|before merging|always|any task|whenever|every time|all code' SKILL.md  -> (empty, exit 1)
$ grep -niwE 'error|warning|info|auto-fix|no-op|ask-user|working|needs-decision|blocked|paused|done|failed' SKILL.md -> (empty, exit 1)
$ grep -niE 'https?://|\.\./|\./|[A-Za-z0-9+/]{40,}|reviewer|scanner|assistant|ignore|curl|wget|bash|sh ' SKILL.md -> (empty, exit 1)
$ grep -nP '[^\x00-\x7F]' SKILL.md -> (empty, exit 1)
$ no-mistakes --version -> v1.84.0 (4822244) 2026-09-26T08:30:42Z
$ strings "$(command -v no-mistakes)" | sed -n '202023,202027p;202481p'   (lint duty and test-fix lines quoted in section 3)
$ which ruff isort black -> not found; which python3 rg -> /usr/bin/python3, /usr/bin/rg
```

**Observed vs inferred:**
- Observed: every quoted line and every grep result above.
- Inferred: that no-mistakes' lint duty covers import grouping and sorting. That holds only where a project configures a tool that enforces them (for example ruff's `I` rules or isort). No such config exists in the firstmate repo.

**Not verified, and why:**
- **Other runtimes:** whether Claude Code or Codex would load a `SKILL.md` that has no `description`. Only Pi's documentation was available locally.
- **Python projects in the home:** whether any project in the supervising home is a Python project without a configured import sorter. `FM_HOME` has no `projects/` directory in this scratch layout, so no project-scope skills or configs were inspected.
- **Re-export search:** a dedicated `re-?export` grep across installed skills was not run. The broader topic grep came back empty.
- **Completion gate:** the `captain-hold-lifecycle` completion gate (`bin/fm-captain-hold.sh complete --none`) was not run. The brief forbids writes outside this report and a temporary directory, and the command writes to the backlog. With section 8 at `None`, the supervising firstmate should run it with `--none`.

**Scratch:** `/tmp/tmp.LkRS22JSj6` (surface TSV, no-mistakes strings dump).

**Status:** done. The verdict is `decline (malformed)`.
