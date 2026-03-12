# Disqus Comment Email Notification

This repository now includes `.github/workflows/disqus-comment-notify.yml` and
`scripts/disqus_comment_notifier.py`.

The workflow runs every 10 minutes, polls Disqus for new approved comments, and
sends an email with the post link and comment summary.

## Required GitHub Secrets

Add these secrets in:
`Repository -> Settings -> Secrets and variables -> Actions`

- `DISQUS_API_KEY`
  - Disqus public API key for your application.
- `SMTP_USERNAME`
  - Naver sender email address (e.g. `yourid@naver.com`)
- `SMTP_PASSWORD`
  - SMTP password or app password

Naver SMTP defaults are already set in workflow:

- Server: `smtp.naver.com`
- Port: `587`
- Secure: `false` (STARTTLS)

## First Run Behavior

The first successful workflow run initializes a baseline state and does not
send an email. This prevents a bulk notification for old comments.

After baseline setup, only comments that appeared after the previous run are
emailed.

## Manual Test

1. Go to `Actions -> Disqus Comment Notify`.
2. Click `Run workflow`.
3. Confirm the run succeeds.
4. Add a new comment on the blog.
5. Run workflow again (or wait for schedule) and verify email delivery.
