#!/usr/bin/env bash
set -euo pipefail

REPO="${GITHUB_REPOSITORY:-Tejanshu22/PersonalFinanceManager}"
MODE="${1:---dry-run}"
if [[ "$MODE" != '--dry-run' && "$MODE" != '--apply' ]]; then
  echo 'Usage: bash scripts/first_run_github.sh [--dry-run|--apply]' >&2
  exit 2
fi
command -v gh >/dev/null || { echo 'Install the GitHub CLI (gh) first.' >&2; exit 1; }
command -v python >/dev/null || { echo 'Python is required.' >&2; exit 1; }
gh auth status >/dev/null || { echo 'Run: gh auth login' >&2; exit 1; }

# An explicit authenticated repository check: fail rather than writing to a guessed repo.
DEFAULT_BRANCH="$(gh repo view "$REPO" --json defaultBranchRef --jq '.defaultBranchRef.name // ""')"
if [[ "$DEFAULT_BRANCH" != 'main' ]]; then
  echo "Expected default branch main; found: ${DEFAULT_BRANCH:-<none>}. Adjust workflows/default branch first." >&2
  exit 1
fi

if [[ "$MODE" == '--dry-run' ]]; then
  echo "Would configure labels and preview 12 issues for $REPO (no GitHub writes)."
  python scripts/bootstrap_issues.py --kind both --release V1 --limit 12
  exit 0
fi

echo "Creating/updating tracker labels in $REPO..."
gh label create 'in-progress' -R "$REPO" --color '0366D6' --description 'Currently being implemented' --force
gh label create 'blocked' -R "$REPO" --color 'D93F0B' --description 'Blocked or unresolved' --force
gh label create 'verified' -R "$REPO" --color '0E8A16' --description 'Human acceptance, tests and relevant reviews passed' --force
gh label create 'canceled' -R "$REPO" --color '6A737D' --description 'Explicitly canceled scope' --force

# Token is kept in a process environment, not stored in a file or printed.
export GITHUB_REPOSITORY="$REPO"
export GITHUB_TOKEN="$(gh auth token)"
python scripts/bootstrap_issues.py --kind both --release V1 --limit 12 --apply
unset GITHUB_TOKEN

echo 'Ready. Start Actions → Synchronize project progress → Run workflow.'
echo 'Do not mark issues verified without human acceptance and required tests.'
