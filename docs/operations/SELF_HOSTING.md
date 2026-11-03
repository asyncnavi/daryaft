# Self-hosting plan

Daryaft is not runnable yet. No supported deployment artifact exists.

The initial target is Docker Compose with the Go core, Python service, PostgreSQL with pgvector, and persistent document storage. Redis is optional only when justified. Bind internal services privately. Expose the Go API through an authenticated TLS endpoint for nonlocal use.

The implementation must document image versions, secrets, persistent volumes, limits, health checks, migrations, backups, restore verification, upgrades, and cleanup. The local filesystem adapter is intended for development. Document S3-compatible storage before advertising it as supported.

External model providers receive authorized document text. Operators need an explicit provider and data-handling decision before using confidential material. Use synthetic fixtures for the initial demonstration.
