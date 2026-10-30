---
name: good-standalone
description: Generate RFC 5545 iCalendar (.ics) files for meetings and reminders. Use when asked to create a calendar invite, an event file, or an .ics attachment from a date, time, and title.
license: MIT
---

# Calendar file generator

Write a standards-compliant `.ics` file that common calendar apps import without warnings.

## Inputs

- A title, a start date and time, and either an end time or a duration.
- An optional time zone name from the IANA database, such as `Europe/Paris`.
- Optional location, description, and attendee email addresses.

## Procedure

1. Convert the start and end to UTC and format them as `YYYYMMDDTHHMMSSZ`.
2. Generate a UID as `<random hex>@<sender domain>`; never reuse one for a different event.
3. Write the file with CRLF line endings and these lines in order:
   `BEGIN:VCALENDAR`, `VERSION:2.0`, `PRODID:-//example//ics generator//EN`, `BEGIN:VEVENT`, `UID`, `DTSTAMP`, `DTSTART`, `DTEND`, `SUMMARY`, optional `LOCATION` and `DESCRIPTION`, `END:VEVENT`, `END:VCALENDAR`.
4. Escape commas, semicolons, and backslashes in text values with a backslash, and write newlines inside text as the two characters `\n`.
5. Fold any line longer than 75 octets by inserting CRLF followed by one space.
6. Add one `ATTENDEE;CN=<name>:mailto:<address>` line per attendee.

## Gotchas

- Floating times without `Z` or `TZID` are interpreted in the reader's local zone; prefer UTC.
- Some clients reject files with LF-only line endings.
- An all-day event uses `DTSTART;VALUE=DATE:YYYYMMDD` and an exclusive `DTEND` on the next day.

## Check

Open the file in a text editor and confirm every line ends in CRLF and no line exceeds 75 octets.
