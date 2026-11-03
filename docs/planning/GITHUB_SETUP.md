# GitHub setup plan

All resources belong to asyncnavi. The public repository is [asyncnavi/daryaft](https://github.com/asyncnavi/daryaft). No Project, label, milestone, or issue has been created in this run.

## Prerequisites

Verify API identity is asyncnavi before every setup session. SSH authenticates as asyncnavi through github-personal, but that does not supply API access. The current CLI has only Marzi accounts. Do not use those tokens for writes.

The user authorized public repository creation and the initial push. The repository was created through the authenticated asyncnavi browser session. Obtain appropriate repository and Project API permissions. Existing Project inspection failed under the current token because read:project was missing.

## Reconcile existing resources

List existing repository labels, milestones, issues, linked Projects and user Projects before writing. Match exact names and issue intent. Update missing fields deliberately rather than duplicate objects. Record actual URLs and issue numbers after creation.

Use these Project statuses in order: Backlog, Ready, In Progress, In Review, Blocked, Done. Ready requires clear acceptance criteria and satisfied dependencies. Done requires independent verification. Use GitHub's completed state for Done and inspect field capabilities before creating options.

Create missing milestones M0 — Project Foundation, M1 — Document Ingestion, M2 — Retrieval and RAG, M3 — Workspace and ACL, M4 — Developer Experience, and M5 — Public Beta.

Create missing labels:

- type:feature, type:bug, type:chore, type:docs, type:research, type:security, type:testing.
- priority:p0, priority:p1, priority:p2.
- area:backend, area:ai, area:frontend, area:infra, area:devex, area:security, area:docs.
- status:ready, status:blocked, status:needs-review.

Publish reviewed backlog drafts as issues with the supplied task fields. Preserve draft-to-issue mapping in this file and replace roadmap references with actual links. Keep this document as setup history, not a competing progress tracker. GitHub becomes the source of truth once available.
