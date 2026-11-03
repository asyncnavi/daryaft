# Daryaft system overview

Clients use the Go HTTP API. Go authenticates users, resolves workspace membership and grants, manages documents and conversations, and orchestrates processing jobs.

Python parses files, chunks text, creates embeddings, ranks retrieval candidates, and constructs grounded answers. Go controls which content it may access for a request.

PostgreSQL stores application records, ACLs, versions, jobs, chunks, embeddings, and conversations. Original files use a local development adapter or S3-compatible storage. Docker Compose is the planned local deployment entry point.

Redis is reserved for justified job coordination or caching. Start with durable PostgreSQL jobs unless measurement establishes a need for Redis. Next.js remains optional.

All components are planned. See [current status](../engineering/PROJECT_STATUS.md) for implementation evidence.
