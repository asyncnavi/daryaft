# Daryaft high-level design

## Service boundaries

The Go core is a modular monolith with identity, workspaces, authorization, library, jobs, and conversations modules. Keep business rules independent of HTTP, database, and storage adapters.

Python owns parsing, chunking, embeddings, ranking, and answer construction. It has no public end-user entry point and cannot issue arbitrary application queries. Internal requests require service authentication and timeouts. Restrict database privileges by service role.

## Retrieval and authorization

The proposed safe boundary has Python embed a query and Go perform the authoritative pgvector candidate query with workspace, active-version, deletion, and current ACL predicates. Python can rerank the authorized candidates and generate an answer from that content. Go validates returned citation IDs against the authorized candidate set before returning an answer.

Python owns retrieval algorithms, while Go owns the database operation that releases content. Do not give Python unrestricted chunk-read credentials as a shortcut. The internal contract must make this split explicit before implementation.

Recheck authorization immediately before dispatching content to the provider. Requests beginning after revocation must observe the revocation. Already transmitted provider context cannot be recalled. Define transaction and concurrency semantics in a follow-up ADR and test revocation at the dispatch boundary. Avoid authorization caches initially.

## Ingestion and version promotion

Go validates metadata and upload limits, persists the original, creates a version and durable job, and exposes status. Python processes the immutable version. Workers use leases and bounded retries. Job completion must tolerate repeated delivery.

New chunks remain staged until all expected artifacts exist. Go promotes the new active version in one transaction. Failure changes the attempted version's state while leaving the active pointer intact. Deletion tombstones the document first. Every query excludes tombstones. Cleanup is asynchronous and retryable.

## Contracts and operations

Design external OpenAPI and internal service contracts before handlers. Carry request IDs across services. Emit structured logs, latency and job metrics without raw document text, prompts, or tokens. Use bounded requests and provider timeouts. Error responses must not reveal inaccessible resource existence.

Keep PostgreSQL and pgvector. Introduce additional infrastructure only with a recorded need. Use one minimal provider interface and one working provider first.
