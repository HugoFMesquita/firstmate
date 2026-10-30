# Skill analysis: good-standalone (local folder `input/good-standalone`)

## 1. Verdict

`adopt`. Start trial-only (`pi --skill <path>`). If the trial passes, install user-global at `~/.agents/skills/<new name>` with `~/.claude/skills` reaching it through the existing symlink pattern, set to `disable-model-invocation: true`, with the narrowed description in section 7. Confidence: **medium**.
The fact that would change it: the captain confirms there is no real need for calendar-file generation. In that case the verdict becomes `decline (unfit)`, because no project on this machine touches the topic (section 6).

## 2. What the skill is

- **Source:** local folder `/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/good-standalone/input/good-standalone`. It is not inside a git repository (`git -C <dir> rev-parse HEAD` returned `fatal: not a git repository`), so it is pinned by file hashes only:
  - `SKILL.md` sha256 `78ab59a6d6cd702ba3f2fdf553e1b396cfa64ac75b2cdc276dabf28207675eea`
  - `LICENSE` sha256 `feae8fcc8a231893c3ab30bf4ccdae185814964ac88a874dc6c69e29ec80689d`
- **License:** MIT, declared in two places: frontmatter `license: MIT` (ext SKILL.md:4) and the full text (ext LICENSE:1-21, "Copyright (c) 2026 skill-analyzer fixture authors", ext LICENSE:3). Copying and modification are allowed as long as the notice is kept (ext LICENSE:12-13).
- **Frontmatter:** `name: good-standalone` (ext SKILL.md:2) matches the directory name. There is a description (ext SKILL.md:3) and a license (ext SKILL.md:4). There is no `disable-model-invocation` field, so the skill is model-invocable by default. There are no non-spec fields.
- **Candidate `bin/fm-skill-surface.py` flags:** `-`. The row reads `candidate good-standalone … auto 35 1695 -` (section 9).
- **Size:**

  | File | Lines | Bytes | Approx. tokens |
  |---|---|---|---|
  | SKILL.md | 35 | 1695 | ~424 (bytes / 4) |
  | LICENSE | 21 | 1087 | – |

  The description is 193 bytes (~48 tokens). The longest line is 211 characters.
- **Every file:** the two files above, both `ASCII text` per `file`. There are no dotfiles, no subdirectories, no scripts, no binaries, no archives, no images, and no non-ASCII bytes (`grep -nP '[^\x00-\x7F]'` exited 1).
- **References:** there are no relative paths, `../` escapes, sibling-skill names, URLs, or tool names. The only external reference is the standard name "RFC 5545" (ext SKILL.md:3) and "the IANA database" (ext SKILL.md:14). Neither is a fetchable path, and both resolve as external standards, not files. The pattern search for `http|curl|wget|base64|\.\./` returned nothing (section 9).
- **Tools and stack assumed:** nothing is named. Converting a local time zone to UTC (ext SKILL.md:19) implies a time-zone-aware runtime. Writing a file with CRLF endings implies the agent's file-write tool or a script.
- **Intended audience:** a general assistant answering a user request ("Use when asked to create a calendar invite…", ext SKILL.md:3). The check step assumes a human with a text editor (ext SKILL.md:35).

**Capability inventory**

| # | ext file:line | Block | Imperative strength | Vocabulary introduced | Tools called | Audience |
|---|---|---|---|---|---|---|
| 1 | SKILL.md:2-3 | Trigger description | trigger ("Use when asked…") | iCalendar, `.ics`, calendar invite, event file | none | model router |
| 2 | SKILL.md:9 | Goal: standards-compliant `.ics`, imports "without warnings" | declarative | – | none | agent |
| 3 | SKILL.md:13-15 | Inputs: title, start, end or duration, optional IANA zone, location, description, attendee emails | declarative | IANA zone | none | agent |
| 4 | SKILL.md:19 | Convert start and end to UTC as `YYYYMMDDTHHMMSSZ` | imperative | – | implied time-zone conversion | agent |
| 5 | SKILL.md:20 | UID is `<random hex>@<sender domain>`, "never reuse" | imperative and prohibition | UID | none | agent |
| 6 | SKILL.md:21-22 | CRLF line endings, fixed property order | imperative | VCALENDAR/VEVENT property names | file write | agent |
| 7 | SKILL.md:23 | Escape `,` `;` `\`, newline as `\n` | imperative | – | none | agent |
| 8 | SKILL.md:24 | Fold lines over 75 octets with CRLF plus a space | imperative | octet folding | none | agent |
| 9 | SKILL.md:25 | One `ATTENDEE;CN=<name>:mailto:<address>` per attendee | imperative | ATTENDEE | none | agent |
| 10 | SKILL.md:29 | Floating times are read in the reader's local zone; prefer UTC | advisory | floating time | none | agent |
| 11 | SKILL.md:30 | Some clients reject LF-only files | advisory | – | none | agent |
| 12 | SKILL.md:31 | All-day event uses `VALUE=DATE` with an exclusive next-day `DTEND` | advisory | all-day | none | agent |
| 13 | SKILL.md:35 | Open in a text editor; confirm CRLF and no line over 75 octets | imperative | – | "text editor" (human) | human |

## 3. What firstmate already has on this topic

Nothing. No firstmate skill, user-global skill, or project skill owns calendar-file generation. The step-5 owner map (review, decisions, merging, memory, diagnosis, project onboarding) does not cover this topic, so the owner is **none**.

**Exact searches:**

- `grep -rniE 'icalendar|\.ics\b|rfc ?5545|vcalendar|calendar invite|VEVENT'` across firstmate `.agents/skills`, `skills`, `~/.agents/skills`, `~/.claude/skills`, `~/.codex/skills`, `~/.pi/agent/skills`, and `/home/hugo/firstmate/projects/*/.agents/skills` and `.claude/skills` returned exactly one line. That line is unrelated: `setup-writing-style/SKILL.md:79: - Skip obvious boilerplate: calendar invites, automated notifications, one-word replies.` It is about writing-style sampling, not generation.
- `grep -rliE 'calendar'` over the same skill roots found these files that mention calendars but do not generate `.ics`:
  - `user-claude morning` (SKILL.md:3, :20, :30) reads a connected calendar to render a morning brief. Its description already says "A question about their day, schedule, or calendar is not by itself a request for the brief" (morning/SKILL.md:3).
  - `user-codex openai-docs` (references/codex-self-knowledge.md:57) mentions using a connector for Calendar data.
  - The other hits are Office XML `.xsd` schemas, a reddit script, and a manifest in `user-claude` synced skills. None is about `.ics`.
- `bin/fm-skill-surface.py` (default roots, then again with `FM_HOME=/home/hugo/firstmate` for project scopes) shows no row named `good-standalone` and no `same-content-as` entry pointing at the candidate (section 9).

## 4. Overlap map

| External piece | Firstmate today | Class |
|---|---|---|
| ext SKILL.md:2-3 trigger (calendar invite / `.ics`) | Empty search (section 3). Nearest description is `morning` (morning/SKILL.md:3), which reads calendars and explicitly disclaims calendar questions. | new |
| ext SKILL.md:9 goal | Empty search (section 3) | new |
| ext SKILL.md:13-15 inputs | Empty search (section 3) | new |
| ext SKILL.md:19 UTC conversion | Empty search (section 3) | new |
| ext SKILL.md:20 UID rule | Empty search (section 3) | new |
| ext SKILL.md:21-22 CRLF and property order | Empty search (section 3) | new |
| ext SKILL.md:23 text escaping | Empty search (section 3) | new |
| ext SKILL.md:24 line folding | Empty search (section 3) | new |
| ext SKILL.md:25 attendees | Empty search (section 3) | new |
| ext SKILL.md:29-31 gotchas | Empty search (section 3) | new |
| ext SKILL.md:35 manual text-editor check | Empty search (section 3). It assumes a human, so for autonomous workers it needs a mechanized rewrite (section 7). | noise as written |

**Totals:** 0 `already-done`, 0 `clash`, 10 `new`, 1 `noise`.

## 5. Conflicts and safety

**Conflict table:** none.
The skill never mentions merging, PRs, projects, delivery, captain address, crewmates, or memory. None of the hard rules in `AGENTS.md:27-49` (never write to a project, never merge without the captain's word, never tear down unlanded work, crewmates never address the captain, report faithfully) or the delivery path in `AGENTS.md` section 7 (`AGENTS.md:165`) is touched. Only the external side would exist to quote, and there is no firstmate counterpart to quote against.

**Vocabulary collisions** against error/warning/info, auto-fix/no-op/ask-user, and working/needs-decision/blocked/paused/done/failed: one incidental word. ext SKILL.md:9 says "import without warnings". That refers to calendar-app import warnings, not a firstmate status or review label. No other hit (`grep -niwE 'error|warning|warnings|info|auto-fix|no-op|ask-user|working|needs-decision|blocked|paused|done|failed'` returned only line 9).

**Safety findings (observed):**

- No text is addressed to a reviewer, scanner, or assistant.
- No remote fetch or remote execution.
- No base64, secrets, URLs, or `../` escapes. The search `grep -niE 'http|curl|wget|base64|\.\./|reviewer|scanner|assistant|ignore (all|previous)|system prompt|token|password|secret|api[_-]?key'` over both files exited 1 with no output.
- No scripts, binaries, or non-ASCII bytes.
- The size ratio is sane: 1695 bytes over 35 lines for a single-format procedure.
- The `PRODID:-//example//ics generator//EN` value (ext SKILL.md:22) is a placeholder, not an identity or secret.

**Correctness observations.** These come from my knowledge of RFC 5545. The RFC text was not fetched in this run (section 9).

- Attendee lines are ordered badly. Step 3 fixes the line order ending in `END:VEVENT`, `END:VCALENDAR` (ext SKILL.md:22). Step 6 then adds `ATTENDEE` lines (ext SKILL.md:25) without saying they belong inside the VEVENT. Taken literally, an agent could append them after `END:VCALENDAR`.
- With attendees, the event is a group-scheduled entity, which needs an `ORGANIZER`. The skill never mentions it. An emailed "invite" (ext SKILL.md:3) normally also needs `METHOD:REQUEST` (RFC 5546). As written, the output is a calendar file, not a true scheduling invite.
- `DTSTAMP` appears in the order list (ext SKILL.md:22), but its value and format are never specified. It must be UTC.
- Folding at 75 octets (ext SKILL.md:24) is correct. It does not warn against splitting a multi-byte UTF-8 character.
- Values in the `CN` parameter (ext SKILL.md:25) that contain `,`, `;`, or `:` need double quotes. This is not mentioned.
- Input allows a duration instead of an end time (ext SKILL.md:13), but the output only writes `DTEND` (ext SKILL.md:22). This is fine if the agent computes the end, but it is implicit.
- The rest is accurate: escaping (ext SKILL.md:23), floating times (ext SKILL.md:29), and all-day exclusive `DTEND` (ext SKILL.md:31).

**Trigger analysis:**

- **Exact description:** "Generate RFC 5545 iCalendar (.ics) files for meetings and reminders. Use when asked to create a calendar invite, an event file, or an .ics attachment from a date, time, and title." (ext SKILL.md:3)
- **Broad phrases:** none. The search `grep -niE 'any change|before merging|always|any task|whenever|every time|all code'` exited 1, and `fm-skill-surface.py` raised no `broad-trigger` flag.
- **Same-topic installed descriptions:** `morning` only ("…A question about their day, schedule, or calendar is not by itself a request for the brief…", morning/SKILL.md:3). It does not compete for "create an .ics" requests.
- **Model-invocation default:** `auto`, because there is no `disable-model-invocation`. Adoption must add `disable-model-invocation: true` (decision rules).

## 6. Fit and cost

- **Stack:** the skill is stack-agnostic, a plain-text file format. No captain project touches the topic. `grep -rliE 'icalendar|\.ics\b|calendar|vevent'` over `/home/hugo/firstmate/projects/{fm-sandbox,knoliver,OllieCrew}` (excluding `.git` and `node_modules`) returned nothing. The candidate is a personal utility, not project work.
- **Human-in-loop assumptions:** only ext SKILL.md:35 ("Open the file in a text editor"). An autonomous worker cannot do this, and a text editor does not reliably show CRLF anyway. The step needs a mechanized check (section 7).
- **Tool availability:**
  - `which python3` → `/usr/bin/python3` (3.14.7, `zoneinfo` resolves `Europe/Paris`).
  - `which date` → `/usr/bin/date`.
  - `which zdump` → `/usr/bin/zdump`.
  - `/usr/share/zoneinfo/Europe/Paris` exists.
  - The `icalendar` Python package is **not** installed (`ModuleNotFoundError`). Validation would have to be a small stdlib check, not that library.
- **Context cost per load:**
  - When invoked, the body is ~424 tokens (1695 bytes).
  - While `auto`, the always-loaded trigger index pays ~48 tokens (193-byte description) in every session of every runtime that discovers the folder.
  - With `disable-model-invocation: true`, Pi hides it from automatic model selection (Pi docs `docs/skills.md:53`, `:79`), so the standing cost is at most the explicit-command listing.
- **Which workers load it, by placement:**
  - **Trial-only:** only the single `pi --skill <path>` session.
  - **One project's `.agents/skills`:** workers whose working directory is inside that project. Pi discovers `.agents/skills` up to the repo root (Pi docs `docs/skills.md:61`). No project fits this topic.
  - **User-global `~/.agents/skills` plus `~/.claude/skills`:** every Pi session (Pi docs `docs/skills.md:61`). Also Devin (`harness-adapters/references/harness/devin.md:14`), Command Code (`commandcode.md:15`), and, through `~/.claude/skills`, Claude Code and Cortex (`cortex.md:16`). This includes every firstmate crewmate on those runtimes, which is why explicit-only matters here.
  - **Firstmate's own `.agents/skills`:** not appropriate, because the behavior is not firstmate-specific (placement rule).

## 7. Recommendation

**adopt**: a new topic with no owner, no clash, a trigger that is already narrow, and a cost of ~424 tokens on explicit load.

**Placement:**

1. Trial-only first: `pi --skill <scratch copy>`.
2. On pass, user-global at `~/.agents/skills/ics-file/` (directory renamed from the fixture name `good-standalone`), with `LICENSE` kept beside it per ext LICENSE:12-13.
3. Firstmate's own `.agents/skills` is not a candidate.

**Narrowed description:**

> Write a single-event RFC 5545 iCalendar (.ics) file from a title, start, and end or duration. Use only when explicitly asked for an .ics file or calendar-invite attachment.

Add `disable-model-invocation: true`.

**Pre-install edits to the copy.** These are small, and the trial should test them:

1. State that the `ATTENDEE` lines (ext SKILL.md:25) and `ORGANIZER;CN=<name>:mailto:<address>` go inside the VEVENT, before `END:VEVENT`. `ORGANIZER` is required whenever there are attendees.
2. State that an emailed invite adds `METHOD:REQUEST` after `PRODID`. A plain file to import does not.
3. Specify `DTSTAMP` as the current UTC time in `YYYYMMDDTHHMMSSZ` form (fills the gap at ext SKILL.md:22).
4. Fold only between whole UTF-8 characters (extends ext SKILL.md:24), and double-quote `CN` values that contain `,`, `;`, or `:`.
5. Replace ext SKILL.md:35 with a mechanized check: a stdlib `python3` one-liner that asserts every line ends in `\r\n` and every physical line is ≤ 75 octets, run on the written file.
6. Replace the `PRODID` placeholder `-//example//ics generator//EN` with a neutral value of the captain's choice.

**Trial plan.** This is a separate, short, captain-approved task, not part of this analysis.

- **Input:** in a scratch directory, ask one Pi session with `--skill` for a 90-minute meeting in `Europe/Paris` with two attendees. The description should contain a comma, a semicolon, a newline, and a 120-character run.
- **Pass needs all of the following:**
  - CRLF on every line.
  - No physical line over 75 octets.
  - Correct UTC conversion, cross-checked with `zdump`.
  - `ATTENDEE` and `ORGANIZER` inside the VEVENT.
  - Escaped text.
  - No extra steering.
- **On fail:** delete the trial copy and decline.

## 8. Captain's decision

- **A (recommended):** approve a trial-only run of the edited copy, then install it user-global as explicit-only `ics-file` if it passes.
- **B:** install the edited copy user-global as explicit-only now, without a trial.
- **C:** decline as unfit, because there is no calendar-file need on this machine.

## 9. Evidence

**Pinned file list** (`ls -la`, `file`, `sha256sum`, `wc -lc` on the folder):

```
-rw-r--r-- 1 hugo hugo 1087 Oct 30 12:52 LICENSE
-rw-r--r-- 1 hugo hugo 1695 Oct 30 12:52 SKILL.md
LICENSE:  ASCII text
SKILL.md: ASCII text
feae8fcc8a231893c3ab30bf4ccdae185814964ac88a874dc6c69e29ec80689d  LICENSE
78ab59a6d6cd702ba3f2fdf553e1b396cfa64ac75b2cdc276dabf28207675eea  SKILL.md
  21 1087 LICENSE
  35 1695 SKILL.md
```

`git -C <folder> rev-parse HEAD`:

```
fatal: not a git repository (or any parent up to mount point /)
```

**Candidate surface row:**

```
$ python3 bin/fm-skill-surface.py --root candidate=/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/good-standalone/input
scope	name	dir	description	model_invocation	lines	bytes	flags
candidate	good-standalone	/tmp/fmsa-r5/fm-skill-analyzer-live.xERmiz/good-standalone/input/good-standalone	Generate RFC 5545 iCalendar (.ics) files for meetings and reminders. Use when asked to create a calendar invite, an event file, or an .ics attachment from a date, time, and title.	auto	35	1695	-
```

**Live surface:**

- `python3 bin/fm-skill-surface.py` (firstmate worktree at `f28b2e8e19a20fea0339e23452f637c9226070b7`, `FM_HOME` unset) listed:
  - 29 `firstmate` skills
  - `user-agents`: bro, diagnose-crash, grilling, no-mistakes, omarchy, reverse-engineer-anything
  - `user-claude`: no-mistakes (`same-content-as:user-agents`) plus synced docs, docx, google-workspace, import-memory, last30days, morning, pdf, pptx, setup-writing-style, skill-creator, xlsx
  - `user-codex`: imagegen, openai-docs, plugin-creator, review-agent, skill-creator, skill-installer
- `FM_HOME=/home/hugo/firstmate python3 bin/fm-skill-surface.py` added `project:OllieCrew` rows, all `same-content-as:firstmate` except `agent-skill-trigger-index`.
- In both runs: no `good-standalone` name, no candidate content match.
- The pre-existing name collisions are unrelated: `skill-creator` (user-claude vs user-codex) and `agent-skill-trigger-index` (firstmate vs project:OllieCrew).

**Searches** (all quoted in sections 3 to 6):

- Topic search: one unrelated hit (`setup-writing-style/SKILL.md:79`).
- Project search: empty.
- Vocabulary search: only ext SKILL.md:9.
- Broad-phrase search: exit 1.
- Safety search: exit 1.
- Non-ASCII search: exit 1.

**Tools:**

- `which python3 date zdump` → `/usr/bin/python3`, `/usr/bin/date`, `/usr/bin/zdump`
- `python3 -c 'import icalendar'` → `ModuleNotFoundError`
- `which pi claude codex` → all present under mise

**Owner reads:** `AGENTS.md:27-49` (hard rules), `AGENTS.md:165` (section 7 heading), `AGENTS.md:412-415` (section 13); `morning/SKILL.md:3,20,30`; harness reference rows at `devin.md:14`, `commandcode.md:15`, `cortex.md:16`; Pi `docs/skills.md:53,61,79`.

**Not verified, and why:**

- The RFC 5545 and RFC 5546 correctness notes in section 5 come from my own knowledge. The RFC text was not fetched, because the brief forbids fetching and the skill contains no URL to probe with `curl -sI`.
- No `.ics` file was generated or imported into any calendar client, because a trial is a separate captain-approved task.
- Whether `disable-model-invocation: true` removes the description from the always-loaded index on Claude Code, Devin, and Command Code (rather than only on Pi) was not checked.
- The skill was read as data only. Nothing was executed, installed, or followed.
