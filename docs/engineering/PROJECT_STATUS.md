# Daryaft project status

Updated 2026-11-03.

## Implemented

Local Git initialization, repository-local personal identity and SSH configuration, shared agent instructions, draft foundation documentation, issue and PR templates, and a documentation CI workflow. The public repository is [asyncnavi/daryaft](https://github.com/asyncnavi/daryaft). The initial foundation commit `40793a8` is published on `main`.

## Not implemented

Go and Python services, database schemas, Compose, API contracts, ingestion, retrieval, answering, authorization, application CI, or SDKs. The first hosted documentation CI run was in progress at the publication handoff. Documentation is a design proposal, not evidence that these capabilities exist.

## External blockers

- The personal SSH alias authenticates as `asyncnavi`.
- The repository was created publicly through the authenticated asyncnavi browser session.
- GitHub CLI has only Marzi accounts authenticated. Never use them for Daryaft writes.
- The inspected active token lacks Project read scope. Authenticate as asyncnavi with suitable repository and Project permissions before setup.
- The user authorized initial public repository creation and pushing. Subsequent publication follows the project approval policy.
- Copyright ownership and attribution are unconfirmed. No license added.
- Docker is unavailable and PostgreSQL connectivity and pgvector remain unverified.
- Local Git uses the asyncnavi account ID-based GitHub noreply address.

## Review and next work

Independent documentation review completed with its material findings addressed. Local Markdown lint, link checks, and backlog dependency checks pass. This review does not verify runtime security. The next task is D02 contracts, which can proceed after the local portion of D01 without waiting for remote setup. D03 service scaffolding follows contract review. Remote draft IDs are not GitHub issue numbers.
