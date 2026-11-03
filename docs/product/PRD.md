# Daryaft product requirements

## Users and scope

Workspace members upload and find organisational knowledge. Workspace administrators manage members, groups, collections, and grants. Administrators do not gain access to employees' private conversations.

V1 includes workspaces, a company-wide library, manual PDF, DOCX, and Markdown uploads, collections, groups, document status and retries, semantic retrieval, grounded Q&A, citations, and private conversations. It also includes document replacement and deletion.

Company-wide search covers all currently accessible documents in the workspace. Document-specific Q&A applies the same authorization rules to one selected document. Neither mode may widen access.

## Observable requirements

- Every retrieval checks current workspace membership and resource grants.
- Collection permissions pass to documents. Additional document grants add access. A more restrictive document belongs in a separately restricted collection.
- Every answer cites supporting active document versions and source locations. Fabricated or inaccessible citations fail acceptance.
- When support is insufficient, the system says so rather than asserting an unsupported answer.
- Conversations are private by default. Cross-user reads fail even for workspace administrators.
- Uploads expose Uploaded, Processing, Indexed, Failed, and Reprocessing states.
- Replacing a document retains the previous indexed version until successful atomic promotion. Failure preserves the old version.
- Deletion blocks subsequent retrieval immediately and schedules storage and index cleanup.
- Document text is untrusted data. Embedded instructions cannot override application rules or authorize tools.

## First-week boundary

Demonstrate one workspace using synthetic documents, one embedding provider, one answer provider, and both query modes. Tenant and access checks are prerequisites, including for a demonstration. The first week does not promise all V1 behavior or production readiness.

Defer the web console, generated SDKs, connectors, OCR, every-provider support, Kubernetes, Kafka, and a separate vector database.

## Acceptance evidence

Use an end-to-end synthetic fixture for upload, indexing, retrieval, answer, citation, revocation, replacement failure, and deletion. Add explicit negative cases for cross-workspace and private-conversation access. Retrieval quality and unsupported-answer behavior need a small labelled evaluation set. Targets must be recorded before a measured acceptance run.
