# Local development

The repository currently contains documentation only. There are no service startup commands yet.

## Foundation inspection

On 2026-11-03, the workstation reported Go 1.26.3, Python 3.14.6, Node.js 25.8.2, npm 11.11.1, uv 0.11.24, Docker CLI 29.2.1, Compose v5.0.2, and PostgreSQL client 18.3. Docker was not reachable. PostgreSQL did not respond on the default socket. pgvector was not verified.

Select supported runtime and image versions after checking parser and provider dependencies. Pin versions and lock dependencies in the scaffolding work. Do not change global runtimes just to match a draft.

Use Go modules and uv for Python. Node is unnecessary until documentation tooling or a console needs it. Keep local secrets in ignored environment files and document safe placeholders in `.env.example` when services exist.

## Git identity

This repository uses a local `asyncnavi` identity and the personal SSH key. The noreply address uses the public asyncnavi account ID. The origin remote is `git@github-personal:asyncnavi/daryaft.git`. Verify `git config --local --list` and `ssh -T git@github-personal` before publishing changes.

GitHub API operations require an authenticated `asyncnavi` account. SSH access does not authorize Issues or Projects API calls. Never use the globally active Marzi API account for Daryaft writes.
