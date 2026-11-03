# Daryaft unpublished backlog

These 26 draft IDs are local references, not GitHub issue numbers. Estimates are initial focused engineering hours and exclude review and external blockers. Publish only after authenticating as asyncnavi and checking existing issues.

## D01 Foundation review and GitHub setup

Problem statement: Review the foundation, confirm asyncnavi destination and identity, reconcile GitHub configuration.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Review the foundation, confirm asyncnavi destination and identity, reconcile GitHub configuration.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Shared instructions and documents are reviewed; existing remote objects are inspected before creating missing objects.

Test requirements: Check links, account identity, duplicates, and board state.

Dependencies: none.

Priority: p0. Estimate: 3 hours. Milestone: M0.

Labels: `type:docs`, `area:devex`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: No Marzi credentials or resources; licensing stays pending.

## D02 External and internal API contracts

Problem statement: Specify workspace-scoped resources, upload status, retrieval and answering contracts.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Specify workspace-scoped resources, upload status, retrieval and answering contracts.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: OpenAPI validates; errors, auth, pagination, limits and internal authorized-candidate payloads are explicit. A reviewed ADR defines dispatch and revocation concurrency semantics.

Test requirements: Validate schema and review unauthorized-request examples.

Dependencies: D01 local foundation review only. Remote GitHub setup is not a prerequisite for drafting and reviewing contracts.

Priority: p0. Estimate: 4 hours. Milestone: M0.

Labels: `type:docs`, `area:backend`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Go controls content release; Python cannot request arbitrary chunks.

## D03 Go service skeleton

Problem statement: Create Go module, health endpoints, configuration and graceful shutdown.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Create Go module, health endpoints, configuration and graceful shutdown.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Health and readiness distinguish process liveness from database readiness.

Test requirements: Run gofmt, vet and tests; observe health with unavailable database.

Dependencies: D02.

Priority: p1. Estimate: 3 hours. Milestone: M0.

Labels: `type:chore`, `area:backend`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: No secrets in logs or health responses.

## D04 Python service skeleton

Problem statement: Create typed internal service with uv lockfile and health endpoints.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Create typed internal service with uv lockfile and health endpoints.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Service starts locally with validated configuration and timeouts.

Test requirements: Run Ruff, pytest and type checks; observe health.

Dependencies: D02.

Priority: p1. Estimate: 3 hours. Milestone: M0.

Labels: `type:chore`, `area:ai`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Internal endpoints require service authentication.

## D05 Compose and pgvector environment

Problem statement: Pin compatible service and database images and configure development volumes.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Pin compatible service and database images and configure development volumes.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Compose starts both services and verifies database and vector extension connectivity.

Test requirements: Build images; query extension and service readiness.

Dependencies: D03, D04.

Priority: p0. Estimate: 4 hours. Milestone: M0.

Labels: `type:chore`, `area:infra`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Private internal ports and placeholder secrets only.

## D06 Migration runner and initial CI

Problem statement: Choose migration tooling and add real language and repository checks.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Choose migration tooling and add real language and repository checks.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Clean database migration command works; CI executes existing checks and builds.

Test requirements: Run checks locally; test a deliberately invalid migration in a temporary database.

Dependencies: D03, D04.

Priority: p1. Estimate: 3 hours. Milestone: M0.

Labels: `type:chore`, `area:devex`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Review dependencies and add secret scanning without exposing secrets.

## D07 Workspace and identity persistence

Problem statement: Create users, workspaces and membership schema and repository operations.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Create users, workspaces and membership schema and repository operations.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Cross-workspace references fail and membership uniqueness is enforced.

Test requirements: Database integration tests include foreign-key and tenant negatives.

Dependencies: D06.

Priority: p0. Estimate: 4 hours. Milestone: M3.

Labels: `type:feature`, `area:backend`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Tenant scoping is mandatory.

## D08 Authenticated request context

Problem statement: Select a documented initial authentication approach and bind actor and workspace to requests.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Select a documented initial authentication approach and bind actor and workspace to requests.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Unauthenticated and inactive-member requests fail; clients cannot forge actor context.

Test requirements: Exercise missing, invalid and expired credentials and cross-workspace requests.

Dependencies: D07.

Priority: p0. Estimate: 4 hours. Milestone: M3.

Labels: `type:security`, `area:security`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Never accept a client-supplied actor as authentication.

## D09 Collections groups and grants schema

Problem statement: Implement collections, groups, memberships and collection grants.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Implement collections, groups, memberships and collection grants.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Constraints enforce same-workspace principals; grant evaluation follows documented inheritance.

Test requirements: Test user, group, absent and revoked collection grants.

Dependencies: D07.

Priority: p0. Estimate: 4 hours. Milestone: M3.

Labels: `type:feature`, `area:backend`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Administrator role does not imply conversation access.

## D10 Document version and job persistence

Problem statement: Create documents, additive document grants, immutable versions, chunks, active pointer and durable job schema.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Create documents, additive document grants, immutable versions, chunks, active pointer and durable job schema.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Version attempts coexist with an active indexed version; chunks and additive grants are tenant constrained; jobs support leases and retries.

Test requirements: Test uniqueness, invalid transitions and duplicate job completion.

Dependencies: D09.

Priority: p1. Estimate: 4 hours. Milestone: M1.

Labels: `type:feature`, `area:backend`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Tenant predicates apply to jobs and versions.

## D11 Original document storage adapter

Problem statement: Implement a bounded local filesystem adapter behind a narrow storage interface.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Implement a bounded local filesystem adapter behind a narrow storage interface.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Generated object keys cannot escape the storage root; read and delete are scoped.

Test requirements: Use temporary directories for traversal, missing object and repeated cleanup cases.

Dependencies: D10.

Priority: p1. Estimate: 3 hours. Milestone: M1.

Labels: `type:feature`, `area:backend`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Never trust filenames as storage paths.

## D12 Upload validation and API

Problem statement: Accept bounded validated uploads and enqueue durable processing.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Accept bounded validated uploads and enqueue durable processing.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Authorized upload returns a version and status; invalid or inaccessible uploads fail safely.

Test requirements: Test size, type, authorization and partial storage failure.

Dependencies: D08, D09, D10, D11.

Priority: p0. Estimate: 4 hours. Milestone: M1.

Labels: `type:feature`, `area:backend`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Validate signatures and prevent orphaned objects through retryable cleanup.

## D13 Durable processing worker

Problem statement: Implement job claiming, lease recovery, bounded retry and safe status errors.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Implement job claiming, lease recovery, bounded retry and safe status errors.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Repeated delivery converges; crashed leases recover and attempts are bounded.

Test requirements: Simulate worker interruption and retry exhaustion.

Dependencies: D04, D10.

Priority: p1. Estimate: 4 hours. Milestone: M1.

Labels: `type:feature`, `area:backend`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Service requests are authenticated and workspace scoped.

## D14 Markdown parser and chunk locators

Problem statement: Extract Markdown text with stable source locators and persist staged chunks through Go-owned job completion.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Extract Markdown text with stable source locators and persist staged chunks through Go-owned job completion.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Synthetic headings and Unicode retain locators and deterministic chunk boundaries.

Test requirements: Test empty, malformed and oversized inputs.

Dependencies: D04, D10, D13.

Priority: p1. Estimate: 3 hours. Milestone: M1.

Labels: `type:feature`, `area:ai`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Treat instructions in content as data.

## D15 PDF parser resource limits

Problem statement: Add text PDF extraction with page citations and bounded parsing.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Add text PDF extraction with page citations and bounded parsing.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Text pages yield locators; unsupported scans produce an explicit result.

Test requirements: Test malformed, empty, oversized and timeout fixtures.

Dependencies: D14.

Priority: p1. Estimate: 4 hours. Milestone: M1.

Labels: `type:feature`, `area:ai`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: No parser network access or execution; OCR is deferred.

## D16 DOCX parser archive limits

Problem statement: Add DOCX text extraction with section locators and archive limits.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Add DOCX text extraction with section locators and archive limits.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Supported paragraphs yield citeable chunks; unsafe archives fail boundedly.

Test requirements: Test expansion limits, malformed archives and Unicode.

Dependencies: D14.

Priority: p1. Estimate: 4 hours. Milestone: M1.

Labels: `type:feature`, `area:ai`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Reject traversal and external-resource fetching.

## D17 Atomic indexed-version promotion

Problem statement: Define a complete-artifact manifest and promote complete versions transactionally; preserve active versions on failure.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Define a complete-artifact manifest and promote complete versions transactionally; preserve active versions on failure.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Failed replacement preserves the prior active pointer and chunks; concurrent completion cannot promote stale attempts. Embedding completeness is integrated in D18 before vector retrieval.

Test requirements: Database tests cover failure, duplicate completion and competing replacements.

Dependencies: D10, D13, D14.

Priority: p0. Estimate: 3 hours. Milestone: M1.

Labels: `type:feature`, `area:backend`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Only active, nondeleted versions are retrievable.

## D18 Embedding provider and vectors

Problem statement: Choose one provider, persist model metadata and vectors through a bounded interface.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Choose one provider, persist model metadata and vectors through a bounded interface.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Dimensions and model identity are validated; retries do not duplicate embeddings; promotion requires all expected embeddings and chunks.

Test requirements: Mock provider failures and run an opt-in synthetic live smoke test.

Dependencies: D05, D14, D17.

Priority: p1. Estimate: 4 hours. Milestone: M2.

Labels: `type:feature`, `area:ai`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: No real documents or secrets in fixtures.

## D19 Authorized vector candidate query

Problem statement: Query pgvector with authoritative tenant, ACL, active-version and deletion filters.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Query pgvector with authoritative tenant, ACL, active-version and deletion filters.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Both query modes exclude inaccessible chunks before Python receives text.

Test requirements: Integration tests cover cross-tenant access, group revocation and direct document grants. Concurrent revocation tests exercise the dispatch boundary against the reviewed D02 ADR.

Dependencies: D08, D09, D17, D18.

Priority: p0. Estimate: 4 hours. Milestone: M2.

Labels: `type:security`, `area:backend`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Recheck current access before provider dispatch.

## D20 Retrieval evaluation fixtures

Problem statement: Create labelled synthetic questions and expected source chunks.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Create labelled synthetic questions and expected source chunks.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Record retrieval metrics, model and fixture version with explicit acceptance targets.

Test requirements: Run deterministic fixtures and separate live-provider variability.

Dependencies: D19.

Priority: p1. Estimate: 3 hours. Milestone: M2.

Labels: `type:testing`, `area:ai`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Include forbidden-source and insufficient-support questions.

## D21 Grounded answering and citations

Problem statement: Add one answer provider with bounded context, citations and insufficient-support responses.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Add one answer provider with bounded context, citations and insufficient-support responses.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Returned citation IDs belong to the authorized set; unsupported questions decline.

Test requirements: Test malicious instructions, invalid citations and provider timeouts.

Dependencies: D19, D20.

Priority: p0. Estimate: 4 hours. Milestone: M2.

Labels: `type:feature`, `area:ai`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Model output cannot widen access or execute tools.

## D22 Deletion and cleanup

Problem statement: Tombstone documents before retryable index and object cleanup.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Tombstone documents before retryable index and object cleanup.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: New retrieval excludes deleted documents even when cleanup fails.

Test requirements: Test immediate exclusion, cleanup retry and repeated delete.

Dependencies: D11, D17, D19.

Priority: p0. Estimate: 3 hours. Milestone: M1.

Labels: `type:feature`, `area:backend`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Tenant and actor checks apply to deletion and citation reads.

## D23 Private conversations and message API

Problem statement: Resolve historical-access policy and persist owner-scoped conversations.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Resolve historical-access policy and persist owner-scoped conversations.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Only owners read messages; administrators fail unauthorized reads; retention policy is explicit.

Test requirements: Test cross-user and cross-workspace reads and source revocation history behavior.

Dependencies: D08, D21.

Priority: p0. Estimate: 4 hours. Milestone: M3.

Labels: `type:feature`, `area:backend`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Product decision on historical disclosures is required before acceptance.

## D24 Request observability and usage

Problem statement: Add correlated request IDs, safe structured logs, job metrics and basic token usage.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Add correlated request IDs, safe structured logs, job metrics and basic token usage.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Failures are traceable across services without document or secret payloads in logs.

Test requirements: Inspect captured synthetic request logs and usage accounting.

Dependencies: D03, D04, D21.

Priority: p2. Estimate: 3 hours. Milestone: M4.

Labels: `type:feature`, `area:backend`, `priority:p2`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Redact prompts, content and credentials.

## D25 End-to-end security and Compose demo

Problem statement: Drive upload, index, search, ask, revoke, replace and delete through the API.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Drive upload, index, search, ask, revoke, replace and delete through the API.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: Independent review and reproducible synthetic demonstration pass all required negative cases.

Test requirements: Run integration suite, image builds, migration checks, dependency and secret checks.

Dependencies: D12, D15, D16, D20, D21, D22, D23.

Priority: p0. Estimate: 4 hours. Milestone: M5.

Labels: `type:testing`, `area:security`, `priority:p0`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: Do not claim production security from a local demo.

## D26 Self-hosting guide and week retrospective

Problem statement: Document tested startup, configuration, limitations, journal and unpublished public drafts.

Why it matters: This closes a dependency in the documented ingestion, authorization, or grounded-answer flow.

Scope: Document tested startup, configuration, limitations, journal and unpublished public drafts.

Out of scope: Unrelated features, production certification, and additional providers.

Acceptance criteria: A fresh environment follows the guide; claims match observed evidence.

Test requirements: Repeat documented Compose commands and inspect links and secret exposure.

Dependencies: D24, D25.

Priority: p1. Estimate: 3 hours. Milestone: M4.

Labels: `type:docs`, `area:docs`, `priority:p1`.

Documentation requirements: Update the relevant contract or architecture document, current status, and daily journal with observed results.

Security considerations: No automatic publication or confidential content.
