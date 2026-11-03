# Testing and quality gates

## Current evidence

No application tests, migrations, containers, or runtime security checks exist. Documentation CI runs Markdown lint and the foundation checker.

Run `python3 scripts/test_check_foundation.py` and then `python3 scripts/check_foundation.py` from the repository root. The controls modify temporary copies only. They verify rejection of missing inputs, broken local links, duplicate draft IDs, missing issue fields, incorrect counts, unknown dependencies, cycles, and an empty backlog.

The checker validates local file paths in simple inline Markdown links, required foundation files, and the unpublished backlog format. It does not validate heading anchors, reference-style links, remote URLs, semantic correctness, or runtime security. Keep Markdown lint as a separate check. Update the checker deliberately when the backlog format changes.

## Required checks by change

| Change | Required evidence |
| --- | --- |
| Go | gofmt, go vet, go test, and race detection for concurrent behavior. |
| Python | Ruff format check, Ruff lint, pytest, and type checking. |
| SQL | Apply migrations to an empty PostgreSQL instance and test constraints and tenant queries. |
| Retrieval | Labelled synthetic fixtures, expected sources, inaccessible-source negatives, and model metadata. |
| Answering | Citation validity, unsupported questions, injection attempts, and provider-context authorization. |
| Deployment | Docker image builds and Compose startup with health checks and database connectivity. |
| Repository | Markdown lint, link checks, secret scanning, and dependency review where supported. |

Tests assert observable behavior. Use unit tests for pure logic, database integration tests for ACL predicates and promotion transactions, and a full API flow for the demonstration. Avoid tests that only repeat implementation details.

Record commands, exit codes, and limitations in PRs and journals. CI passing does not replace independent review. Never report planned tests as executed. Security requirements need both negative test evidence and independent review.

Baseline CI should begin with documentation checks. Add Go, Python, migration, image, and integration jobs as their real artifacts land. Do not create empty jobs that pass without running relevant work.
