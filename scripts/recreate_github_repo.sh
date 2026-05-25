#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${REPO_NAME:-pm-skill-lap}"
GITHUB_OWNER="${GITHUB_OWNER:-}"
VISIBILITY="${VISIBILITY:-private}"
CONFIRM_DELETE="${CONFIRM_DELETE:-}"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install it first."
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Run: gh auth login"
  exit 1
fi

if [ -z "$GITHUB_OWNER" ]; then
  GITHUB_OWNER="$(gh api user --jq .login)"
fi

FULL_REPO="$GITHUB_OWNER/$REPO_NAME"

echo "Target repo: $FULL_REPO"
echo "Visibility: $VISIBILITY"

if gh repo view "$FULL_REPO" >/dev/null 2>&1; then
  echo "Remote repo exists: $FULL_REPO"
  if [ "$CONFIRM_DELETE" != "DELETE" ]; then
    echo "Refusing to delete without explicit confirmation."
    echo "Re-run with: CONFIRM_DELETE=DELETE GITHUB_OWNER=$GITHUB_OWNER REPO_NAME=$REPO_NAME ./scripts/recreate_github_repo.sh"
    exit 1
  fi
  echo "Deleting $FULL_REPO ..."
  gh repo delete "$FULL_REPO" --yes
fi

if [ "$VISIBILITY" = "public" ]; then
  gh repo create "$FULL_REPO" --public --source . --remote origin --push
else
  gh repo create "$FULL_REPO" --private --source . --remote origin --push
fi

echo "Done: https://github.com/$FULL_REPO"
