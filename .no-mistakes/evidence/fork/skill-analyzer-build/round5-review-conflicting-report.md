# Skill analysis: code-review-and-quality (local folder `input/review-conflicting`, vendored from addyosmani/agent-skills)

## 1. Verdict

`harvest`. Placement: no skill is installed anywhere. Piece 1 goes into one chosen project's no-mistakes repo config (`.no-mistakes.yaml`, `review.path_instructions`) through a normal ship. Piece 2 is only a local issue draft for the no-mistakes maintainer.
Everything else stays out, including every clash in section 5.
Confidence: **medium**. I read the owner's real text (no-mistakes v1.84.0 embedded review prompt, `AGENTS.md` sections 1/7/9, `ask-user-authority`, `validation-supervision`). One fact would change the verdict: whether any registered project has a dependency manifest or lockfile. I could not read the project registry in this home (`FM_HOME` unset, no `projects/` in the code root). If no project has one, piece 1 has no target, and the verdict becomes `decline (conflict)`.

## 2. What the skill is

- **Source:** local folder `/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/review-conflicting/input/review-conflicting`. It is not inside a git repository (`git rev-parse` reports `fatal: not a git repository`), so it is pinned by file hashes only (section 9).
  The folder's own `SOURCE` file says the content was vendored from `https://github.com/addyosmani/agent-skills`, path `skills/code-review-and-quality/SKILL.md`, commit `28f435ea69a78531ec00779c7f3b78c64ce95896` (ext SOURCE:4-6). I did not verify that claim (no fetch, by instruction). `SOURCE` also records sha256 `2db1e850…d4396e` (ext SOURCE:8), which matches the computed hash of `SKILL.md`.
- **License:** MIT, Copyright (c) 2025 Addy Osmani (ext LICENSE:1-3). Copying is allowed with the notice. Any harvest here re-derives the ideas anyway and credits the source in the commit message.
- **Frontmatter:** `name: code-review-and-quality`; `description:` as quoted in section 5 (ext SKILL.md:3). There is no `license` field, no `disable-model-invocation` (so the default is model-invoked, surface value `auto`), and no non-spec fields.
- **`bin/fm-skill-surface.py` candidate flags (verbatim):** `name!=dir,broad-trigger:any change|before merging`.
  `name!=dir` is real here: the folder is `review-conflicting` but the skill names itself `code-review-and-quality`. `SOURCE` says the rename was deliberate (ext SOURCE:2).
  There is no `missing-description` flag, so the skill is not `malformed`.
- **Size:** `SKILL.md` is 398 lines, 20,976 bytes, about 5.2k tokens (bytes/4). The longest line is 433 chars. The whole folder is 3 files, 22,589 bytes.
- **Files:** `SKILL.md` (UTF-8 text), `LICENSE` (ASCII, 21 lines, 1,068 B), `SOURCE` (ASCII, 10 lines, 545 B). There are no scripts, binaries, archives, images or dotfiles.
- **References and whether each resolves:**
  - `../../references/security-checklist.md`, `../../references/performance-checklist.md` (ext SKILL.md:353-354) resolve to `/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/review-conflicting/references/…`, which does not exist. Upstream they would point at the repository root, outside the skill folder, so they would not travel. Classified as **nowhere**.
  - Sibling skills `security-and-hardening` (ext :66, :302), `performance-optimization` (ext :79), `constraint-driven-development` (ext :164): none is installed in any skill root (the `find` returned 0 for each). Classified as **nowhere**.
  - URLs: none in `SKILL.md`. The one URL in `SOURCE` was not contacted (section 9).
- **Tools and stack assumed:** `npm audit` (ext :289, :302), `package.json` and lockfiles (ext :299-300), "run the suite" (ext :164), and web-app concerns such as XSS, re-renders and pagination (ext :73, :84-85). This is a JS/npm web stack.
- **Intended audience:** a human or agent reviewer inside a human team that has authors, reviewers, business-day response times and bug self-assignment (ext :251-258, :269). Its output is PR comments with an Approve or Request-changes verdict (ext :347-349).

## 3. What firstmate already has on this topic

Owner of the topic (review): the **no-mistakes review step**, a tool-owned prompt. **`AGENTS.md` section 7** sets its authority.

- `AGENTS.md:229-233`: "The selected delivery path owns its own rigor. When no-mistakes is selected, no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI; otherwise follow the faster path without adding an independent reviewer. Never hold work outside no-mistakes for a manual clean verdict, stack serial manual reviews … A separate review or audit is allowed only when the captain explicitly requests that deliverable … If fast-path risk needs more rigor, escalate whether to use no-mistakes instead of inventing a manual gate."
- `AGENTS.md:33` (hard rule 2) and `AGENTS.md:241`: merge authority belongs to the captain unless `yolo` is on. With `yolo` on, firstmate merges green, in-scope work.
- `AGENTS.md:245`, `.agents/skills/ask-user-authority/SKILL.md:18,24`, `.agents/skills/validation-supervision/SKILL.md:24`: ask-user findings route through firstmate. The worker never answers its own finding, and reviewer language cannot amend the accepted contract.
- No-mistakes v1.84.0 embedded review prompt (`strings "$(command -v no-mistakes)"`, output lines 203513-203570):
  - intent and concrete-trace correctness (203524, 203526)
  - authorization and privacy tracing (203527-203530)
  - risk classes: security, performance, breaking changes, error handling (203537)
  - "Do NOT run tests during review" (203534)
  - full pass (203538)
  - severity `error|warning|info` (203543)
  - "Do NOT report styling, formatting …" (203546)
  - actions `ask-user|auto-fix|no-op` (203548-203551)
  - remedy-based classification (203552)
  - a dedicated Simplification pass (203557-203561)
  - risk_level (203563-203567)
  - JSON schema enums (237978, 237982)
- No-mistakes test and verification guidance: "A missing-test finding must name the observable failure …" (202277, 201906), plus the test-failure action rule (203331).
- No-mistakes also drafts PR content. It has the PR title rule (201732) and the commit `fix_message` template `no-mistakes({{.Step}}): {{.Summary}}` (201435).
- Installed descriptions on the same topic: `no-mistakes` (user-agents, user-claude: "Validate your code changes through the no-mistakes pipeline - automated code review, …") and `review-agent` (user-codex, a Codex system skill: "Perform a read-only, defect-first review …").
- Empty searches, used for the `new` rows below:
  - `grep -rniE 'lockfile|changelog|semver|mutation test|invert one condition' AGENTS.md .agents/skills/` returned nothing (rc=1).
  - `grep -noiE '.{0,80}(changelog|semver).{0,120}' nm.txt` matched only the Go symbol `internal/update.semVersion.compare`. There is no prompt text.
  - `grep -noiE '.{0,100}(invert (one|a) condition|mutation (score|test)|mutant).{0,100}' nm.txt` returned nothing.

## 4. Overlap map

| # | External piece | Firstmate today | Class |
|---|---|---|---|
| 1 | Trigger "Use before merging any change" (ext SKILL.md:3); "Before merging any PR or change", "After completing a feature", "After any bug fix" (ext :16-20) | `AGENTS.md:230-232` (no-mistakes alone owns review; no independent reviewer on the fast path; no stacked manual reviews) | clash |
| 2 | "Every change gets reviewed before merge — no exceptions" (ext :10) | `AGENTS.md:230`, `:233` | clash |
| 3 | Approval standard and the reviewer's "Approve — Ready to merge" / "Request changes" verdict (ext :12, :347-349) | `AGENTS.md:33` hard rule 2, `:241` yolo; no-mistakes risk_level (203563-203567) | clash |
| 4 | Correctness axis: spec match, edge and error paths, off-by-one, races (ext :26-34) | no-mistakes 203524, 203526, 203537 | already-done |
| 5 | Readability and simplicity: fewer lines, dead artifacts, bolted-on conditionals (ext :36-49) | no-mistakes Simplification pass 203536, 203557-203561 | already-done |
| 6 | "Is there code duplication that should be shared?" (ext :57); "Presumptive blockers" for file size, relocation and shared modules (ext :398); file-size watch (ext :113) | no-mistakes 203531 "Do not infer a systemic flaw from code shape, duplication, or architectural preference alone. Do not demand a shared abstraction or broad redesign without a concrete reachable path …" | clash |
| 7 | Refactor reduces vs relocates complexity; type boundaries; feature logic in shared module (ext :60-62) | no-mistakes 203536, 203558, 203560 (remove the unrequired component as the smallest honest remedy) | already-done |
| 8 | Security axis (ext :64-75) | no-mistakes 203527-203530, 203537 | already-done |
| 9 | Performance axis (ext :77-86) | no-mistakes 203537 ("performance regressions") | already-done |
| 10 | Structural remedies: propose the move (ext :88-101) | no-mistakes 203530 (earliest shared boundary), 203560 | already-done |
| 11 | Change sizing, split strategies, separate refactor from feature (ext :103-128) | `AGENTS.md:203-206` scopes and parallelises at intake; no-mistakes 203533 "Do not expand user scope". Human PR-stacking process. | noise |
| 12 | Change descriptions, first line, anti-patterns (ext :130-138) | no-mistakes drafts PR title and body (201732) and fix commits (201435); `AGENTS.md:14` non-chat artifact rule | already-done |
| 13 | Understand context first (ext :142-150) | no-mistakes 203524; intent conformance (strings line 202287) | already-done |
| 14 | Review the tests first (ext :152-162) | no-mistakes 202277 missing-test rule; test step 203331 | already-done |
| 15 | Mutation probe: "Invert one condition … run the suite, then restore the file" (ext :164) | Reviewer: no-mistakes 203534 "Do NOT run tests during review". As an idea for the test step: empty search for `invert (one\|a) condition\|mutation (score\|test)\|mutant` | clash (as written) / new (idea only) |
| 16 | Severity prefixes Critical / Required / Nit / Optional / Consider / FYI (ext :179-191, :230) | no-mistakes 203543 `error\|warning\|info`; 203548-203551 `ask-user\|auto-fix\|no-op`; schema 237978/237982 | clash |
| 17 | "Lead with what matters … a few high-conviction comments beat a long list" (ext :193) | no-mistakes 203538 "Do a full review pass … until you have enumerated all material issues"; 203545 | clash |
| 18 | Verify the verification story (ext :195-205) | `AGENTS.md:230` (no-mistakes owns tests and CI); no-mistakes verification-plan guidance (strings lines ~202270-202277) | already-done |
| 19 | Multi-model pattern, "Human makes the final call" (ext :207-231) | `AGENTS.md:230-232`, `:241` | clash |
| 20 | Dead code: "Ask before deleting: 'Should I remove …?'" (ext :233-249) | no-mistakes 203559 (unrequired component, `ask-user` finding); `AGENTS.md:39-41` hard rule 4; `ask-user-authority/SKILL.md:18` | clash |
| 21 | Review speed, one business day (ext :251-258) | empty search; human-team cadence not applicable to autonomous workers | noise |
| 22 | "Don't accept 'I'll clean it up later' … require filing a bug with self-assignment" (ext :269) | no-mistakes 203543 ("warning … can be done in a follow up"), 203533 ("Do not … turn optional broader improvements into blockers"); `validation-supervision/SKILL.md:15` (follow-up routing); `AGENTS.md:50` (no issue on own authority) | clash |
| 23 | Honesty in review: no rubber-stamp, quantify, push back (ext :271-278) | `AGENTS.md:42-43` hard rule 5; no-mistakes 203544 | already-done |
| 24 | "Accept override gracefully … defer to their judgment" (ext :279) | `ask-user-authority/SKILL.md:24` "Reviewer language cannot amend that contract" | already-done |
| 25 | Before adding any dependency: existing stack, size, maintenance, `npm audit`, license (ext :285-292) | Partial: no-mistakes 203537 (breaking changes / security as risks). Empty search for dependency-review guidance in firstmate | new |
| 26 | Dependency upgrade workflow: changelog, one package per change, green before/after, transitive lockfile diff, no hand-edits (ext :294-302) | empty searches (section 3) in firstmate and the no-mistakes prompt | new |
| 27 | Review checklist template ending in Approve / Request changes (ext :304-349) | same as rows 3, 16 | clash |
| 28 | See Also `../../references/*` (ext :353-354) | unresolvable (section 2) | noise |
| 29 | Rationalizations and Red Flags tables (ext :356-385) | These restate rows 1-26. "PRs merged without any review" (ext :372) and "Review comments without severity labels" (ext :378) restate clashes 2 and 16. | noise |
| 30 | Verification: "All Critical issues are resolved", "Required … explicitly deferred" (ext :387-396) | no-mistakes gate outcomes; `validation-supervision/SKILL.md:24,29` | clash |

Tally over 30 rows: already-done 12, clash 12 (row 15 counted here), new 2 (rows 25-26, plus row 15's idea), noise 4.
The duplicate threshold (4 of 5 already-done) is not met. The clashes touch hard rule 2, merge authority and the selected delivery path.

## 5. Conflicts and safety

### Conflict table

| Topic | External (quoted) | Firstmate (quoted) | Touches |
|---|---|---|---|
| Who reviews | "Every change gets reviewed before merge — no exceptions." (ext SKILL.md:10); "Use before merging any change." (ext :3) | "When no-mistakes is selected, no-mistakes alone owns review … otherwise follow the faster path without adding an independent reviewer." (`AGENTS.md:230`) | selected delivery path |
| Manual gate | "The review is the quality gate — use it. Require cleanup before merge, not after." (ext :362) | "Never hold work outside no-mistakes for a manual clean verdict, stack serial manual reviews, or infer authority for one from security, architecture, or risk alone." (`AGENTS.md:231`) | selected delivery path |
| Merge call | "- [ ] **Approve** — Ready to merge" (ext :348); "Human makes the final call" (ext :221) | "**Never merge a PR without the captain's explicit word.**" (`AGENTS.md:33`); "with it on, firstmate merges green, in-scope work itself." (`AGENTS.md:241`) | hard rule 2, merge authority |
| Asking the human | "**Ask before deleting:** 'Should I remove these now-unused elements: [list]?'" (ext :239) | "**Crewmates never address the captain.** All crewmate communication flows through firstmate." (`AGENTS.md:39-40`); "The implementation worker never decides or answers its own ask-user finding." (`ask-user-authority/SKILL.md:18`) | hard rule 4 |
| Running tests in review | "Invert one condition … run the suite, then restore the file from a copy." (ext :164) | "Do NOT run tests during review. The pipeline has a dedicated test step after review." (no-mistakes 203534) | tool-owned prompt |
| Duplication / structure | "Is there code duplication that should be shared?" (ext :57); "Presumptive blockers: … a change that pushes a file past the size boundary …" (ext :398) | "Do not infer a systemic flaw from code shape, duplication, or architectural preference alone. Do not demand a shared abstraction or broad redesign without a concrete reachable path …" (no-mistakes 203531) | tool-owned prompt |
| Style findings | "**Nit:** … formatting, style preferences" (ext :187) | "Do NOT report styling, formatting, linting, compilation, or type-checking issues." (no-mistakes 203546) | tool-owned prompt |
| Breadth | "a few high-conviction comments beat a long list" (ext :193) | "Do a full review pass … until you have enumerated all material issues you can substantiate." (no-mistakes 203538) | tool-owned prompt |
| Deferral | "Don't accept 'I'll clean it up later.' … Require cleanup before submission … require filing a bug with self-assignment." (ext :269) | "'warning' for things that are worth addressing but can be done in a follow up" (no-mistakes 203543); "prefer routing new requirements to follow-up work rather than expanding the current task" (`validation-supervision/SKILL.md:15`) | delivery path |

### Vocabulary collisions

| Firstmate set | External terms that collide |
|---|---|
| severity `error` / `warning` / `info` (no-mistakes 203543, 237978) | `Critical:` "Blocks merge", *(no prefix)* "Required change … Must address before merge", `Nit:`, `Optional:` / `Consider:`, `FYI` (ext :183-189); "Flag any issues as Critical, Required, Optional, or Nit." (ext :230) |
| action `auto-fix` / `no-op` / `ask-user` (no-mistakes 203548-203551) | "Author may ignore" (Nit), "No action needed" (FYI), "Ask before deleting" (ext :187-189, :239); verdict `Approve` / `Request changes` / "LGTM" (ext :275, :348-349) |
| status `working` / `needs-decision` / `blocked` / `paused` / `done` / `failed` (`bin/fm-classify-lib.sh:176`; `AGENTS.md:331-332`) | "Blocks merge" (ext :186), "Presumptive blockers" and "escalate to Required" (ext :398), "After review is complete" (ext :389), "explicitly deferred with justification" (ext :392) |

If any of this vocabulary reaches a worker's status line or a no-mistakes finding, it would be foreign to firstmate's classifier and to the escalation translation rules (`AGENTS.md:331-332`).

### Safety findings

- There is no injection text addressed to a reviewer, scanner or assistant. `grep` for `ignore (previous|all)|system prompt|<!--` returned nothing. Every hit on `reviewer` is ordinary prose (ext :18, :24, :122, :126, :128, :266).
- No zero-width or bidi characters were found (the Unicode-range `grep` returned rc=1). The only non-ASCII characters are 29 `—`, 4 `→`, 3 `│` and 3 `▼` (box-drawing in the diagram at ext :211-221).
- There are no base64 blobs, secrets, remote fetch-and-execute commands, scripts or binaries. The size-to-purpose ratio is normal (52.7 bytes per line).
- One file-modifying instruction: ext :164 tells the reviewer to mutate source, run the suite and restore from a copy. A read-only scout would break its read-only contract by following it, and a no-mistakes reviewer would break 203534.

### Trigger analysis

- Exact description: "Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. Use when asked to review a diff or a pull request, even when the diff is pasted inline." (ext SKILL.md:3)
- Broad phrases: `any change` and `before merging` (flagged by the surface tool). Also unflagged but broad: "code written by yourself" (every coding task), "before it enters the main branch", and "even when the diff is pasted inline".
- Same-topic installed descriptions: `no-mistakes` (user-agents and user-claude), `review-agent` (user-codex), `validation-supervision` (firstmate, "when a ship starts or already has an active no-mistakes validation run"), and `captain-hold-lifecycle` (firstmate, "structured review … as complete").
- Model invocation: the default is on (`auto`, no `disable-model-invocation`). At any shared placement it would fire on essentially every ship.

## 6. Fit and cost

- **Stack:** the examples are JS/npm web (`npm audit`, `package.json`, XSS, re-renders, pagination; ext :73, :84-85, :289, :299). Firstmate's own repo is shell/Python. Project stacks are unknown, because the registry could not be read in this home.
- **Human-in-the-loop assumptions:** the skill assumes humans in the loop throughout. It has authors and reviewers in dialogue (ext :279), a one-business-day response (ext :255), asking before deleting (ext :239), a human final call (ext :221) and bug self-assignment (ext :269). Each one contradicts autonomous workers that report only to firstmate (`AGENTS.md:39-40`).
- **Tool availability (`which`):**
  - Available: `npm` at `/home/hugo/.local/share/mise/installs/node/26.7.0/bin/npm`, `git` at `/usr/bin/git`, `no-mistakes` at `/home/hugo/.local/bin/no-mistakes` (v1.84.0, 4822244), `pi`, `gh-axi`.
  - Missing: the referenced sibling skills and `references/` files.
- **Context cost per load:** about 80 tokens of description in every session's skill listing at any shared placement, plus about 5.2k tokens of body each time it triggers. Given the trigger, that would be nearly every coding turn.
- **Which workers load it where:**
  - Trial-only (`pi --skill`): only that one session.
  - One project's `.agents/skills`: firstmate and Pi workers on that project. Inferred: the no-mistakes reviewer agent running in that project's run worktree could also pick it up, which would bring Critical/Nit/Approve vocabulary into the reviewer.
  - User-global `~/.agents/skills` plus the `~/.claude/skills` symlink: every Pi and Claude session on the machine, including firstmate, every crewmate and secondmate, and (inferred) no-mistakes reviewer agents. Codex reads `~/.codex/skills` and already has `review-agent`.
  - Firstmate's `.agents/skills`: firstmate and every firstmate-repo worker.
  - The placements that could reach the no-mistakes reviewer are not verified (section 9).

## 7. Recommendation

`harvest`. Do not install the skill at any placement. Re-derive two pieces in firstmate's own words, credit "addyosmani/agent-skills `skills/code-review-and-quality` (MIT)" in the commit message of whichever change carries them, and copy no text.

1. **Dependency-change review rule.** Target: the chosen project's `.no-mistakes.yaml` `review.path_instructions` entry. That is a supported no-mistakes repo setting (validation strings at nm 201494, 201518, 201537, 201557, 201647, 201686; source file `internal/pipeline/steps/review_path_instructions.go`, nm 234351).
   - It is delivered by a normal ship on that project, by a worker, never by firstmate writing to the project (`AGENTS.md:28`).
   - The path globs cover that project's manifest and lockfile (for example `package.json`, `package-lock.json`).
   - One-sentence rewrite: "When this change bumps a dependency, cite the release notes for each bumped package, report as `ask-user` any bump that bundles unrelated packages, review the transitive lockfile changes as well as the direct ones, and report a lockfile entry that does not match what the package manager would generate."
   - It must use only no-mistakes' own severity and action labels.
2. **Mutation-probe idea for the no-mistakes test step.** Target: a local issue draft for the no-mistakes maintainer, kept in this home's private records. It is not opened anywhere on firstmate's own authority (`AGENTS.md:50`).
   - One-sentence rewrite: "In the test step (not review), for one condition the change adds, check whether inverting it would leave the suite green, and if so report the missing test case under the existing missing-test rule."
   - The tool-owned prompt is never edited or replaced from here.

**Must not come along:**
- the "every change reviewed before merge" trigger and gate (ext :3, :10, :16-20)
- the Approve/Request-changes verdict and the human-final-call pattern (ext :207-231, :347-349)
- the Critical/Required/Nit/Optional/FYI labels (ext :179-191)
- ask-before-deleting (ext :239)
- running or mutating tests inside review (ext :164 as written)
- duplication and file-size presumptive blockers (ext :57, :113, :398)
- the no-deferral and bug self-assignment rules (ext :269)
- review-speed and team-process material (ext :103-128, :251-258)

## 8. Captain's decision

- **A (recommended):** harvest piece 1 only. Name the npm-based project that should get the dependency-change review rule, and a normal ship adds it to that project's no-mistakes config.
- **B:** harvest pieces 1 and 2. Same as A, plus a private draft suggestion to the no-mistakes maintainer about the mutation probe.
- **C:** decline outright as conflicting with how reviews and merges already work. Nothing is added anywhere.

## 9. Evidence

### Pinned file list (local folder, no git repository)

```
$ find …/input -type f -exec sha256sum {} \;
c2575f0c97ba17f3b6e0c29c6c52530ff2abe5ed0f71fe591da5b45b8ee5ec88  input/review-conflicting/SOURCE
2db1e850379f255fd3091ef278cde24cd6c7d2ba23e360cc52ea522c40d4396e  input/review-conflicting/SKILL.md
6f202f8bd568cd730dbb2b0d1f8e243bc74c2fa1f64dbce9b2c7ea08bd5c9fd7  input/review-conflicting/LICENSE
$ file …            SOURCE: ASCII text | SKILL.md: Unicode text, UTF-8 text, with very long lines (433) | LICENSE: ASCII text
$ wc -lc …          SOURCE 10 l / 545 B | SKILL.md 398 l / 20976 B | LICENSE 21 l / 1068 B
$ ls -la            no dotfiles; directory holds exactly LICENSE, SKILL.md, SOURCE
$ git -C …/input/review-conflicting rev-parse HEAD
fatal: not a git repository (or any parent up to mount point /)
```

### Candidate surface row (verbatim)

```
$ python3 bin/fm-skill-surface.py --root candidate=/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/review-conflicting/input
scope	name	dir	description	model_invocation	lines	bytes	flags
candidate	code-review-and-quality	/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/review-conflicting/input/review-conflicting	Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. Use when asked to review a diff or a pull request, even when the diff is pasted inline.	auto	398	20976	name!=dir,broad-trigger:any change|before merging
```

### Live surface

`python3 bin/fm-skill-surface.py` (FM_HOME unset, so it used the code-root default roots):
- There is no entry named `code-review-and-quality` and no `same-content-as` flag on any row.
- The only reported name collision is the unrelated `skill-creator` (user-claude vs user-codex).
- Rows on the same topic: `user-agents no-mistakes`, `user-claude no-mistakes`, `user-codex review-agent` (57 lines, 2,661 B, `-`).

### References

```
$ ls …/review-conflicting/references …/references
ls: cannot access …: No such file or directory   (both)
$ find <all skill roots> -maxdepth 4 -name security-and-hardening|performance-optimization|constraint-driven-development
0 / 0 / 0
```

### Safety scans

- `grep -nP '[^\x00-\x7F]'`: only `—`×29, `→`×4, `│`×3, `▼`×3.
- Zero-width/bidi range `grep`: rc=1.
- Pattern scan for `<!--|base64-like runs|curl|wget|bash -c|eval|ignore previous|system prompt|api key|token|password|secret`: only benign prose hits (ext :18, :24, :69, :122, :126, :128, :266, :331) and the hash line ext SOURCE:8.

### Owner text

`strings "$(command -v no-mistakes)" > $TMP/nm.txt` (no-mistakes v1.84.0 (4822244), 4,798,541 bytes of strings output). The cited `nm` line numbers are lines of that output:
- review prompt: 203513-203570
- schema enums: 237978, 237982, 238036, 238040
- missing-test rule: 202277
- review-auto-fix note: 201732
- `review.path_instructions` validation: 201494, 201518, 201537, 201557, 201647, 201686
- source path: 234351

Firstmate files read at the cited lines: `AGENTS.md` (sections 1, 7, 9), `.agents/skills/ask-user-authority/SKILL.md`, `.agents/skills/validation-supervision/SKILL.md`, `.agents/skills/firstmate-coding-guidelines/SKILL.md`, `bin/fm-classify-lib.sh:170-180`, `/home/hugo/.codex/skills/.system/review-agent/SKILL.md`.

### Empty searches

```
$ grep -rniE 'lockfile|changelog|semver|mutation test|invert one condition' AGENTS.md .agents/skills/   -> (no output), rc=1
$ grep -noiE '.{0,80}(changelog|semver).{0,120}' nm.txt   -> only Go symbols internal/update.semVersion.compare
$ grep -noiE '.{0,100}(invert (one|a) condition|mutation (score|test)|mutant).{0,100}' nm.txt   -> (no output)
```

### Not verified, and why

- **Upstream provenance** (repo, commit `28f435e…`, blob `08209ff…`): not fetched, because the instruction says the local folder is the pinned copy. The claim rests only on ext SOURCE:4-7, though the recorded sha256 matches.
- **`curl -sI` on `https://github.com/addyosmani/agent-skills`** (ext SOURCE:4): not run, because the instruction says to fetch nothing. `SKILL.md` itself contains no URLs.
- **Exact `.no-mistakes.yaml` YAML shape for `review.path_instructions`:** inferred from validation strings (`path` glob, `instructions`, entry-count and byte budgets). Also, `trusted repo config: not present on default branch` (nm 201494) suggests the rule takes effect only after it lands on the default branch. The setting's help or docs were not read.
- **Whether no-mistakes reviewer agents load project or user-global skills in their run worktrees:** inferred, not tested. A trial would be its own task.
- **Project stacks and registry:** not readable in this home. This is the fact that decides between `harvest` and `decline (conflict)`.
- **Codex loading `~/.agents/skills`:** not verified.
- **`captain-hold-lifecycle` completion gate:** I did not run `bin/fm-captain-hold.sh hold` or `complete`, because this run was confined to writing only this report. The one captain decision in section 8 (A/B/C) is still open. Firstmate must hold it in the supervising home's backlog with `--origin` set to this analysis, then run `complete` with that task id before treating this analysis as complete.
- **Scratch files:** written only under the temporary directory `/tmp/fmsa-r5/tmp.9XDPo3if2w/` (`nm.txt`).

done: harvest (dependency-change review rule into one project's no-mistakes config; mutation-probe idea as a maintainer note); everything else stays out as conflicting.
