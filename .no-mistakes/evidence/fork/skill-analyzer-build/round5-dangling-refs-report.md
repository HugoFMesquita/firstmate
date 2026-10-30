# Skill analysis: dangling-refs (local folder `input/dangling-refs`)

## 1. Verdict

`decline (malformed)`. Placement: none. Confidence: high.
Three of the skill's five steps depend on things that don't exist: a checklist file outside the skill folder, another skill it calls a sibling, and a website on a reserved domain that can never resolve. The two steps that remain are generic one-liners with no license.
One fact would change this: the full source collection, with `references/checklist.md`, the `test-driven-development` skill, and a license, turning up and holding enough release-specific content to justify a new analysis of that collection.

## 2. What the skill is

- **Source:** local folder `/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/dangling-refs/input/dangling-refs`. It's a pinned local copy and wasn't fetched from anywhere. It isn't inside a git repository (`git rev-parse HEAD` returned `fatal: not a git repository`), so it is pinned by file hash only (section 9).
- **Pinned files:** one file, `SKILL.md`, 14 lines, 627 bytes, 87 words, `ASCII text`, sha256 `ff3b1bc41c64677f3b5d0ecaa561dd62e0b854eee5fe1a29305457ed4cd28857`. There are no dotfiles, scripts, binaries, archives, or images (`ls -la` shows only `SKILL.md`).
- **License:** none. There is no LICENSE file and no `license:` field (`grep -niE 'license'` on the file returned nothing, exit 1). The text is unlicensed to copy.
- **Frontmatter:** `name: dangling-refs` (ext SKILL.md:2), `description: Write a release checklist for a library before tagging a version. Use when preparing a release of a package.` (ext SKILL.md:3). There is no `disable-model-invocation` field, so it defaults to model-invocable. There are no non-spec fields.
- **`bin/fm-skill-surface.py` flags:** `-` (no flags; the row is in section 9). The frontmatter is well formed and Pi would load it. "Malformed" here refers to the body.
- **Size:** 14 lines, 627 bytes, about 157 tokens per full load (bytes / 4). The always-loaded description is 142 bytes of frontmatter, about 30 tokens.
- **References and whether each resolves:**

| Reference | Where | Class | Result |
|---|---|---|---|
| `../../references/checklist.md` | ext SKILL.md:10 | `../` escape, two levels above the skill folder | **Nowhere.** In the pinned copy it resolves to `/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/dangling-refs/references/checklist.md`, which doesn't exist (`ls` gave "No such file or directory"). It would not travel with an install. At user-global placement it would resolve to `~/.agents/references/checklist.md`, and at firstmate placement to `<repo>/.agents/references/checklist.md`. Both are absent (`ls`: "No such file or directory"). `find /tmp/fmsa-r5 -name checklist.md` found nothing. |
| `test-driven-development` skill "from this collection" | ext SKILL.md:11 | sibling-skill name | **Nowhere.** It isn't in the folder (one file only) and isn't on the live surface (`bin/fm-skill-surface.py` lists no such name). `find` across `/tmp/fmsa-r5`, `~/.agents`, `~/.claude/skills`, `~/.codex/skills`, `~/.pi` and the firstmate repo found nothing. `grep -rn test-driven-development` over the firstmate `.agents`, `AGENTS.md` and the user skill roots also returned nothing (exit 1). |
| `https://release-guide.example.invalid/semver` | ext SKILL.md:12 | URL | **Nowhere.** `curl -sI` exited with code 6 (could not resolve host). `.invalid` is a reserved top-level domain that never resolves (my inference from RFC 6761; I didn't check the RFC during this run). |
| `v<major>.<minor>.<patch>` | ext SKILL.md:14 | tag format, not a path | n/a |

- **Tools and stack assumed:** a library or package with a test suite, a changelog, and version tags (ext SKILL.md:8, 11, 13, 14). No tool is named. `git` is implied by "Tag" (inferred), and `which git` → `/usr/bin/git`.
- **Intended audience:** a single maintainer or agent doing a release by hand. There's no mention of PRs, review, push, or delegation (inferred from the absence of any such text in ext SKILL.md:6-14).

## 3. What firstmate already has on this topic

No firstmate skill owns releases or changelogs. The skill-analyzer triage table maps no owner for this topic.

- `grep -rniE 'changelog|semver|release checklist|tag(ging)? (a |the )?(release|version)|cut a release'` over the firstmate `AGENTS.md`, `.agents/skills` and `docs` found only unrelated mentions in `docs/calm-mode-feasibility.md` (Pi's own changelog) and `docs/verification/muse.md:164` (Muse's version string).
- `grep -rniE '\brelease\b|...|git tag|version bump'` over `AGENTS.md` and `.agents/skills` found no release procedure. These lines touch the topic:
  - `AGENTS.md:199`: "release or submission work ships `direct-PR`" on `no-mistakes-prod-only` projects. Release work is routed through a delivery path, but no release procedure exists. The same rule appears at `.agents/skills/project-management/SKILL.md:43`.
  - `AGENTS.md:197`: release branches pass as `--base-branch`.
  - `AGENTS.md:229`: "When no-mistakes is selected, no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI".
  - The no-mistakes embedded commit prompt (`strings "$(command -v no-mistakes)" | grep -n`, string 201996): "If the change has any user-facing product impact, the type must use feat or fix so release automation can pick it up." This is adjacent to changelog writing, but it covers commit types, not a changelog.
- Live surface: `bin/fm-skill-surface.py | grep -iE 'release|version|changelog|tag|semver|checklist|test-driven'` matched only `reverse-engineer-anything`, through the words "compare versions". It's off topic. There is no exact name match and no `same-content-as` entry for `dangling-refs`.
- User skills: `grep -rliE 'changelog|semver'` over the user skill roots matched only `~/.codex/skills/.system/skill-creator/SKILL.md:115` (advice against shipping a changelog inside a skill) and `plugin-creator/references/plugin-json-spec.md:207` (plugin manifest semver). Neither is about project releases.

## 4. Overlap map

| External piece | Firstmate today | Class |
|---|---|---|
| ext SKILL.md:1-4 frontmatter (name, description, no license, model-invocable by default) | Model invocation must start disabled for any adopt (skill-analyzer Decision rules). No owner (section 3 searches). | noise (no usable content in itself) |
| ext SKILL.md:6-8 title and one-line scope "Prepare a library for a tagged release." | Empty search (section 3) | noise (heading only) |
| ext SKILL.md:10 "Work through the shared checklist in `../../references/checklist.md` and tick each item." | Target missing at every placement (section 2) | noise (dangling; the real content is unknown) |
| ext SKILL.md:11 "Confirm the test suite passes using the `test-driven-development` skill from this collection." | On no-mistakes projects the pipeline owns tests: `AGENTS.md:229`. The named skill exists nowhere (section 2). | already-done (test gate on the no-mistakes path); the reference itself dangles |
| ext SKILL.md:12 "Follow the versioning guide at https://release-guide.example.invalid/semver before choosing the next number." | URL unresolvable (`curl -sI` exit 6) | noise (dangling) |
| ext SKILL.md:13 "Update the changelog with one line per user-visible change." | Empty search for `changelog` in firstmate. Closest is the no-mistakes commit-type rule for release automation (string 201996), which is a different step. | new (one sentence, generic) |
| ext SKILL.md:14 "Tag the release as `v<major>.<minor>.<patch>`." | Empty search for `git tag`, `semver`, `tag ... release` in firstmate | new (one sentence, generic) |

Summary: 1 already-done, 2 new, 4 noise. The two `new` rows add up to two sentences, less than a paragraph.

## 5. Conflicts and safety

**Conflict table.** No rule is directly contradicted by quoted text. The skill never mentions push, PR, merge, or review. Inferred risks follow (not clashes):

| External | Firstmate | Assessment |
|---|---|---|
| ext SKILL.md:14 "Tag the release as `v<major>.<minor>.<patch>`." | `AGENTS.md:29-30` hard rule 1: "Never write to a project. Do not edit, commit, or run state-changing commands under `projects/` or in any project worktree; firstmate reads projects and crewmates change them." `AGENTS.md:199`: "release or submission work ships `direct-PR`". | Inferred risk. A tag is a state-changing project operation, and pushing it publishes immediately with no PR. Firstmate has no rule saying who creates or pushes tags, or under what merge authority. Any future release skill must route tagging through a crewmate and the project's delivery path. This text gives no such guidance. |
| ext SKILL.md:11 "Confirm the test suite passes using the `test-driven-development` skill" | `AGENTS.md:229`: "no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI" | Overlap only on the no-mistakes path. Not a clash, because the named skill doesn't exist to load. |

**Vocabulary collisions.** The skill uses none of the firstmate labels for severity (`error`/`warning`/`info`), finding actions (`auto-fix`/`no-op`/`ask-user`), or task states (`working`/`needs-decision`/`blocked`/`paused`/`done`/`failed`); this is from reading all 14 lines. Its only new terms are "tick each item" (ext SKILL.md:10), "tag" and "release" (ext SKILL.md:3, 14). "release" is a word clash only: firstmate's captain-hold "release" means freeing a held task to proceed (`.agents/skills/captain-hold-lifecycle/SKILL.md:31`, `.agents/skills/bearings/SKILL.md:105`), a different sense. That's minor.

**Safety findings**
- No scripts, binaries, archives, bytecode, or images (one ASCII file).
- No text aimed at a reviewer, scanner, or assistant: `grep -niE 'ignore|reviewer|scanner|assistant|claude|system prompt|curl|wget|bash|eval|base64|token|secret|password|key'` returned nothing (exit 1).
- No base64-like blobs: `grep -nE '[A-Za-z0-9+/]{40,}'` returned nothing (exit 1). No secrets.
- ext SKILL.md:12 tells the agent to fetch a remote page and follow its instructions. It doesn't say to execute anything, so it isn't remote execution under the `unsafe` rule. Still, any skill that sends an agent to follow live remote text is an injection channel. Here the host can't resolve (`curl -sI` exit 6), so the risk is latent rather than live (inferred).
- ext SKILL.md:10 escapes the skill folder by `../../`. Installed, it would read whatever sits at `~/.agents/references/checklist.md` or `<repo>/.agents/references/checklist.md`. Anyone who can write that path could plant instructions there (inferred). Both paths are absent today.
- Size and bytes per line fit the stated purpose (627 bytes over 14 lines).

**Trigger analysis**
- Exact description: "Write a release checklist for a library before tagging a version. Use when preparing a release of a package."
- Broad phrases: none of `any change`, `before merging`, `always`, `any task`, `whenever`, `every time`, `all code` (`grep -niE` exit 1). The surface tool also gave no `broad-trigger:*` flag.
- Same-topic installed descriptions: none (section 3).
- Model-invocation default: `auto` (surface row column `model_invocation`). An adopt would have to set `disable-model-invocation: true`.

## 6. Fit and cost

- **Stack:** generic library or package releases. No firstmate project stack is assumed, and the skill doesn't name one.
- **Human-in-the-loop assumptions:** it assumes one actor who can tick a checklist, read a website, choose a version number, and tag locally (ext SKILL.md:10-14). There's no handling for autonomous workers, PRs, or merge authority (inferred from what's absent).
- **Tool availability:** `which git` → `/usr/bin/git`. No other tool is named. The referenced skill, file, and URL are unavailable (section 2).
- **Context cost:** about 30 tokens of description at every session at `auto` invocation, and about 157 tokens per full load. That's cheap, but most of what gets loaded is three pointers to nothing.
- **Who would load it:**
  - trial-only: only the session given `pi --skill <path>` or "read `<path>`";
  - one project's `.agents/skills`: workers in that project;
  - `~/.agents/skills` plus `~/.claude/skills`: every Pi or Claude worker on the machine;
  - firstmate `.agents/skills`: firstmate and its crew in this repo.
  - At every placement, steps 10-12 fail the same way (section 2).

## 7. Recommendation

Decline (malformed). These facts settle it:

1. The body's substance is in three references and none resolve: ext SKILL.md:10 (file missing at the pinned copy and at every install placement), ext SKILL.md:11 (the sibling skill exists nowhere), ext SKILL.md:12 (`curl -sI` exit 6 on a `.invalid` host).
2. The remainder is two generic sentences (ext SKILL.md:13-14). That's less than a paragraph, so the rule that would turn `malformed` into `harvest` doesn't apply. Fixing it isn't trivial either, because the checklist's content is unknown.
3. No firstmate owner exists to harvest into (section 3), and there's no license (section 2), so none of the text can be copied in any case.
4. Adopting it as-is would teach workers to read a missing file outside the skill folder and follow an unreachable remote guide (section 5).

If firstmate later wants a release procedure, it should be a firstmate-native skill written from scratch. It would need to cover changelog lines, the tag format, who tags, which delivery path the work ships on (`AGENTS.md:199`), and merge authority. Nothing from this text needs to come along.

## 8. Captain's decision

- **A (recommended):** accept the decline. Nothing is installed or kept.
- **B:** point firstmate at the full upstream collection: the repo that carries `references/checklist.md`, the `test-driven-development` skill, and a license. A fresh analysis would then pin it by commit.
- **C:** open a separate task to write a firstmate-native release-checklist skill from scratch (tagging only through a crewmate and the project's delivery path), unrelated to this candidate.

## 9. Evidence

**Pinned file list** (`find .../input -type f -exec file {} \; -exec sha256sum {} \; -exec wc -lc {} \;`):

```
.../input/dangling-refs/SKILL.md: ASCII text
ff3b1bc41c64677f3b5d0ecaa561dd62e0b854eee5fe1a29305457ed4cd28857  .../input/dangling-refs/SKILL.md
 14 627 .../input/dangling-refs/SKILL.md
```

`ls -la .../input/dangling-refs`: `SKILL.md` (627 bytes) only, no dotfiles.
`git -C .../input rev-parse HEAD`: `fatal: not a git repository (or any parent up to mount point /)`, so there is no commit to pin.

**Candidate surface row** (`bin/fm-skill-surface.py --root candidate=/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/dangling-refs/input`):

```
scope	name	dir	description	model_invocation	lines	bytes	flags
candidate	dangling-refs	/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/dangling-refs/input/dangling-refs	Write a release checklist for a library before tagging a version. Use when preparing a release of a package.	auto	14	627	-
```

**Live surface** (`bin/fm-skill-surface.py`, default roots): 51 skills across the firstmate, user-agents, user-claude and user-codex roots. There is no row named `dangling-refs` or `test-driven-development`. The only name collision reported is unrelated: `skill-creator` in user-claude and user-codex. Filtering for `release|version|changelog|tag|semver|checklist|test-driven` matched only `reverse-engineer-anything` ("compare versions").

**Reference resolution**

```
ls -la .../input/dangling-refs/../../references/checklist.md   -> No such file or directory
realpath -m -> /tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/dangling-refs/references/checklist.md
ls -la ~/.agents/references/checklist.md <repo>/.agents/references/checklist.md -> No such file or directory (both)
find /tmp/fmsa-r5 -name checklist.md -> (empty)
find / -xdev -path '*/references/checklist.md' -> (empty)
find /tmp/fmsa-r5 ~/.agents ~/.claude/skills ~/.codex/skills ~/.pi <repo> -name 'test-driven-development*' -> (empty)
grep -rn test-driven-development <repo>/.agents <repo>/AGENTS.md ~/.agents/skills ~/.claude/skills ~/.codex/skills (minus skill-analyzer) -> exit 1
timeout 15 curl -sI https://release-guide.example.invalid/semver -> no output, exit 6
which git gh gh-axi -> /usr/bin/git, .../gh, .../gh-axi
```

**Content scans of the candidate**

```
grep -niE 'any change|before merging|always|any task|whenever|every time|all code' -> exit 1
grep -niE 'ignore|reviewer|scanner|assistant|claude|system prompt|curl|wget|bash|eval|base64|token|secret|password|key' -> exit 1
grep -nE '[A-Za-z0-9+/]{40,}' -> exit 1
grep -niE 'license' -> exit 1
wc -w -> 87
```

**Owner searches** (firstmate repo `/home/hugo/.no-mistakes/worktrees/3f83383b2e86/01M66J7TBMNGZSZPZQX5FC74XP`):
- `grep -rniE 'changelog|semver|release checklist|tag(ging)? (a |the )?(release|version)|cut a release'` over `AGENTS.md`, `.agents/skills` and `docs` found only `docs/calm-mode-feasibility.md:17,498,504,679` and `docs/verification/muse.md:164`, all unrelated.
- `grep -rniE '\brelease\b|\breleases\b|git tag|\bv<major|version bump|bump.*version'` over `AGENTS.md` and `.agents/skills` found only delivery-routing and hold-"release" lines, among them `AGENTS.md:197,199`, `project-management/SKILL.md:43`, `captain-hold-lifecycle/SKILL.md:31` and `bearings/SKILL.md:105`.
- Owner text read: `AGENTS.md:19-55` (hard rules), `AGENTS.md:227-247` (delivery path and merge authority), `AGENTS.md:195-200`.
- `strings "$(command -v no-mistakes)" | grep -niE 'changelog|semver|git tag|release notes'` found only the internal symbols `update.semVersion.compare` (no changelog prompt).
- `... | grep -niE 'user-visible'` found the commit-type rule at strings 201996, 202372 and 202459 ("so release automation can pick it up").
- `grep -niE 'changelog|semver|\btag\b|release' ~/.agents/skills/no-mistakes/SKILL.md` found only line 270, which uses "released" for a branch, not a release.

**Not verified, and why**
- No commit pin: the folder isn't in a git repository, so it is pinned by its sha256 only.
- That `.invalid` can never resolve is taken from RFC 6761 knowledge, not checked during the run. The observed fact is `curl -sI` exit 6.
- `find / -xdev` may not cross into `/tmp` if `/tmp` is a separate filesystem, so `/tmp/fmsa-r5` was searched explicitly as well.
- I didn't check what the missing checklist or the missing `test-driven-development` skill contain, because neither exists anywhere reachable.
- I didn't run the completion gate (skill-analyzer Tier 1 step 8, `bin/fm-captain-hold.sh complete`). This run was scoped to writing this report only, with no task id or state writes. Firstmate runs it when relaying section 8, using `--none` if the captain takes option A.
- I didn't run any trial (skill-analyzer Rules: no trial inside an analysis).

done: verdict decline (malformed)
