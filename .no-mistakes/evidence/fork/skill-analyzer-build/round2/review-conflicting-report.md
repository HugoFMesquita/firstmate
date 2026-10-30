# Skill analysis: code-review-and-quality (local folder `input/review-conflicting`, vendored from addyosmani/agent-skills `skills/code-review-and-quality`)

Citation keys used throughout:

- `ext <file>:<line>` - the skill under test, in `/tmp/fm-skill-analyzer-live.FRdgf9/review-conflicting/input/review-conflicting/`.
- `<path>:<line>` with no prefix - the firstmate repository at `/home/hugo/.no-mistakes/worktrees/3f83383b2e86/01M66J7TBMNGZSZPZQX5FC74XP` (HEAD `6b63be47c23a48d7aaa7f3048523ce9056a0e255`).
- `nm:<line>` - line number in the output of `strings -n 8 /home/hugo/.no-mistakes/bin/no-mistakes` for no-mistakes v1.84.0 (4822244), binary sha256 `41fb1c780ef5d204c318eca8fbe73a0a86ae576395b7ae2153e21aacefef0d53`.
  The embedded review prompt is nm:18143-18196 (extract sha256 `65cfbc72cd78875ebd6c1ea7905eb31b217c226660f0734f473cf5d5743e0ed3`).

## 1. Verdict

`harvest` - two numbered pieces (a mutation probe for test adequacy, and dependency-change review rules) go into named existing owners; the rest stays out because its trigger and gate model clash with firstmate's delivery path and merge authority and its labels clash with no-mistakes' finding vocabulary.
Placement: none for the skill itself (nothing is installed); pieces are re-derived into owners through normal ships.
Confidence: medium - the one fact that would change it is whether the mutation probe is judged worth carrying; if the captain declines both pieces, the same evidence settles `decline (conflict)`.

## 2. What the skill is

- Source: local folder `/tmp/fm-skill-analyzer-live.FRdgf9/review-conflicting/input/review-conflicting`, not a git repository (`git -C <dir> rev-parse HEAD` -> `fatal: not a git repository`), so it is pinned by file hashes only (section 9).
  The folder's `SOURCE` manifest claims upstream `https://github.com/addyosmani/agent-skills`, path `skills/code-review-and-quality/SKILL.md`, commit `28f435ea69a78531ec00779c7f3b78c64ce95896` (ext SOURCE:4-6).
  Locally verified: SKILL.md sha256 equals the manifest's (ext SOURCE:8), `git hash-object` equals the manifest's blob `08209ff2208d2883d48d945f7754c428b77f8d87` (ext SOURCE:7), and size equals the manifest's 398 lines / 20976 bytes (ext SOURCE:9).
  The upstream commit itself was not verified because the run forbids fetching.
- Name: `code-review-and-quality` (ext SKILL.md:2); the folder is named `review-conflicting`, so `name!=dir` (Pi and other runtimes key skills by name; this mismatch is flagged by `bin/fm-skill-surface.py`, section 9).
- Description (ext SKILL.md:3): present, 339 bytes, no `disable-model-invocation`, no `license` field, no non-spec fields; so it is model-invocable by default.
- License: MIT, `Copyright (c) 2025 Addy Osmani` (ext LICENSE:1-3), stated by the manifest to be the repository LICENSE (ext SOURCE:10); permits copying with notice, but harvest re-derives text anyway.
- Size: 398 lines, 20976 bytes, about 5,200 tokens per load (bytes / 4); 292 non-blank lines; longest line 433 bytes; about 53 bytes per line, ordinary for prose.
- Files (all three read in full):
  - `SKILL.md` - UTF-8 text, 20976 bytes.
  - `LICENSE` - ASCII text, 1068 bytes.
  - `SOURCE` - ASCII text, 545 bytes; fixture provenance, not part of the upstream skill (ext SOURCE:1).
  - No dotfiles, scripts, archives, bytecode, images, or binaries (`ls -la` and `file`, section 9).
- References and resolution:
  - `security-and-hardening` (ext SKILL.md:66, :302) - sibling skill name; not in the folder, not installed anywhere on this machine (empty surface search, section 9); would not travel.
  - `performance-optimization` (ext SKILL.md:79) - same: nowhere locally; would not travel.
  - `constraint-driven-development` (ext SKILL.md:164) - same: nowhere locally; would not travel.
  - `../../references/security-checklist.md`, `../../references/performance-checklist.md` (ext SKILL.md:353-354) - escape the folder into the source repository; not present locally; would not travel.
  - URLs: none in SKILL.md (`grep -n http` matched no SKILL.md line); the only URL is the manifest's repository URL (ext SOURCE:4), not probed because the run forbids fetching.
- Tools named: `npm audit` (ext SKILL.md:289, :302); the mutation probe implies running the project's test suite (ext SKILL.md:164).
- Stack assumed: web/JS application code - SQL, XSS, UI re-renders, pagination, `package.json`, lockfiles (ext SKILL.md:71-72, :83-84, :299-300).
- Intended audience: a human-supervised coding agent or human reviewer on a team with PRs, authors, and reviewers (ext SKILL.md:221, :239, :251-258, :279).

## 3. What firstmate already has on this topic

Topic: code review and merge gating; the owner is the no-mistakes review prompt plus `AGENTS.md` section 7.

- `AGENTS.md:229-233` - "The selected delivery path owns its own rigor. When no-mistakes is selected, no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI; otherwise follow the faster path without adding an independent reviewer."
- `AGENTS.md:33-34` - hard rule 2, never merge without the captain's explicit word; `AGENTS.md:240-246` - merge authority and `bin/fm-pr-merge.sh`.
- `AGENTS.md:236-238` - the three delivery paths, two of which (direct-PR, local-only) ship without the no-mistakes review.
- no-mistakes review prompt nm:18143-18196 - findings with severity `error|warning|info` (nm:18171), action `ask-user|auto-fix|no-op` (nm:18176-18180), a simplification pass (nm:18185-18189), and `risk_level` low/medium/high (nm:18190-18196; schema nm:47763).
- no-mistakes intent conformance clause nm:17064, test-quality rule nm:17148-17169, test-step rules nm:17960-17973, commit-subject generator nm:17139-17146.
- `.agents/skills/ask-user-authority/SKILL.md:13-35` - single owner of ask-user finding decisions.
- `.agents/skills/validation-supervision/SKILL.md:11-32` - supervising an active no-mistakes run; new requirements go to follow-up work (line 15).
- `.agents/skills/ship-landing/SKILL.md:11-20` - PR-ready signal, risk level relay, merge authority.
- `.agents/skills/firstmate-coding-guidelines/SKILL.md:113-133` - test configuration and test rules for firstmate's own repo.
- `.no-mistakes.yaml:15-49` - firstmate's own document and test instructions (the supported per-step settings).
- Installed same-topic skills: user-global `no-mistakes` (`~/.agents/skills/no-mistakes/SKILL.md:3`, also in `~/.claude/skills`, flagged `same-content-as:user-agents`) and Codex's system `review-agent` (`~/.codex/skills/.system/review-agent/SKILL.md:3`).
- No installed skill is named `code-review-and-quality` (surface search, section 9).

## 4. Overlap map

| # | External piece | Firstmate today | Class |
|---|---|---|---|
| 1 | Trigger and gate: "Use before merging any change" (ext SKILL.md:3), "Every change gets reviewed before merge — no exceptions" (ext SKILL.md:10), "Before merging any PR or change" (ext SKILL.md:16) | `AGENTS.md:229-233` the selected path owns rigor, no independent reviewer on the fast path, never stack serial manual reviews | clash |
| 2 | Approval standard: approve when it improves code health, do not block on preference (ext SKILL.md:12) | nm:18162 "Do not expand user scope or turn optional broader improvements into blockers"; nm:18193 medium risk "safe to merge first with concerns addressed as follow-ups" | already-done |
| 3 | Correctness axis: spec match, edge cases, error paths, races (ext SKILL.md:26-34) | nm:18152-18155, nm:18166, intent conformance nm:17064 | already-done |
| 4 | Readability and simplicity: fewer lines, abstractions earning complexity, dead artifacts, bolted-on conditionals (ext SKILL.md:36-49) | nm:18164-18165 simplification as non-functional refactoring; nm:18185-18189 unrequired components; naming and comment style excluded by nm:18174 | already-done |
| 5 | Architecture axis: relocate-vs-reduce complexity, feature logic in shared modules, explicit type boundaries (ext SKILL.md:51-62) | nm:18160 "Do not infer a systemic flaw from code shape, duplication, or architectural preference alone. Do not demand a shared abstraction or broad redesign without a concrete reachable path" | clash |
| 6 | Security axis (ext SKILL.md:64-75) | nm:18156-18158 authorization and disclosure tracing; nm:18166 security issues as risks | already-done |
| 7 | Performance axis (ext SKILL.md:77-86) | nm:18166 "performance regressions" as risks | already-done |
| 8 | Structural remedies: propose the named move (ext SKILL.md:88-101) | nm:18159 recommend the earliest shared boundary; nm:18188 name removal as the smallest honest remedy | already-done |
| 9 | Change sizing 100/300/1000 lines, file-size boundary, split strategies (ext SKILL.md:103-128) | Scope is set at intake (`AGENTS.md:183-186`, `AGENTS.md:203-205`); review must not expand scope (nm:18162); `grep -rn -i -E 'file size\|1000 lines\|large file' AGENTS.md CONTRIBUTING.md .agents/skills .no-mistakes.yaml` returned no hit on this topic | noise |
| 10 | Change descriptions: imperative first line like "Delete the FizzBuzz RPC" (ext SKILL.md:130-138) | nm:17139-17146 generates conventional-commit subjects `type(scope): description`; PR title/body schema owned by no-mistakes | clash |
| 11 | Step 1 understand intent (ext SKILL.md:142-150) | nm:17064 intent is authoritative acceptance criteria; nm:18151-18153 | already-done |
| 12 | Step 2 review tests first; "Would the tests catch a regression" (ext SKILL.md:152-162) | nm:17148-17169 test-quality rule, "the test should fail before the fix and pass after it" (nm:17168-17169) | already-done |
| 13 | Mutation probe: invert one added condition, run the suite, restore; a surviving mutation names the missing test (ext SKILL.md:164) | `grep -rn -i -E 'mutation (test\|score)\|invert (one\|a) condition' AGENTS.md CONTRIBUTING.md .agents/skills .no-mistakes.yaml <review-prompt extract>` returned nothing (exit 1); in the review step it would clash with nm:18163 "Do NOT run tests during review" | new |
| 14 | Step 3 five-axis walk per file (ext SKILL.md:166-177) | rows 3-7; nm:18167-18168 full pass and `reviewed_paths` coverage | already-done |
| 15 | Step 4 severity labels Critical / no-prefix Required / Nit / Optional / Consider / FYI (ext SKILL.md:179-189, :230) | nm:18171 `error\|warning\|info`; nm:18176-18179 `ask-user\|auto-fix\|no-op`; nm:18174 no style findings | clash |
| 16 | Lead with what matters, a few high-conviction comments (ext SKILL.md:193) | nm:18172-18173 concise, only what genuinely matters; nm:18167 enumerate all material issues | already-done |
| 17 | Step 5 verify the verification: tests run, build, screenshots, before/after (ext SKILL.md:195-205) | no-mistakes test step `tested`, `artifacts`, `scenarios` schema (nm:47797-47813) and rules nm:17960-17973 | already-done |
| 18 | Multi-model review pattern, "Human makes the final call" (ext SKILL.md:207-231) | `AGENTS.md:230-232` no stacked manual reviews; no-mistakes `review_agents` setting (nm:13271); hard rule 2 `AGENTS.md:33` | clash |
| 19 | Dead code hygiene: list orphans and "Ask before deleting" (ext SKILL.md:233-249) | nm:18164-18165 dedup simplification; nm:18177 deletions route to ask-user; `AGENTS.md:39-40` workers never address the captain; `grep -rn -i -E 'dead code\|unused (code\|element\|symbol)' ...` returned nothing | clash |
| 20 | Review speed, one business day (ext SKILL.md:251-258) | `grep -rn -i -E 'business day\|review speed' ...` returned nothing; no human review queue exists | noise |
| 21 | Disagreement hierarchy; "Don't accept 'I'll clean it up later'... Require cleanup before submission" (ext SKILL.md:260-269) | nm:18171 "warning ... can be done in a follow up"; `.agents/skills/validation-supervision/SKILL.md:15` route new requirements to follow-up; `.agents/skills/ask-user-authority/SKILL.md:30-35` | clash |
| 22 | Honesty: no rubber-stamp, quantify, push back, accept override (ext SKILL.md:271-279) | nm:18167, nm:18170; `AGENTS.md:344-346` evidence-first objections; `.agents/skills/ask-user-authority/SKILL.md:35` labels are evidence | already-done |
| 23 | Before adding a dependency: existing stack, size, maintenance, vulnerabilities, license (ext SKILL.md:281-292) | nm:18185-18187 flags unrequired components only; `grep -rn -i -E 'lockfile\|changelog\|bump' ...` returned nothing | new |
| 24 | Upgrading a dependency: read the changelog, one package per change, green before and after, review the lockfile diff, never hand-edit it (ext SKILL.md:294-302) | same empty search as row 23 | new |
| 25 | Review checklist ending in "Approve — Ready to merge" / "Request changes" (ext SKILL.md:304-350) | nm:47763 `risk_level` enum; `.agents/skills/ship-landing/SKILL.md:19-20` relay risk level, merge authority stays with the captain or `yolo` | clash |
| 26 | See Also links to `../../references/*.md` (ext SKILL.md:351-354) | targets do not exist locally and would not travel | noise |
| 27 | Common rationalizations table (ext SKILL.md:356-368) | restates rows 3-24 | noise |
| 28 | Red flag "PRs merged without any review" (ext SKILL.md:372) | `AGENTS.md:237-238` direct-PR and local-only legitimately merge without the no-mistakes review | clash |
| 29 | Presumptive blockers: escalate structural regressions to Required (ext SKILL.md:398) | nm:18160 no architectural-preference findings; `.agents/skills/ask-user-authority/SKILL.md:31` a Fix adding abstraction or broader architecture escalates rather than being demanded | clash |

Tally: 12 already-done, 10 clash, 3 new, 4 noise out of 29 rows; already-done is 41%, below the four-in-five duplicate bar.

## 5. Conflicts and safety

### Conflict table

| Topic | External text | Firstmate text |
|---|---|---|
| Who reviews and when (delivery path) | "Every change gets reviewed before merge — no exceptions." (ext SKILL.md:10) | "When no-mistakes is selected, no-mistakes alone owns review, fixes, tests, documentation, push, PR, and CI; otherwise follow the faster path without adding an independent reviewer." (`AGENTS.md:230`); "Never hold work outside no-mistakes for a manual clean verdict, stack serial manual reviews, or infer authority for one from security, architecture, or risk alone." (`AGENTS.md:231`) |
| Unreviewed merges | "PRs merged without any review" listed as a red flag (ext SKILL.md:372) | "**direct-PR** has the worker push and open a PR without the no-mistakes pipeline" (`AGENTS.md:237`) |
| Second reviewer | "Model B reviews for correctness and architecture ... Human makes the final call" (ext SKILL.md:215-221) | "A separate review or audit is allowed only when the captain explicitly requests that deliverable" (`AGENTS.md:232`) |
| Merge verdict | "**Approve** — Ready to merge" / "**Request changes**" (ext SKILL.md:348-349) | "Never merge a PR without the captain's explicit word." (`AGENTS.md:33`); `risk_level` low/medium/high (nm:18192-18194) |
| Severity vocabulary | "*(no prefix)* Required change ... **Critical:** Blocks merge ... **Nit:** ... **Optional:** / **Consider:** ... **FYI**" (ext SKILL.md:185-189) | "Use severity \"error\" for problems that should absolutely not get merged, \"warning\" for things that are worth addressing but can be done in a follow up, and \"info\" for things that are nice to have." (nm:18171) |
| Style findings | "**Nit:** Minor, optional ... formatting, style preferences" (ext SKILL.md:187) | "Do NOT report styling, formatting, linting, compilation, or type-checking issues." (nm:18174) |
| Architecture preference | "escalate to Required only when the change actively makes structure worse: a refactor that relocates complexity instead of reducing it; a change that pushes a file past the size boundary ..." (ext SKILL.md:398) | "Do not infer a systemic flaw from code shape, duplication, or architectural preference alone. Do not demand a shared abstraction or broad redesign without a concrete reachable path, violated invariant, or immediately competing semantic owner." (nm:18160) |
| Running tests in review | "Invert one condition the change adds ... run the suite, then restore the file from a copy." (ext SKILL.md:164) | "Do NOT run tests during review. The pipeline has a dedicated test step after review." (nm:18163) |
| Deferred cleanup | "Require cleanup before submission unless it's a genuine emergency." (ext SKILL.md:269) | "\"warning\" for things that are worth addressing but can be done in a follow up" (nm:18171); "prefer routing new requirements to follow-up work rather than expanding the current task" (`.agents/skills/validation-supervision/SKILL.md:15`) |
| Asking a human | "**Ask before deleting:** \"Should I remove these now-unused elements: [list]?\"" (ext SKILL.md:239) | "Crewmates never address the captain. All crewmate communication flows through firstmate." (`AGENTS.md:39-40`); ask-user decisions are owned by `.agents/skills/ask-user-authority/SKILL.md:13-19` |
| Commit message form | "\"Delete the FizzBuzz RPC\" not \"Deleting the FizzBuzz RPC.\"" (ext SKILL.md:134) | "Use conventional commit format: \"type(scope): description\"" (nm:17142) |

### Vocabulary collisions

- Against `error` / `warning` / `info`: Critical, Required (no prefix), Nit, Optional, Consider, FYI (ext SKILL.md:183-189, :230, :391-392).
- Against `auto-fix` / `no-op` / `ask-user`: "Must address before merge" (ext SKILL.md:185), "Author may ignore" (ext SKILL.md:187), "No action needed" (ext SKILL.md:189, near `no-op` but with a different owner), "Ask before deleting" (ext SKILL.md:239), "escalate to Required" (ext SKILL.md:398).
- Against `working` / `needs-decision` / `blocked` / `paused` / `done` / `failed` (`AGENTS.md:331-332`, `bin/fm-brief.sh:117-119`): "Blocks merge" (ext SKILL.md:186), "Presumptive blockers" (ext SKILL.md:398), "Approve — Ready to merge" / "Request changes" (ext SKILL.md:348-349), "LGTM" (ext SKILL.md:275, :374).

### Safety findings

- No scripts, archives, bytecode, images, or binaries (section 9 listing).
- No remote fetch-and-execute: no URL, `curl`, `wget`, or shell pipe in SKILL.md.
- No base64-like blob (`grep -n -E '[A-Za-z0-9+/]{60,}'` empty), no secret patterns (the only `secret` hits are review checklist items at ext SKILL.md:69 and :331).
- No zero-width or bidirectional-control characters (`grep -n -P '[\x{200B}-\x{200F}\x{202A}-\x{202E}\x{2060}-\x{2064}\x{FEFF}]'` empty); the 39 non-ASCII lines hold em dashes, arrows, and box-drawing characters.
- Text addressed to a review agent, copied verbatim (ext SKILL.md:228-230): "Review this code change for correctness, security, and adherence to / our project conventions. The spec says [X]. The change should [Y]. / Flag any issues as Critical, Required, Optional, or Nit."
  This is observed to be an example prompt template for the user's own reviewer, not an instruction aimed at an analyzer or scanner; it is not an injection, but it is exactly the foreign vocabulary in the conflict table and must not come along.
- Text addressed to the analyzer, copied verbatim (ext SOURCE:2): "The directory name differs from the skill's own name on purpose; the analyzer must flag it."
  It is in the fixture's provenance manifest, not the upstream skill (ext SOURCE:1); it asks for nothing beyond what `bin/fm-skill-surface.py` reported on its own (`name!=dir`), and it was not acted on as an instruction.
  It does not change the verdict.
- Unresolved references (section 2) are a portability defect, not a safety defect.

### Trigger analysis

- Exact description (ext SKILL.md:3): "Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. Use when asked to review a diff or a pull request, even when the diff is pasted inline."
- Broad phrases: `any change` and `before merging` (both flagged by `bin/fm-skill-surface.py` as `broad-trigger:any change|before merging`); "code written by yourself" also fires on every ship worker's own diff.
- Same-topic installed descriptions: user-global `no-mistakes` ("Validate your code changes through the no-mistakes pipeline - automated code review, tests, lint, docs, push, PR, and CI - before they reach the configured push target ...") and Codex `review-agent` ("Perform a read-only, defect-first review of a specified code change and return every actionable finding ...").
  "before merging any change" competes directly with `no-mistakes`' "before they reach the configured push target".
- Model-invocation default: auto (no `disable-model-invocation`), so at any shared placement it would load in every ship worker before its PR and, inferred, inside no-mistakes review agents running on a harness that reads user-global skills; `.no-mistakes.yaml:3-10` disables project-level settings for gate agents, not user-global skills (unverified, section 9).

## 6. Fit and cost

- Stack: generic but web/JS-leaning (SQL, XSS, re-renders, `npm audit`, lockfiles; ext SKILL.md:71-72, :84, :289, :299-300).
  Firstmate itself is bash and Markdown (`bin/*.sh`, `.agents/skills/firstmate-coding-guidelines/SKILL.md:125`), with one tracked manifest, `.opencode/plugins/package.json` (`git ls-files` search, section 9).
- Human-in-the-loop assumptions: "Ask before deleting" (ext SKILL.md:239), "Human makes the final call" (ext SKILL.md:221), "Respond within one business day" (ext SKILL.md:255), "Ask the author to split them" (ext SKILL.md:258), "Accept override gracefully" (ext SKILL.md:279), manual testing and screenshots (ext SKILL.md:200-203).
  Firstmate workers are autonomous and never address the captain (`AGENTS.md:39-40`).
- Tool availability: `which npm` -> `/home/hugo/.local/share/mise/installs/node/26.7.0/bin/npm` (present); `which no-mistakes` -> `/home/hugo/.local/bin/no-mistakes` (present, v1.84.0).
- Context cost per load: about 5,200 tokens body plus about 85 tokens of always-listed description at auto invocation.
- Which workers load it at each placement:
  - Trial-only: only the one session started with `pi --skill <path>` or briefed to read the path.
  - One project's `.agents/skills`: every worker in that project's isolated copies whose runtime reads project skills; no-mistakes gate agents there too unless that project sets `disable_project_settings`.
  - User-global `~/.agents/skills` plus `~/.claude/skills`: every runtime that reads those roots, for example Command Code (`.agents/skills/harness-adapters/references/harness/commandcode.md:15`), Devin (`.../devin.md:14`), Gemini (`.../gemini.md:99-100`), Cortex (`.../cortex.md:16`), and Claude; inferred to include no-mistakes review agents on those runtimes.
  - Firstmate's own `.agents/skills`: the supervisor and every firstmate-repo worker; unfit, because this is not firstmate-specific behavior.

## 7. Recommendation

Harvest these two pieces by re-deriving the idea in firstmate's words; copy no text.

1. Mutation probe for test adequacy (from ext SKILL.md:164) -> `.agents/skills/firstmate-coding-guidelines/SKILL.md` "Repo style rules" test bullets (lines 129-130), with a one-line pointer added to `.no-mistakes.yaml` `test.instructions` (lines 41-49), so it runs in the test step and never in review (nm:18163).
   Rewrite: "For each new or changed condition a change adds, invert it once in place, run only the targeted test for that behavior, then restore the file and confirm `git diff --quiet` on it; a mutation that still passes is a finding naming the missing test case."
2. Dependency-change review (from ext SKILL.md:281-302) -> the no-mistakes `review.path_instructions` setting (nm:14127, nm:16515) in the `.no-mistakes.yaml` of a project the captain names that has package manifests, through that project's normal ship; it is the tool's supported setting, so the tool's prompt is not replaced.
   Rewrite: "For a changed manifest or lockfile, check the changelog or migration notes of each bumped package, prefer one package per change, review the full lockfile diff for transitive changes, and flag a hand-edited lockfile or a new dependency the existing stack already covers."

These must not come along: the trigger and "no exceptions" gate (rows 1, 28), the second-model reviewer and human final call (row 18), Approve/Request changes verdicts (row 25), the Critical/Required/Nit/Optional/FYI labels (row 15), architecture-preference blockers (rows 5, 29), require-cleanup-before-merge (row 21), ask-before-deleting (row 19), the commit-subject style (row 10), and the review-speed, change-sizing, and broken See Also material (rows 9, 20, 26).
Credit "addyosmani/agent-skills, MIT" in each commit message.
Each piece is a separate ship and needs no trial.

## 8. Captain's decision

- A. Harvest piece 1 only (mutation probe into firstmate's coding guideline and test-step instructions). Recommended: it is the one idea with no current owner text and it fits firstmate's own tests.
- B. Harvest pieces 1 and 2, naming the project with package manifests whose review settings should get piece 2.
- C. Take nothing; the verdict becomes `decline (conflict)`.

Recommended: A.

## 9. Evidence

### Pinned file list

```
/tmp/fm-skill-analyzer-live.FRdgf9/review-conflicting/input/review-conflicting/LICENSE: ASCII text
  21 1068  sha256 6f202f8bd568cd730dbb2b0d1f8e243bc74c2fa1f64dbce9b2c7ea08bd5c9fd7
/tmp/fm-skill-analyzer-live.FRdgf9/review-conflicting/input/review-conflicting/SKILL.md: Unicode text, UTF-8 text, with very long lines (433)
  398 20976 sha256 2db1e850379f255fd3091ef278cde24cd6c7d2ba23e360cc52ea522c40d4396e
  git hash-object 08209ff2208d2883d48d945f7754c428b77f8d87
/tmp/fm-skill-analyzer-live.FRdgf9/review-conflicting/input/review-conflicting/SOURCE: ASCII text
  10 545   sha256 c2575f0c97ba17f3b6e0c29c6c52530ff2abe5ed0f71fe591da5b45b8ee5ec88
```

`ls -la` of the folder listed exactly `LICENSE`, `SKILL.md`, and `SOURCE`, with no dotfiles.
`git -C <folder> rev-parse HEAD` -> `fatal: not a git repository (or any parent up to mount point /)`.

### Commands and output

- `python3 bin/fm-skill-surface.py --root ext=/tmp/fm-skill-analyzer-live.FRdgf9/review-conflicting/input` ->
  `ext  code-review-and-quality  .../review-conflicting  <description>  auto  398  20976  name!=dir,broad-trigger:any change|before merging`
- `python3 bin/fm-skill-surface.py` (default roots, `FM_HOME` unset so the home is the code root) -> 53 skills; no `code-review-and-quality`; same-topic matches are `no-mistakes` (user-agents, plus a user-claude `same-content-as:user-agents` copy) and `review-agent` (user-codex); the only name collision is `skill-creator` (unrelated).
- `python3 bin/fm-skill-surface.py | awk -F'\t' '$2 ~ /security-and-hardening|performance-optimization|constraint-driven-development|code-review/'` -> empty output.
- `strings -n 8 "$(command -v no-mistakes)"` to a temporary file (74818 lines); review prompt read at nm:18143-18196, finding schemas at nm:47700-47830, test-quality rule at nm:17148-17169, commit-subject prompt at nm:17139-17146, test-step rules at nm:17960-17973, `review.path_instructions` at nm:14127 and nm:16515.
- `no-mistakes --version` -> `no-mistakes version v1.84.0 (4822244) 2026-09-26T08:30:42Z`.
- `grep -rn -i -E 'mutation (test|score)|invert (one|a) condition' AGENTS.md CONTRIBUTING.md .agents/skills .no-mistakes.yaml <review-prompt extract>` -> empty, exit 1.
- `grep -rn -i -E '<pattern>' AGENTS.md CONTRIBUTING.md .agents/skills .no-mistakes.yaml <review-prompt extract>` returned empty output for each of: `dead code|unused (code|element|symbol)`, `lockfile|changelog|bump`, `N\+1|pagination|re-render`, `sycophan|rubber.stamp|LGTM`, `business day|review speed`, `change description|first line of (the )?commit`.
- `git -C <firstmate> ls-files | grep -E -i '(package(-lock)?\.json|pnpm-lock|yarn\.lock|go\.(mod|sum)|requirements.*\.txt|Cargo\.(toml|lock)|pyproject|Gemfile)$'` -> `.opencode/plugins/package.json`.
- `which npm no-mistakes` -> both present (section 6).
- Owner files read at cited lines: `AGENTS.md` sections 1, 7, 9, 11; `.agents/skills/{firstmate-coding-guidelines,ship-landing,validation-supervision,ask-user-authority,captain-hold-lifecycle}/SKILL.md`; `.no-mistakes.yaml`; `docs/architecture.md:341-347`; `~/.agents/skills/no-mistakes/SKILL.md`; `~/.codex/skills/.system/review-agent/SKILL.md`.

### Not verified, and why

- Upstream commit `28f435ea...`, upstream LICENSE, and the existence of the sibling skills and `references/` files in the source repository: not checked because the run forbids fetching; the local hashes match the manifest's claims.
- Whether no-mistakes review agents load user-global skills at run time: inferred from the harness references and from `disable_project_settings` covering only project-level settings (`.no-mistakes.yaml:3-10`); not checked by a run because analysis forbids trials.
- Whether `review.path_instructions` applies when a project sets `disable_project_settings: true`: not determined from the strings; piece 2's target project should be checked before its ship.
- The `captain-hold-lifecycle` completion gate (`bin/fm-captain-hold.sh hold`/`complete`) was not run: this run has no task id or backlog home and may write only this report; the open decision in section 8 is the one item a supervisor would hold.
