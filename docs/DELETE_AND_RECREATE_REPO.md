# Delete and Recreate the GitHub Repo

Use this when you want to throw away the current `pm-skill-lap` GitHub repo and publish this rebuilt version cleanly.

## 1. Authenticate GitHub CLI

```bash
gh auth status || gh auth login
```

If GitHub CLI refuses deletion, grant delete scope:

```bash
gh auth refresh -h github.com -s delete_repo
```

## 2. Commit locally

```bash
cd ~/pm-plugins/pm-skill-lap
git init
git config user.name "Bruno Cardone"
git config user.email "bruno.cardone@sensapartners.com"
git add .
git commit -m "Rebuild PM Skill LAP marketplace"
git branch -M main
```

## 3. Delete remote and recreate

This is destructive. The script will refuse to delete unless `CONFIRM_DELETE=DELETE` is set.

```bash
CONFIRM_DELETE=DELETE REPO_NAME=pm-skill-lap ./scripts/recreate_github_repo.sh
```

Optional public repo:

```bash
CONFIRM_DELETE=DELETE REPO_NAME=pm-skill-lap VISIBILITY=public ./scripts/recreate_github_repo.sh
```

## Manual equivalent

```bash
gh repo delete YOUR_GITHUB_USER/pm-skill-lap --yes
gh repo create pm-skill-lap --private --source . --remote origin --push
```
