# Skill analysis: good-standalone (local folder input/good-standalone)

## 1. Verdict

`adopt` - placement trial-only first (`pi --skill /tmp/fm-skill-analyzer-live.FRdgf9/good-standalone/input/good-standalone`), installed as `disable-model-invocation: true` with a narrowed description; confidence **medium**.
The one fact that would change it: if the captain has no recurring need for `.ics` files (no project, workflow, or request that produces calendar files), the verdict becomes `decline (unfit)`, because nothing on this machine's firstmate surface or visible projects calls for calendar output (section 3 searches).

## 2. What the skill is

- **Source:** local folder `/tmp/fm-skill-analyzer-live.FRdgf9/good-standalone/input/good-standalone`, already a pinned local copy. Nothing was fetched.
- **Pinned commit:** none. The folder is not inside a git repository (`git -C <folder> rev-parse HEAD` -> `fatal: not a git repository`), so the pin is the file hashes below and nothing else.
- **Pin (sha256):**
  - `78ab59a6d6cd702ba3f2fdf553e1b396cfa64ac75b2cdc276dabf28207675eea  SKILL.md`
  - `feae8fcc8a231893c3ab30bf4ccdae185814964ac88a874dc6c69e29ec80689d  LICENSE`
- **License:** MIT, declared in the frontmatter at ext SKILL.md:4 and backed by a bundled MIT text at ext LICENSE:1-21 ("Copyright (c) 2026 skill-analyzer fixture authors", ext LICENSE:3). Copying and modifying are allowed as long as the notice is kept.
- **Size:** SKILL.md has 35 lines, 1695 bytes and 259 words, which is about 425 tokens per full load. LICENSE has 21 lines and 1087 bytes and is not loaded by any harness. The description is 186 characters (about 45 tokens) and goes into every session's system prompt when model invocation is on.
- **Files:** two in total (`ls -la` shows no dotfiles and no subdirectories). Both are `ASCII text` (`file`), contain no non-ASCII bytes (`grep -nP '[^\x09\x0a\x0d\x20-\x7e]'` returned nothing, exit 1), and have no CR bytes.
- **Scripts and binaries:** none.
- **Frontmatter:** `name: good-standalone` (matches the folder), `description:` present (ext SKILL.md:3), `license: MIT`. No `disable-model-invocation` field, so it defaults to auto-invocation. No non-spec fields. Not malformed.
- **References:** none. There are no relative paths, no `../` escapes, no sibling-skill names, no URLs, and no tool names (see the URL and escape search in section 9). `PRODID:-//example//ics generator//EN` (ext SKILL.md:22) is a literal placeholder and not a reference. `mailto:<address>` (ext SKILL.md:25) is a template.
- **Tools and stack assumed:** the ability to write a text file with CRLF line endings. No CLI, language, or library is named. The time-zone conversion needs IANA tzdata (ext SKILL.md:14,19). It is available here: `python3 -c 'import zoneinfo; zoneinfo.ZoneInfo("Europe/Paris")'` succeeded.
- **Intended audience:** a general-purpose assistant that is asked in conversation to produce a calendar invite or attachment (ext SKILL.md:3). The final check is written for a human with a text editor (ext SKILL.md:35).

### Capability inventory

| # | ext file:line | Instruction block | Strength | Vocabulary introduced | Tools | Audience |
|---|---|---|---|---|---|---|
| C1 | SKILL.md:3 | Trigger: create a calendar invite, event file, or .ics attachment | routing | iCalendar, .ics | - | model router |
| C2 | SKILL.md:9 | Goal: standards-compliant .ics that imports without warnings | descriptive | "standards-compliant" | - | agent |
| C3 | SKILL.md:13-15 | Inputs: title, start, end or duration, IANA TZ, location, description, attendees | descriptive | IANA zone | - | agent |
| C4 | SKILL.md:19 | Convert to UTC, `YYYYMMDDTHHMMSSZ` | imperative | UTC basic format | tz conversion | agent |
| C5 | SKILL.md:20 | UID `<random hex>@<sender domain>`; never reuse | imperative + "never" | UID | randomness | agent |
| C6 | SKILL.md:21-22 | CRLF; fixed property order VCALENDAR/VEVENT | imperative | PRODID, DTSTAMP, etc. | file write | agent |
| C7 | SKILL.md:23 | Escape `,` `;` `\`; newline as `\n` | imperative | TEXT escaping | - | agent |
| C8 | SKILL.md:24 | Fold lines over 75 octets with CRLF + space | imperative | folding | - | agent |
| C9 | SKILL.md:25 | One `ATTENDEE;CN=...:mailto:...` per attendee | imperative | ATTENDEE | - | agent |
| C10 | SKILL.md:29 | Floating times gotcha; prefer UTC | advisory | floating time, TZID | - | agent |
| C11 | SKILL.md:30 | LF-only rejected by some clients | advisory | - | - | agent |
| C12 | SKILL.md:31 | All-day: `VALUE=DATE`, exclusive DTEND | advisory | VALUE=DATE | - | agent |
| C13 | SKILL.md:35 | Manual check in a text editor: CRLF, ≤75 octets | imperative | - | text editor | human |

## 3. What firstmate already has on this topic

No owner exists. Topic class "otherwise none" under skill-analyzer Tier 0 step 5. Calendar files have nothing to do with review, decisions, merging, memory, diagnosis, or project onboarding.

- `grep -rniIE 'icalendar|\.ics\b|rfc ?5545|vcalendar|vevent' <firstmate>/.agents/skills <firstmate>/AGENTS.md <firstmate>/docs <firstmate>/bin ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.pi/agent/skills` returned no output (exit=1).
- `grep -rniIE 'calendar' <firstmate>/.agents/skills <firstmate>/AGENTS.md <firstmate>/docs` returned no output.
- Elsewhere on the machine, "calendar" appears only in the user-claude `morning` skill (`.../synced/.../morning/SKILL.md:20,30,59`). That skill *reads* calendar connectors to render a morning brief and never writes `.ics`. `setup-writing-style/SKILL.md:79` says to skip calendar invites while learning a writing voice. Neither one owns this topic.
- `bin/fm-skill-surface.py` (default roots, `FM_HOME` unset in this environment) shows no `good-standalone` row (`grep -n good-standalone` exit=1) and no `same-content-as` entry for it.

## 4. Overlap map

| External piece | Firstmate today | Class |
|---|---|---|
| C1 ext SKILL.md:3 trigger | empty search (section 3, ics/calendar greps) | new |
| C2 ext SKILL.md:9 goal | empty search | new |
| C3 ext SKILL.md:13-15 inputs | empty search | new |
| C4 ext SKILL.md:19 UTC formatting | empty search | new |
| C5 ext SKILL.md:20 UID rule | empty search | new |
| C6 ext SKILL.md:21-22 CRLF and property order | empty search | new |
| C7 ext SKILL.md:23 TEXT escaping | empty search | new |
| C8 ext SKILL.md:24 line folding | empty search | new |
| C9 ext SKILL.md:25 ATTENDEE lines | empty search | new |
| C10-C12 ext SKILL.md:29-31 gotchas | empty search | new |
| C13 ext SKILL.md:35 manual text-editor check | empty search; human step for autonomous workers | noise (for workers), new (for interactive use) |

Result: 11 rows - 0 `already-done`, 0 `clash`, 10 `new` (covering C1-C12), 1 mixed `new`/`noise` (C13).

## 5. Conflicts and safety

### Conflict table

| External text | Firstmate text | Collision |
|---|---|---|
| (none) | (none) | No row of the skill touches project writes, merging, teardown, captain addressing, delivery, or review. It writes only a `.ics` file wherever the requester asks. Hard rules 1-5 (`AGENTS.md:28-46`) were read and none is engaged. |

Inferred note: if a firstmate-the-supervisor session were asked to write a `.ics` *into a project*, hard rule 1 (`AGENTS.md:28` "**Never write to a project.**") would still govern. The skill does not tell anyone to write anywhere in particular, so this is not a clash.

### Vocabulary collisions

- `grep -nwiE 'error|warning|warnings|info|auto-fix|no-op|ask-user|working|needs-decision|blocked|paused|done|failed' SKILL.md` matched only ext SKILL.md:9 "import without warnings". That is ordinary prose about calendar apps, not a severity or status label. There are no collisions with the error/warning/info, auto-fix/no-op/ask-user, or working/needs-decision/blocked/paused/done/failed sets.

### Safety findings

- No text addressed to a reviewer, scanner, or assistant: `grep -niE 'reviewer|scanner|assistant|ignore (all|previous)|system prompt'` returned no output (exit=1).
- No remote fetch or execution, no URLs, no base64 or long opaque runs: `grep -nE 'https?://|\.\./|...|base64|[A-Za-z0-9+/]{40,}'` returned no output (exit=1).
- No secrets, archives, bytecode, images, or binaries. Two ASCII text files.
- The size fits the purpose: 1695 bytes for a single-format procedure. The longest line is 211 characters (ext SKILL.md:22, the property list).
- Privacy (inferred): ext SKILL.md:15,25 put attendee email addresses into the file. That is inherent to the format. The skill never sends mail.

### Trigger analysis

- Exact description (ext SKILL.md:3): "Generate RFC 5545 iCalendar (.ics) files for meetings and reminders. Use when asked to create a calendar invite, an event file, or an .ics attachment from a date, time, and title."
- Broad phrases (`any change`, `before merging`, `always`, `any task`, `whenever`, `every time`, `all code`): `grep -niE ...` returned none (exit=1). The trigger is already narrow and specific to the format.
- Same-topic installed descriptions: none write calendar files. The nearest is user-claude `morning` ("...A question about their day, schedule, or cale[ndar]...", the surface output). It reads calendars and does not write them, so there is no routing contention.
- Model-invocation default: the frontmatter has no `disable-model-invocation`, so the skill would auto-invoke. Per the decision rules, adoption must set `disable-model-invocation: true`.

## 6. Fit and cost

- **Stack:** this does not depend on any language. Python 3 with `zoneinfo`, `date`, `openssl`, and `uuidgen` are all present (`which` found `/usr/bin/python3`, `/usr/bin/date`, `/usr/bin/openssl`, `/usr/bin/uuidgen`) for anyone who wants to script the output. The skill itself names no tools.
- **Human-in-the-loop:** the final check, ext SKILL.md:35 "Open the file in a text editor", assumes a human. An autonomous worker would have to swap in a byte check (CR count equals line count, maximum octets per physical line ≤ 75). Everything else works without a human.
- **Firstmate fit:** firstmate supervises software work (`AGENTS.md:21-24`). Calendar-file generation is not firstmate behavior, so the skill must never go into firstmate's own `.agents/skills`. The skill-analyzer placement rule keeps that location for firstmate-specific behavior only.
- **Project fit:** no projects were visible to check. The code root has no `projects/`, `data/`, `state/`, or `config/` (`ls -d` showed "No such file or directory"), and `FM_HOME` is unset. Whether any project emits `.ics` is therefore unverified (section 9).
- **Content accuracy (inferred from knowledge of RFC 5545, not checked against the RFC text, see section 9):**
  - These steps are correct: C4 (UTC basic format), C6 (VERSION, PRODID, UID, and DTSTAMP are the required properties; CRLF), C7 (escaping backslash, semicolon, comma, and newline), C8 (75-octet folding with CRLF plus a space), and C12 (all-day `VALUE=DATE` with an exclusive DTEND).
  - Gap: folding can split a multi-byte UTF-8 character. The folding must respect character boundaries, and C8 does not say so.
  - Gap: an `ATTENDEE` `CN` parameter containing `:`, `;`, or `,` must be double-quoted (C9). C7's backslash escaping applies to TEXT values, not parameters.
  - Gap: an *invite* that clients treat as a meeting request normally needs `METHOD:REQUEST` and an `ORGANIZER` property. The skill writes neither, so its output imports as a plain event, not as an invitation.
  - Ambiguity: step 3 fixes the order ending in `END:VEVENT`, `END:VCALENDAR`, and step 6 then adds `ATTENDEE` lines without saying they belong inside the VEVENT.
  - None of these is a safety issue. They lower the quality of results for "invite" requests.
- **Context cost per load:** about 425 tokens for the full SKILL.md when invoked. The always-on description costs about 45 tokens per session at any auto placement, and 0 tokens with `disable-model-invocation: true` (Pi docs `skills.md:53,79`: "Hide the skill from automatic model selection").
- **Who loads it where:**
  - Trial-only (`pi --skill <path>`): only that one Pi session.
  - One project's `.agents/skills`: Pi sessions whose working directory is inside that project (Pi `skills.md:61`). Claude-family workers only if a `.claude/skills` entry is also present.
  - User-global `~/.agents/skills` plus the `~/.claude/skills` symlink: every Pi session and every Claude Code session on the machine, including all firstmate workers. That reach is the reason the explicit-only flag is mandatory there.
  - Firstmate `.agents/skills`: not applicable (see Firstmate fit above).

## 7. Recommendation

`adopt`. This is a new topic with no owner, no clash, a trigger that is already narrow, and a small cost. It belongs outside firstmate.

1. **Placement:** start trial-only with `pi --skill <path-to-adapted-copy>`. Only when the captain has a real `.ics` need confirmed, promote to user-global `~/.agents/skills/ics-event-file` plus the `~/.claude/skills` symlink. Never place it in firstmate's own `.agents/skills`.
2. **Frontmatter for the installed copy:**
   - Rename it to `ics-event-file`. The name `good-standalone` says nothing about the skill, and the folder name must match.
   - Add `disable-model-invocation: true`.
   - Keep `license: MIT` and ship the LICENSE file with the copy.
3. **Narrowed description:** "Write one RFC 5545 iCalendar (.ics) file for a single non-recurring event from a title, a start, and an end or duration. Explicit use only, when the captain asks for an .ics file or calendar attachment."
4. **Edits to make while adapting (each one sentence):**
   - (a) Step 5: fold only on UTF-8 character boundaries, so no line exceeds 75 octets and no multi-byte character is split.
   - (b) Step 6: put `ATTENDEE` lines inside the VEVENT before `END:VEVENT`, and double-quote any `CN` value that contains `:`, `;`, or `,`.
   - (c) For a meeting *invitation*, add `METHOD:REQUEST` after `PRODID` and one `ORGANIZER;CN=...:mailto:...` line in the VEVENT.
   - (d) Replace the text-editor check with a byte check an agent can run: every line ends in CRLF and no physical line exceeds 75 octets.
5. **Trial plan (a separate, captain-approved short task, not part of this analysis):**
   - Run one Pi session with `--skill`, asking for a two-attendee meeting in `Europe/Paris` with a comma in the title and a non-ASCII location.
   - Pass needs all of the following:
     - the file passes the byte check;
     - an iCalendar parser accepts it (for example Python `icalendar`, if installed, or an import into the captain's calendar app);
     - DTSTART and DTEND are correct in UTC;
     - escaping and folding are intact.
   - Fail means the trial copy is deleted and the verdict is `decline (unfit)`.

## 8. Captain's decision

- **A (recommended):** adopt with the edits in section 7 item 4, trial-only first. Promote to user-global and explicit-only only after one trial passes.
- **B:** adopt as-is (renamed, explicit-only), straight to user-global `~/.agents/skills` plus `~/.claude/skills`, with no trial. Faster, but it keeps the missing pieces for invites and folding.
- **C:** decline (unfit). There is no real need for calendar files on this machine.

## 9. Evidence

### Commands and output (abridged)

- `find <folder> -type f -exec sha256sum {} \;` gave
  - `78ab59a6d6cd702ba3f2fdf553e1b396cfa64ac75b2cdc276dabf28207675eea  .../SKILL.md`
  - `feae8fcc8a231893c3ab30bf4ccdae185814964ac88a874dc6c69e29ec80689d  .../LICENSE`
- `file` reported both as `ASCII text`.
- `wc -lc` gave `35 1695 SKILL.md` and `21 1087 LICENSE`. `wc -w SKILL.md` gave `259`.
- `ls -la <folder>`: two regular files, no dotfiles, no subdirectories. `stat` shows mode `-rw-r--r--` on both (not executable).
- `git -C <folder> rev-parse HEAD`: `fatal: not a git repository (or any parent up to mount point /)`.
- `python3 <firstmate>/bin/fm-skill-surface.py | grep -n good-standalone` returned exit=1 (no name match, no same-content entry). The only stderr collision is `skill-creator` (user-claude vs user-codex), which is unrelated.
- Searches that returned no output (exit 1 unless noted):
  - Topic: `grep -rniIE 'icalendar|\.ics\b|rfc ?5545|vcalendar|vevent' <firstmate>/{.agents/skills,AGENTS.md,docs,bin} ~/.agents/skills ~/.claude/skills ~/.codex/skills ~/.pi/agent/skills` (exit=1), and `grep -rniIE 'calendar' <firstmate>/.agents/skills <firstmate>/AGENTS.md <firstmate>/docs` (no output).
  - Broad phrases: `grep -niE 'any change|before merging|always|any task|whenever|every time|all code' SKILL.md`.
  - URLs, escapes, and blobs: `grep -nE 'https?://|\.\./|`[a-z-]+\.(sh|py|js)`|base64|[A-Za-z0-9+/]{40,}' SKILL.md LICENSE`.
  - Injection text: `grep -niE 'reviewer|scanner|assistant|ignore (all|previous)|system prompt' SKILL.md LICENSE`.
  - Non-ASCII: `LC_ALL=C grep -nP '[^\x09\x0a\x0d\x20-\x7e]' SKILL.md LICENSE`.
- Vocabulary grep (section 5): one hit, ext SKILL.md:9 "without warnings".
- `which python3 date openssl uuidgen file sha256sum`: all present under `/usr/bin`. The `zoneinfo` `Europe/Paris` lookup succeeded.
- Firstmate code root: `/home/hugo/.no-mistakes/worktrees/3f83383b2e86/01M66J7TBMNGZSZPZQX5FC74XP` at commit `6b63be47c23a48d7aaa7f3048523ce9056a0e255`. Owner text read: `AGENTS.md:19-50` (hard rules) and `AGENTS.md:315-367` (section 9). Pi docs read: `docs/skills.md:41-80`.

### Not verified, and why

- **RFC 5545 conformance:** the claims in section 6 come from model knowledge. The RFC was not fetched because the skill cites no URL and the brief forbids fetching. Checking against RFC 5545 sections 3.1 (folding), 3.2 (parameter quoting), 3.3.11 (TEXT), and RFC 5546 (METHOD and ORGANIZER for invitations) would raise confidence in edits 4a-4c.
- **Project stack fit:** no `projects/` directory and no `FM_HOME` were visible, so it is unknown whether any project produces `.ics`. This is the deciding fact in section 1.
- **Client import behavior:** "imports without warnings" (ext SKILL.md:9) was not tested because no trial runs inside an analysis.
- **Completion gate:** the `captain-hold-lifecycle` gate (`bin/fm-captain-hold.sh complete`) was not run. This worker was told to write only this report, and the gate writes to the home's backlog. The supervisor should hold one captain task for the section 8 decision (A/B/C) with this report as its origin, then run the gate.
- **Unrelated file:** `/tmp/fm-skill-analyzer-live.FRdgf9/.fm-test-fixture` lies outside the skill folder. It was read only to confirm it is not part of the skill under test (it holds a process marker, not skill content).
