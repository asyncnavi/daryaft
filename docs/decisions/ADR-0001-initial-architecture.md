# ADR-0001 Initial architecture

Status: Proposed, pending independent review.

Date: 2026-11-03.

## Context

Daryaft needs a self-hostable API-first platform with tenant isolation and grounded answers. The first implementation must remain small enough to understand and operate.

## Decision

Use a Go modular monolith and a separate Python AI service. Use PostgreSQL with pgvector for application data and vectors. Store originals through a local filesystem adapter initially and an S3-compatible adapter when needed. Use Docker Compose for the initial local environment.

Go controls release of authorized chunks. Python owns retrieval algorithms and answer generation. Use durable database jobs first. Redis remains available when coordination requirements justify it. Defer a separate vector database, Kubernetes, Kafka, and optional console.

Keep contracts explicit, provider interfaces narrow, and one provider implementation initially. Preserve old indexed versions until replacement succeeds.

## Consequences and alternatives

One database reduces initial operational work but makes query filtering, indexes, and workload limits important. A separate Python service adds an internal contract and deployment boundary but keeps parsing and AI dependencies outside Go.

Giving Python unrestricted retrieval access would simplify some library integrations but would weaken the required authorization boundary. Reject that shortcut. The precise dispatch and revocation concurrency contract needs a later ADR before answering implementation.

## Verification

Independent architecture review, ACL integration tests, replacement failure tests, and a Compose demonstration are pending. This ADR does not establish runtime security.
