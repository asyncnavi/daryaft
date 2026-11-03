# First-week roadmap

This is an ambitious demonstration plan, not a production deadline. Draft IDs refer to the [unpublished backlog](../planning/BACKLOG.md). No remote issue numbers exist yet.

| Day | Target | Drafts and dependencies |
| --- | --- | --- |
| 1 | Foundation, security boundary, agent workflow, project setup. | D01 and initial D02. Remote setup depends on asyncnavi API access and repository destination. |
| 2 | Go and Python health, database connectivity, Compose and CI. | D03-D06 after contracts. |
| 3 | Tenant-aware persistence, authentication, grants, versions and jobs. | D07-D10 before retrieval or answering. |
| 4 | Upload, storage, workers, parsers and version promotion. | D11-D17 after access and persistence prerequisites. |
| 5 | Embeddings, authorized candidate queries, evaluation fixtures. | D18-D20 after active-version handling. |
| 6 | Grounded answering, deletion and private conversations. | D21-D24 after retrieval and historical-access decision. |
| 7 | Independent verification, reproducible demo and retrospective. | D25-D26 after the implemented flow passes its checks. |

## Capacity and throughput checkpoint

The backlog contains more work than one engineer can safely finish in seven ordinary working days. Re-estimate after service setup and again after the first authorized upload. Count only independently verified tickets as complete. Carry unfinished V1 work forward rather than remove security checks to meet the calendar.

Prioritize a Markdown vertical slice first. PDF and DOCX remain V1 requirements and must be labelled incomplete if they do not fit the demonstration week. Private conversations must not ship before the historical-access policy is settled. Defer the console and SDK generation.

The critical chain is contracts, runnable environment, identity and grants, upload and version state, authorized retrieval, then grounded answers. Docker availability, GitHub authorization, provider selection, parser compatibility, and independent review can delay it.
