# Coding standards

Use conventional commits. Name issue branches `feat/<issue-number>-description`, `fix/<issue-number>-description`, or `docs/<issue-number>-description`. The foundation branch predates remote issue creation.

Keep Go business rules independent of handlers and database adapters. Use explicit errors, context cancellation, bounded operations, and dependency interfaces only where behavior needs substitution. Format with gofmt. Run go vet and meaningful tests.

Use Python type annotations at service boundaries. Run Ruff formatting and linting, pytest, and a selected type checker. Parse external data at boundaries. Do not build abstractions for providers that have no implementation.

Keep SQL tenant-aware and parameterized. Migrations need constraints, indexes, and clean-database verification. Never silently discard data or change ACL semantics.

Use structured logs without document contents, prompts, credentials, or private messages. Comments explain non-obvious reasons. Keep ownership clear and avoid one-caller wrappers with no domain purpose.

Update OpenAPI before changing public behavior. Do not generate SDKs until the contract is stable. Every PR records its problem, issue, design decisions, tests, verification, limitations, and documentation changes.
