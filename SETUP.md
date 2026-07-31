# Setup — 15 minutes, once

## 1. Kill the StreamPulse workflow first

```bash
gh workflow list --all --repo ayushgupta07xx/StreamPulse-NSE
gh workflow disable "Scheduled Isolation Forest retrain" --repo ayushgupta07xx/StreamPulse-NSE
```

Belt and braces — also remove the trigger so it can't be re-enabled by accident:

```bash
gh repo clone ayushgupta07xx/StreamPulse-NSE /tmp/sp && cd /tmp/sp
git rm .github/workflows/<retrain-workflow>.yml
git commit -m "chore: retire scheduled retrain job (project paused)"
git push
```

## 2. Create this repo

```bash
cd cloud-incident-atlas
git init -b main
gh repo create cloud-incident-atlas --public --source=. \
  --description "Normalized cross-vendor cloud incident dataset with derived reliability metrics"
```

## 3. Set the commit identity — THIS IS THE STEP THAT MATTERS

Find your noreply alias at https://github.com/settings/emails
(format: `12345678+ayushgupta07xx@users.noreply.github.com`)

```bash
gh variable set COMMIT_EMAIL --body "<your-noreply-alias>" --repo ayushgupta07xx/cloud-incident-atlas
```

If this is wrong or unset, the workflow fails loudly rather than committing to
a void. Nothing on your graph counts unless the author email is one GitHub has
associated with your account.

## 4. First run

```bash
python -m src.ingest --dry-run     # verify feeds reachable locally
git add -A && git commit -m "feat: initial ingest pipeline for 13 providers"
git push -u origin main
gh workflow run "Daily incident ingest"
```

Watch it: `gh run watch`

## 5. Verify attribution

After the first automated commit lands, check that it shows your avatar and not
a bot avatar:

```bash
gh api repos/ayushgupta07xx/cloud-incident-atlas/commits --jq '.[0].author.login'
```

Should print `ayushgupta07xx`. If it prints `github-actions[bot]` or `null`, the
COMMIT_EMAIL variable is wrong. Contribution graphs can take a few minutes to
reindex.

## 6. If the repo goes quiet

Public repos have scheduled workflows auto-disabled after 60 days with no
repository activity. Daily commits keep it alive, so this won't bite you — but
if you pause the project for two months, expect to re-enable it manually.
