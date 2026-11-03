# Daryaft (دریافت)
Daryaft is a Persian word meaning “understanding”, “comprehension”, “acquisition” or “the act of receiving something.”

## What it does ? 
Find what your organisation knows.

Daryaft is a planned open-source, self-hostable knowledge platform. Organisations will upload documents, organise collections, and ask questions with citations to sources they can access.

The project is in foundation work. No application services, upload flow, retrieval, or answering are implemented yet. It is not ready for production use.

Start with the [documentation index](docs/README.md), [current status](docs/engineering/PROJECT_STATUS.md), and [first-week roadmap](docs/product/ROADMAP.md).

The proposed architecture uses a Go control plane, a Python AI service, and PostgreSQL with pgvector. Authorization belongs to Go and must filter retrieval before document content reaches an LLM.

Apache-2.0 is proposed. No license has been granted yet because ownership and attribution need confirmation.
