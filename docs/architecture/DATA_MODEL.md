# Daryaft proposed data model

This is a conceptual schema, not a migration.

| Entity | Ownership and invariants |
| --- | --- |
| User | Global identity, with separately scoped workspace memberships. |
| Workspace | Tenant root. |
| Membership | Unique workspace and user pair, with role and active state. |
| Group and group membership | Workspace-scoped. Group members must belong to that workspace. |
| Collection | Workspace-scoped library boundary. |
| Collection grant | Workspace-scoped user or group principal with explicit capability. |
| Document | Workspace and collection, deletion timestamp, active version pointer. |
| Document grant | Additive user or group capability within the same workspace. |
| Document version | Immutable original reference, processing state, parser and embedding metadata. |
| Chunk | Workspace, document version, ordinal, text, and source locator. |
| Embedding | Chunk, model identity, dimensions, and vector. Never compare incompatible models. |
| Job | Workspace, version, kind, lease, attempts, next attempt, and safe failure code. |
| Conversation | Workspace and owning user. No implicit administrator read. |
| Message | Conversation, role, text, citation references, and usage metadata. |
| Audit event | Actor, workspace, action, resource, outcome, timestamp, and request ID. |

Use composite foreign keys or equivalent constraints to reject cross-workspace relationships. Choose identifier format and exact SQL types in the schema ticket. An absent grant denies access. Workspace roles must not imply private-conversation access.

Store active-version selection separately from attempted-version state. Initial upload has no active version until indexing succeeds. A replacement attempt can fail while the document remains searchable through its active version.

Citations refer to immutable version and chunk IDs plus source locators. Reading cited content requires current access. Historical conversation answers may contain previously authorized material. The retention and revocation behavior for that history needs an explicit product decision before conversation persistence ships.
