# Daryaft security model

## Trust boundaries

Users, uploaded bytes, extracted text, model responses, and client-supplied identifiers are untrusted. Go is the authorization authority. Python and external providers receive only the content authorized for that operation. A service credential does not substitute for user authorization.

Workspace isolation applies to uploads, metadata, storage paths, jobs, vector queries, citations, and conversations. Queries must include tenant predicates even when an identifier appears globally unique. Reject cross-workspace references at persistence boundaries too.

## Access semantics

Collection grants are inherited. Document grants are additive. Group membership and grants are resolved from current state on every retrieval. Revocation affects subsequent requests. No authorization-result cache is planned initially.

Conversation ownership is explicit. Workspace administrators do not automatically read private conversations. Historical answer retention after source revocation remains an open decision. Until resolved, do not claim that revocation erases already disclosed information.

## Untrusted documents and providers

Validate extension, signature, size, and parser limits. Define limits in configuration and test them. DOCX requires archive expansion limits. Parse with restricted resources, no network, and isolated temporary files. Never execute uploaded content. OCR is out of scope initially.

Delimit retrieved context as data. Never give a model authority to change grants, execute tools, or select unrestricted resources. Validate citations against the authorized set. Prompt text alone is not a security boundary or proof of injection resistance.

Provider configuration must disclose which external service receives document text. Keep secrets outside Git. Avoid raw content in logs and traces. Use synthetic fixtures exclusively in public examples and tests.

## Required evidence before acceptance

- Cross-workspace access fails for metadata, chunks, citations, jobs, and conversations.
- User and group revocation affect subsequent retrieval and provider dispatch.
- Python cannot fetch arbitrary chunks or override the authorized candidate set.
- Deleted documents stop appearing before asynchronous cleanup finishes.
- Failed replacement preserves the prior indexed version.
- Malicious document instructions cannot widen retrieval or cause tool execution.
- Parser timeout, oversized input, and archive expansion failures remain bounded.

These are required tests and review gates. None is implemented or independently verified yet. Do not describe Daryaft as secure based on these documents alone.
