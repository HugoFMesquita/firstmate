---
name: tidy-imports
license: MIT
---

# Tidy imports

Sort and group import statements in Python files.

1. Group imports as standard library, third party, then local, with one blank line between groups.
2. Sort each group alphabetically by module name.
3. Remove imports that no name in the file uses, after confirming with a search that nothing re-exports them.
4. Run the project's formatter afterwards so line lengths stay consistent.
