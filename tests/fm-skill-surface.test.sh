#!/usr/bin/env bash
# Behavior tests for bin/fm-skill-surface.py, the skill-analyzer's inventory of
# installed skills.
#
# Every case builds a temporary skill root and drives the executable through
# its public command line (TSV and --json), with no network and no harness.
# The last case runs the committed skill-analyzer fixture corpus and checks the
# flags each fixture's expected.json entry requires.
set -u

# shellcheck source=tests/lib.sh
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

SURFACE="$ROOT/bin/fm-skill-surface.py"
CORPUS="$ROOT/tests/fixtures/skill-analyzer"
TMP_ROOT=$(fm_test_tmproot fm-skill-surface)
LAB="$TMP_ROOT/skills"
OTHER="$TMP_ROOT/other"

write_skill() {  # <dir> <content>
  mkdir -p "$1"
  printf '%s' "$2" > "$1/SKILL.md"
}

build_lab() {
  write_skill "$LAB/plain" $'---\nname: plain\ndescription: Plain scalar description for testing.\n---\nbody\n'
  write_skill "$LAB/folded" $'---\nname: folded\ndescription: >-\n  Folded first line.\n  Folded second line.\nmetadata:\n  internal: true\n---\nbody\n'
  write_skill "$LAB/literal" $'---\nname: literal\ndescription: |\n  Literal one.\n  Literal two.\ndisable-model-invocation: true\n---\nbody\n'
  write_skill "$LAB/nofront" $'# No frontmatter here\n'
  write_skill "$LAB/nodesc" $'---\nname: nodesc\nlicense: MIT\n---\nbody\n'
  write_skill "$LAB/wrongdir" $'---\nname: another-name\ndescription: Name does not match directory.\n---\n'
  local long
  long=$(printf 'x%.0s' $(seq 1 1100))
  write_skill "$LAB/toolong" $'---\nname: toolong\ndescription: '"$long"$'\n---\n'
  write_skill "$LAB/copy-a" $'---\nname: copy-a\ndescription: Identical bytes.\n---\n'
  write_skill "$OTHER/copy-a" $'---\nname: copy-a\ndescription: Identical bytes.\n---\n'
  write_skill "$OTHER/plain" $'---\nname: plain\ndescription: A different skill with the same name.\n---\n'
  ln -s "$LAB/plain" "$OTHER/plain-link"
  write_skill "$LAB/broad" $'---\nname: broad\ndescription: Review code. Use before merging any change.\n---\n'
}

run_tsv() {
  "$SURFACE" --root "lab=$LAB" --root "other=$OTHER" 2>"$TMP_ROOT/stderr"
}

row_for() {  # <tsv> <scope> <dir-basename> -> the matching row
  printf '%s\n' "$1" | awk -F '\t' -v s="$2" -v d="$3" '$1 == s { n = split($3, p, "/"); if (p[n] == d) print }'
}

col() {  # <row> <column-number>
  printf '%s\n' "$1" | cut -f "$2"
}

test_scalar_forms_are_unfolded() {
  local out row
  out=$(run_tsv) || fail "surface exited nonzero"
  assert_equals $'scope\tname\tdir\tdescription\tmodel_invocation\tlines\tbytes\tflags' \
    "$(printf '%s\n' "$out" | head -1)" "TSV header"
  row=$(row_for "$out" lab plain)
  assert_equals "Plain scalar description for testing." "$(col "$row" 4)" "plain scalar"
  assert_equals "-" "$(col "$row" 8)" "plain has no flags"
  row=$(row_for "$out" lab folded)
  assert_equals "Folded first line. Folded second line." "$(col "$row" 4)" "folded scalar"
  row=$(row_for "$out" lab literal)
  assert_equals "Literal one. Literal two." "$(col "$row" 4)" "literal scalar flattened in TSV"
  assert_equals "explicit-only" "$(col "$row" 5)" "disable-model-invocation"
  assert_equals "auto" "$(col "$(row_for "$out" lab folded)" 5)" "default invocation"
  pass "plain, folded, and literal descriptions are read; invocation default reported"
}

test_defect_flags() {
  local out
  out=$(run_tsv) || fail "surface exited nonzero"
  assert_equals "no-frontmatter" "$(col "$(row_for "$out" lab nofront)" 8)" "no frontmatter"
  assert_equals "missing-description" "$(col "$(row_for "$out" lab nodesc)" 8)" "no description"
  assert_equals "name!=dir" "$(col "$(row_for "$out" lab wrongdir)" 8)" "name mismatch"
  assert_equals "description>1024" "$(col "$(row_for "$out" lab toolong)" 8)" "long description"
  assert_equals "broad-trigger:any change|before merging" "$(col "$(row_for "$out" lab broad)" 8)" "broad trigger"
  pass "frontmatter defects and broad triggers are flagged"
}

test_dedup_and_collisions() {
  local out err links
  out=$(run_tsv) || fail "surface exited nonzero"
  err=$(cat "$TMP_ROOT/stderr")
  assert_equals "same-content-as:lab" "$(col "$(row_for "$out" other copy-a)" 8)" "identical content flagged"
  links=$(printf '%s\n' "$out" | awk -F '\t' '$2 == "plain"' | wc -l | tr -d ' ')
  assert_equals 2 "$links" "symlinked skill listed once, distinct same-name skill kept"
  assert_contains "$err" "NAME COLLISIONS" "collision summary"
  assert_contains "$err" "  plain: lab=$LAB/plain; other=$OTHER/plain" "plain collision line"
  assert_not_contains "$err" "copy-a:" "identical content is not a collision"
  pass "symlinks collapse, identical copies are flagged, real name collisions are summarised"
}

test_json_output() {
  local json
  json=$("$SURFACE" --json --root "lab=$LAB" --root "other=$OTHER") || fail "json run failed"
  printf '%s' "$json" | python3 -c '
import json, sys
d = json.load(sys.stdin)
rows = {(r["scope"], r["dir"].rsplit("/", 1)[-1]): r for r in d["skills"]}
lit = rows[("lab", "literal")]
assert lit["description"] == "Literal one.\nLiteral two.", lit
assert isinstance(lit["lines"], int) and isinstance(lit["bytes"], int)
assert rows[("lab", "nodesc")]["flags"] == ["missing-description"]
assert rows[("other", "copy-a")]["flags"] == ["same-content-as:lab"]
names = [c["name"] for c in d["collisions"]]
assert names == ["plain"], names
assert [e["scope"] for e in d["collisions"][0]["entries"]] == ["lab", "other"]
' || fail "json shape"
  pass "--json carries rows, typed sizes, flag lists, and collisions"
}

test_usage_errors() {
  local code
  "$SURFACE" --root nodir >/dev/null 2>&1
  code=$?
  expect_code 2 "$code" "--root without ="
  "$SURFACE" --bogus >/dev/null 2>&1
  code=$?
  expect_code 2 "$code" "unknown flag"
  "$SURFACE" --help | grep -q 'same-content-as' || fail "--help lists flags"
  "$SURFACE" --root "none=$TMP_ROOT/missing" >"$TMP_ROOT/empty.tsv" || fail "missing root is skipped"
  assert_equals 1 "$(wc -l < "$TMP_ROOT/empty.tsv" | tr -d ' ')" "missing root yields header only"
  pass "usage errors exit 2; missing roots are skipped"
}

test_fixture_corpus_flags() {
  "$SURFACE" --json --root "fixtures=$CORPUS" > "$TMP_ROOT/corpus.json" || fail "corpus run failed"
  python3 - "$TMP_ROOT/corpus.json" "$CORPUS/expected.json" <<'PY' || fail "fixture flags differ from expected.json"
import json, sys
surface = json.load(open(sys.argv[1], encoding="utf-8"))
expected = json.load(open(sys.argv[2], encoding="utf-8"))["fixtures"]
rows = {r["dir"].rsplit("/", 1)[-1]: r for r in surface["skills"]}
assert sorted(rows) == sorted(expected), (sorted(rows), sorted(expected))
for fixture, want in expected.items():
    row = rows[fixture]
    assert row["name"] == want["name"], (fixture, row["name"])
    assert row["flags"] == want["surface_flags"], (fixture, row["flags"], want["surface_flags"])
PY
  pass "fixture corpus flags match expected.json"
}

build_lab
fm_test_run \
  test_scalar_forms_are_unfolded \
  test_defect_flags \
  test_dedup_and_collisions \
  test_json_output \
  test_usage_errors \
  test_fixture_corpus_flags
