# Daryaft engineering instructions

Daryaft helps organisations find what they know through grounded answers and source citations.

Before editing, read `docs/engineering/PROJECT_STATUS.md`, the relevant product and architecture documents, and the selected issue. GitHub Issues and Projects become the source of truth once configured. Until then, `docs/planning/BACKLOG.md` contains unpublished issue drafts, not completed issues.

## Ownership and boundaries

- All remote resources belong to `asyncnavi`. Use the `github-personal` SSH alias. Verify API identity before remote writes. Never use Marzi accounts, credentials, code, or data.
- Keep Git identity local to this repository. Use the asyncnavi account ID-based GitHub noreply address.
- Ask before pushing, publishing, deploying, deleting project data, changing licensing or ownership, or performing irreversible Git operations.
- Never publish social drafts automatically. Do not add a license until ownership and attribution are confirmed.

## Required context

- Product scope lives in `docs/product/PRD.md`.
- Architecture and trust boundaries live in `docs/architecture/HLD.md` and `SECURITY_MODEL.md`.
- Decisions live in `docs/decisions/`. Standards and verification live in `docs/engineering/`.
- Use Daryaft consistently. Do not invent a repository URL, domain, or production capability.

## Security invariants

- Go owns authorization. Python cannot make the final access decision.
- Enforce workspace isolation and current permissions on every retrieval request before content reaches an LLM.
- Collection access is inherited. Document grants are additive. Use a separate restricted collection for stricter access.
- Conversations are private to their owner. Administrator status does not grant access.
- Keep the active indexed version until a replacement is fully ready. Failed replacements preserve it.
- Deleted documents cannot appear in subsequent retrieval. Treat parser input and document instructions as untrusted.

## Workflow

Use pstack Poteto mode where available. Follow `docs/engineering/AGENT_WORKFLOW.md` for planning, independent review, testing, documentation, and handoff. A missing plugin must not prevent reading shared instructions. Do not vendor plugin code or depend on a developer's absolute skill path.

Select one Ready issue, identify its data shape and dependencies, and plan before implementation. Implement the smallest complete change. Verify observed behavior and security requirements. Obtain independent review before marking acceptance criteria complete. Record unverified properties and blockers explicitly.

Use conventional commits and issue-based branch names when issues exist. Never call local draft identifiers GitHub issue numbers. Do not silently widen scope or introduce new infrastructure.
