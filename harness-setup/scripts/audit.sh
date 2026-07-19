#!/usr/bin/env bash
# audit.sh — docs harness health detector for adopt mode.
# Usage: bash audit.sh <repo-root> <harness-dir>
# Example: bash audit.sh /repo evals
#
# Reports evidence for one user-selected docs harness: doc graveyards, encoding
# corruption, version-numbered plan files, and stale local markdown links.

set -u
export LC_ALL=C.UTF-8 2>/dev/null || true

ROOT="${1:-.}"
HARNESS_DIR="${2:-}"

if [ -z "$HARNESS_DIR" ]; then
  echo "usage: bash audit.sh <repo-root> <harness-dir>" >&2
  exit 2
fi

cd "$ROOT" || { echo "cannot cd to repo root: $ROOT" >&2; exit 1; }

if [ ! -d "$HARNESS_DIR" ]; then
  echo "harness directory not found: $HARNESS_DIR" >&2
  exit 1
fi

GRAVEYARD_LINES=800

echo "=== Harness audit ==="
echo "repo root:    $ROOT"
echo "harness dir:  $HARNESS_DIR"

mapfile -t MD < <(find "$HARNESS_DIR" -type f -name '*.md' \
  -not -path '*/node_modules/*' -not -path '*/.git/*' \
  -not -path '*/dist/*' -not -path '*/.output/*' \
  -not -path '*/__pycache__/*' | sort)

echo
echo "--- [1] Markdown files in harness ---"
if [ "${#MD[@]}" -eq 0 ]; then
  echo "  none"
else
  printf '  %s\n' "${MD[@]}"
fi

echo
echo "--- [2] Oversized docs (graveyard candidates, > ${GRAVEYARD_LINES} lines) ---"
found=0
for f in "${MD[@]}"; do
  n=$(wc -l < "$f")
  if [ "$n" -gt "$GRAVEYARD_LINES" ]; then
    printf '  %6d  %s\n' "$n" "$f"
    found=1
  fi
done
[ "$found" = 0 ] && echo "  none"

echo
echo "--- [3] Encoding corruption (lossy mojibake / replacement chars) ---"
found=0
for f in "${MD[@]}"; do
  if grep -aqP '[\xe4-\xe9][\x80-\xbf]\x3f' "$f" 2>/dev/null || grep -aqP '\xef\xbf\xbd' "$f" 2>/dev/null; then
    printf '  CORRUPT  %s\n' "$f"
    found=1
  fi
done
[ "$found" = 0 ] && echo "  none"

echo
echo "--- [4] Version-numbered plan files (anti-pattern) ---"
found=0
for f in "${MD[@]}"; do
  case "$f" in
    */docs/testing/log/*) continue ;;
  esac
  case "$(basename "$f")" in
    *_v[0-9].md|*_v[0-9][0-9].md|*-v[0-9].md|impl_v*.md|*[._-][vV][0-9]*.md)
      printf '  %s\n' "$f"
      found=1
      ;;
  esac
done
[ "$found" = 0 ] && echo "  none"

echo
echo "--- [5] Stale cross-references inside harness docs ---"
found=0
for f in "${MD[@]}"; do
  dir=$(dirname "$f")
  while IFS= read -r link; do
    case "$link" in
      http*|\#*|mailto:*|"") continue ;;
    esac
    target="${link%%#*}"
    [ -z "$target" ] && continue
    case "$target" in
      */)
        if [ ! -d "$dir/$target" ]; then
          echo "  $f -> $link (missing dir)"
          found=1
        fi
        ;;
      *)
        if [ ! -e "$dir/$target" ]; then
          echo "  $f -> $link (missing file)"
          found=1
        fi
        ;;
    esac
  done < <(grep -aoE '\]\([^)]+\)' "$f" 2>/dev/null | sed -E 's/^\]\(([^)]+)\)$/\1/')
done
[ "$found" = 0 ] && echo "  none"

echo
echo "--- [6] Scoped agent/runbook files (not default for this skill) ---"
found=0
for f in "$HARNESS_DIR/AGENTS.md" "$HARNESS_DIR/harness_management.md"; do
  if [ -e "$f" ]; then
    echo "  found $f"
    found=1
  fi
done
[ "$found" = 0 ] && echo "  none"

echo
echo "=== audit done ==="
