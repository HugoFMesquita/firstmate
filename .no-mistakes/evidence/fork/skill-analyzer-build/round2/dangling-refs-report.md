# Skill analysis: dangling-refs (local folder `input/dangling-refs`)

## 1. Verdict

`decline (malformed)`. Placement: none. Confidence: **high**.
Three of the five steps (ext SKILL.md:10, :11, :12) depend on a checklist file, a sibling skill, and a URL. None of them resolves from the pinned copy (section 2).
The two steps that work (ext SKILL.md:13, :14) are one-line project conventions, so the malformed-to-harvest exception does not apply (skill-analyzer SKILL.md:77).
What would change it: the captain supplying the complete source collection, meaning the repository that holds `references/checklist.md` and its own `test-driven-development` skill. That would be a new analysis against a new pin, not a revision of this one.

## 2. What the skill is

- **Source:** local folder `/tmp/fm-skill-analyzer-live.WuCq0d/dangling-refs/input/dangling-refs`. The task supplied it as an already-pinned local copy, so nothing was fetched.
- **Pinned commit:** none. The folder is not inside a git repository (`git -C … rev-parse HEAD` → `fatal: not a git repository`), so it is pinned by its file hashes alone (section 9).
- **License:** none stated. The frontmatter has no `license` field (ext SKILL.md:1-4), there is no LICENSE file, and `grep -inE 'license|LICENSE'` found nothing (exit 1). Provenance is unknown.
- **Size:** 1 file, 14 lines, 627 bytes, about 160 tokens per load (bytes / 4). The longest line is 121 characters.
- **Files:** `SKILL.md` (ASCII text, sha256 `ff3b1bc41c64677f3b5d0ecaa561dd62e0b854eee5fe1a29305457ed4cd28857`). There are no dotfiles, scripts, binaries, archives, or images.
- **Frontmatter:** `name: dangling-refs` (matches the folder name; `fm-skill-surface.py` raised no flags) and `description: Write a release checklist for a library before tagging a version. Use when preparing a release of a package.` (108 characters).
  There is no `disable-model-invocation` field, so the default is model-invocable (`auto`), and there are no non-spec fields.
  Observation: the name describes nothing about the skill's purpose, which is a release checklist.
- **References and whether each resolves:**

| Ref | Where | Resolution |
|---|---|---|
| `../../references/checklist.md` | ext SKILL.md:10 | **Nowhere.** It escapes the skill folder by two levels, to `/tmp/fm-skill-analyzer-live.WuCq0d/dangling-refs/references/checklist.md`, which does not exist (`ls`: No such file or directory). There is no enclosing repository, and a machine-wide `find / -name checklist.md -path '*references*'` returned nothing. Even if the file existed, it would sit outside the skill folder and would not travel with an install. |
| `test-driven-development` skill "from this collection" | ext SKILL.md:11 | **Not in the collection.** The pinned copy has no sibling skills. No installed skill root has it (the `fm-skill-surface.py` listing has no such name, and `grep -rIn test-driven-development` across firstmate, `~/.agents/skills`, and `~/.claude/skills` came back empty). The only directory with that name on the machine is `/home/hugo/.codex/.tmp/plugins/plugins/superpowers/skills/test-driven-development`. That is an unrelated Codex plugin cache from a different collection, and it is not a root that `fm-skill-surface.py` inventories. |
| `https://release-guide.example.invalid/semver` | ext SKILL.md:12 | **Nowhere.** It uses the reserved `.invalid` TLD. `curl -sI --max-time 10` exited 6 (could not resolve host), so there was no HTTP status. |

- **Tools and stack assumed:** git, implied by "Tag the release" at ext SKILL.md:14 (`/usr/bin/git` is present), plus an unspecified test runner and changelog file. The stack is "a library / package" (ext SKILL.md:3, :8), with no language named.
- **Intended audience:** a library maintainer who prepares a release by hand and ticks off checklist items (ext SKILL.md:10).

**Capability inventory**

| # | ext line | Block | Imperative strength | Vocabulary introduced | Tools called | Audience |
|---|---|---|---|---|---|---|
| C1 | SKILL.md:2-3 | Trigger | "Use when" (soft trigger) | "release checklist", "tagging a version" | none | the model's skill router |
| C2 | SKILL.md:6-8 | Title and purpose | declarative | "tagged release" | none | release preparer |
| C3 | SKILL.md:10 | Work through the shared checklist and tick each item | imperative, unconditional | "shared checklist", "tick" | file read of `../../references/checklist.md` (dangling) | human-style checklist worker |
| C4 | SKILL.md:11 | Confirm the test suite passes via the `test-driven-development` skill | imperative | "this collection" | skill `test-driven-development` (unresolved) | agent with access to that collection |
| C5 | SKILL.md:12 | Follow an external versioning guide before choosing the number | imperative, plus a fetch instruction | none | web fetch (unresolvable URL) | agent with network access |
| C6 | SKILL.md:13 | Changelog: one line per user-visible change | imperative | "user-visible change" | file edit | release preparer |
| C7 | SKILL.md:14 | Tag as `v<major>.<minor>.<patch>` | imperative | none | git tag (implied) | release preparer |

## 3. What firstmate already has on this topic

- No firstmate skill owns releases, changelogs, or tagging.
  - `python3 bin/fm-skill-surface.py | grep -Ei 'release|changelog|semver|version|tag'` matched only `reverse-engineer-anything` ("compare versions"), which is off topic.
  - `grep -rInEi 'changelog|release checklist|semver|git tag|tagging|tag the release'` across `AGENTS.md`, `.agents/skills`, and `docs` matched only prose in `docs/calm-mode-feasibility.md` and `docs/gerrit-forge-integration.md` and `docs/verification/muse.md`, none of it release procedure.
- Adjacent owners (read at the cited lines):
  - `AGENTS.md:230`: "When no-mistakes is selected, no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI".
  - `AGENTS.md:199`: on `no-mistakes-prod-only` projects, "release or submission work ships `direct-PR`". This classifies delivery for release work; it is not a release procedure.
  - `AGENTS.md:233-237` (selected delivery path): each mode ends at a PR or a clean ready branch and "waits for the configured merge authority".
  - `AGENTS.md:28` (hard rule 1, never write to a project) and `AGENTS.md:33` (hard rule 2, never merge without the captain's word).
  - The no-mistakes binary contains an "update documentation" step (`strings "$(command -v no-mistakes)"`). Its strings have no changelog, release-notes, or `git tag` matches (`grep -iE 'changelog|release (notes|checklist)|git tag'` came back empty).
- Topic owner under the triage mapping (skill-analyzer SKILL.md:47): **none**.

## 4. Overlap map

| External piece | Firstmate today | Class |
|---|---|---|
| C1 trigger, ext SKILL.md:3 | No owner (section 3 searches came back empty) | new (topic) |
| C3 shared checklist, ext SKILL.md:10 | The referenced content does not exist, so nothing can be compared | noise (dangling) |
| C4 tests pass via TDD skill, ext SKILL.md:11 | `AGENTS.md:230`: no-mistakes "alone owns … tests" | already-done (and the skill it names is dangling) |
| C5 external versioning guide, ext SKILL.md:12 | Unresolvable URL, no content | noise (dangling) |
| C6 changelog one line per user-visible change, ext SKILL.md:13 | `AGENTS.md:230` gives documentation to no-mistakes when it is selected. No firstmate changelog convention (`grep … changelog` empty, section 3) | new (one sentence; a per-project convention) |
| C7 tag `v<major>.<minor>.<patch>`, ext SKILL.md:14 | `AGENTS.md:233-237`: delivery ends at a PR or ready branch and waits for merge authority. No firstmate step creates tags | clash (inferred, see section 5) |

Totals: 1 already-done, 2 new (one is the bare topic, one is a single sentence), 2 noise, 1 clash.
That falls short of the four-in-five duplicate rule. Nothing `new` is worth more than a paragraph.

## 5. Conflicts and safety

**Conflict table**

| External (quoted) | Firstmate (quoted) | Nature |
|---|---|---|
| "Tag the release as `v<major>.<minor>.<patch>`." (ext SKILL.md:14) | "**no-mistakes** runs the full pipeline through a PR, then waits for the configured merge authority." / "**local-only** has the worker stop with a clean ready branch, then waits for the configured merge authority" (`AGENTS.md:235`, `:237`) | Inferred. Tagging a release is a publication step after the merge, and no delivery mode lets a worker take it. A worker loading this skill inside a ship would tag a commit that has not landed. |
| "Confirm the test suite passes using the `test-driven-development` skill" (ext SKILL.md:11) | "no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI" / "Never hold work outside no-mistakes for a manual clean verdict" (`AGENTS.md:230`, `:231`) | Mild. It adds a test gate that sits outside the selected path. |

**Vocabulary collisions**
- None against error/warning/info, auto-fix/no-op/ask-user, or working/needs-decision/blocked/paused/done/failed.
- The new terms ("shared checklist", "tick", "this collection", "user-visible change") do not overlap any status or review label.

**Safety findings**
- No injection or reviewer-addressed text. `grep -inE 'ignore (all|previous)|reviewer|scanner|assistant|you are|system prompt|curl|wget|bash|base64|eval|sh -c|token|password|secret|api[_-]?key'` exited 1.
- No non-ASCII bytes (`grep -nP '[^\x00-\x7F]'` exited 1), and no opaque files, archives, or binaries.
- No remote fetch-and-execute. ext SKILL.md:12 does tell the agent to fetch and *follow* an external page, which is an instruction-from-the-network pattern. It is inert here only because the host cannot resolve.
- ext SKILL.md:10 escapes the folder with `../../`, which is a path-escape pattern. The target does not exist.
- None of these reaches `unsafe`.

**Trigger analysis**
- Exact description: "Write a release checklist for a library before tagging a version. Use when preparing a release of a package."
- Broad phrases: none (`grep -inE 'any change|before merging|always|any task|whenever|every time|all code'` exited 1; `fm-skill-surface.py` raised no `broad-trigger` flag).
- Same-topic installed descriptions: none (section 3).
- Model-invocation default: `auto`. No `disable-model-invocation` is set, so as shipped it would fire on any "prepare a release" request, and three of its five steps would then fail.

## 6. Fit and cost

- **Stack:** generic library release, no language named. Firstmate projects deliver through PRs or ready branches. Releases and tags are not a delivery step, and section 7 has no tag step.
- **Human-in-the-loop assumptions:** "tick each item" (ext SKILL.md:10) assumes someone works through a checklist by hand. "Before choosing the next number" (ext SKILL.md:12) assumes a person picks the version, with no rule for an autonomous worker.
- **Tool availability:** `which git` → `/usr/bin/git`. The skill names no other tools. The `test-driven-development` skill it depends on is unavailable in every inventoried root.
- **Context cost:** about 30 tokens of description per session at any auto-invocable placement, and about 160 tokens per full load. The cost is fine; the problem is the content.
- **Who would load it:**
  - User-global `~/.agents/skills` (with the `~/.claude/skills` symlink) would expose it to Pi and Claude workers on every project.
  - A project's `.agents/skills` would expose it to workers in that project.
  - Firstmate's own `.agents/skills` would only be loaded by a running firstmate (`AGENTS.md:408`) and is off topic there.

## 7. Recommendation

Decline (malformed). The facts that settle it:

1. **Dangling references.** The body's substance lives in three external artifacts, and none of them resolves from the pinned copy:
   - `../../references/checklist.md` is missing, and it sits outside the folder anyway, so it would not travel.
   - The `test-driven-development` skill "from this collection" is absent; the one on this machine belongs to an unrelated Codex plugin cache.
   - `https://release-guide.example.invalid/semver` cannot resolve (curl exit 6).

   Installed as shipped, the skill would tell a worker to read a file that does not exist, call a skill that does not exist, and follow a page that cannot be fetched.
2. **No trivial fix.** Repairing it would mean writing the checklist and the versioning guide from scratch, which is new-skill work and outside this skill's scope (skill-analyzer SKILL.md:6).
3. **Nothing worth harvesting.** The two rows that work are one-line project conventions (C6 changelog format, C7 tag format). They belong in a project's own `AGENTS.md` or `CONTRIBUTING.md` if that project wants them, not in a firstmate owner. C7 also clashes with the delivery path (section 5).
4. **No license.** The folder has no license or provenance, so even its text could not be copied; any future use would have to re-derive the idea.

The clash in point 3 would alone support `decline (conflict)`, and point 4 would support `decline (unlicensed)`. Every route leads to decline; `malformed` is reported as the class the observed facts establish most directly.

## 8. Captain's decision

None.

## 9. Evidence

**Pinned file list**

```
$ find …/input -type f -exec sha256sum {} \;
ff3b1bc41c64677f3b5d0ecaa561dd62e0b854eee5fe1a29305457ed4cd28857  /tmp/fm-skill-analyzer-live.WuCq0d/dangling-refs/input/dangling-refs/SKILL.md
$ file …/SKILL.md
SKILL.md: ASCII text
$ wc -lc …/SKILL.md
14 627
$ ls -la …/input/dangling-refs
SKILL.md (627 bytes), no dotfiles
$ git -C …/input/dangling-refs rev-parse HEAD
fatal: not a git repository (or any parent up to mount point /)   [exit 128]
```

**Reference resolution**

```
$ ls -la …/input/dangling-refs/../../references/checklist.md …/dangling-refs/references …/input/references
ls: cannot access …: No such file or directory   (all three)
$ find / -path /proc -prune -o -name checklist.md -path '*references*' -print
(empty)
$ find / \( -path /proc -o -path /sys \) -prune -o -type d -name test-driven-development -print
/home/hugo/.codex/.tmp/plugins/plugins/superpowers/skills/test-driven-development
$ grep -rIn test-driven-development <firstmate>/.agents <firstmate>/AGENTS.md <firstmate>/docs ~/.agents/skills ~/.claude/skills
(empty)
$ curl -sI --max-time 10 https://release-guide.example.invalid/semver; echo exit=$?
exit=6
```

**Surface**
- `python3 bin/fm-skill-surface.py` (with `FM_HOME` unset, so the code root is the home) ran across the firstmate, user-agents, user-claude, and user-codex roots. It found no `dangling-refs` name match, no release, changelog, or tag skill, and no `same-content-as` entry for the candidate.
- `fm-skill-surface.py --root ext=…/input` reported `dangling-refs … auto 14 627 -` (no flags).

**Scans:** the broad-phrase, injection/secret, non-ASCII, and license greps are quoted in sections 2 and 5. They all exited 1 (no match).

**Owner text read:** `AGENTS.md:19-50` (prime directives), `AGENTS.md:165-259` (section 7), `.agents/skills/ship-landing/SKILL.md` (whole file), and the no-mistakes binary strings (grep quoted in section 3).

**Not verified, and why**
- The no-mistakes embedded documentation prompt was only grepped, not read in full. Its strings are interleaved with Go runtime data, and the verdict does not depend on whether it mentions changelogs.
- `FM_HOME` was unset, so the surface used the code-root home. Any project-level skills under a separate supervising home were not inventoried.
- The `captain-hold-lifecycle` completion gate was not run. `bin/fm-captain-hold.sh complete --none` writes to the home's backlog, and this task allowed no writes outside the report and a temporary directory. The reviewed surface leaves nothing waiting on the captain, so the gate would be `--none`. Firstmate should run it in the supervising home.
- I did not read the Codex-cache `test-driven-development` skill. It belongs to a different collection and would not satisfy "from this collection" whatever it says.
- Nothing in the skill under test was executed, followed, or fetched for. The single `curl -sI` against its URL was the HEAD-only resolution check that step 2 allows.
