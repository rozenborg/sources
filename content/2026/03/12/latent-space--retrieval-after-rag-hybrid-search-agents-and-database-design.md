---
title: "Retrieval After RAG: Hybrid Search, Agents, and Database Design — Simon Hørup Eskildsen of Turbopuffer"
source: latent-space
url: https://www.latent.space/p/turbopuffer
date: 2026-03-12
type: podcast
---

Turbopuffer's Simon Eskildsen identified a massive cost problem in AI infrastructure when helping Readwise build a recommendation engine that would have cost $30,000 monthly versus their $5,000 total infrastructure budget, leading him to architect a search database that goes all-in on object storage and NVMe SSDs to slash costs by 95%. The company emerged from this insight to become the search infrastructure powering companies like Cursor and Notion, betting that every company will need to connect large amounts of data to AI systems.

---

- **Origin story** - Readwise needed semantic search for article recommendations but vector search would cost $30k/month vs $5k total infrastructure spend, making the feature economically impossible to ship

- **Architecture innovation** - Built database entirely on S3 object storage with NVMe caching, eliminating consensus layers by relying on S3's 2020 strong consistency upgrade and compare-and-swap operations

- **Customer validation** - Cursor contacted them day after launch and saw 95% cost reduction while fixing per-user economics; Notion became customer despite cross-cloud latency challenges requiring dark fiber optimization

- **Market timing** - Three conditions aligned: new AI workload requiring every company to search unstructured data, new storage architecture impossible 15 years ago, and ability to support expanding query patterns over time

- **Agentic shift** - Moving from single upfront retrieval calls to agents firing many parallel queries simultaneously, requiring search infrastructure to handle burst concurrency rather than carefully chosen individual calls

- **Pricing strategy** - Reducing query costs as agentic systems dramatically increase search volume, expecting retrieval to become high-concurrency tool calls rather than sparse targeted searches

- **RAG evolution** - Hybrid retrieval combining semantic, text, regex, and SQL patterns becoming more important as coding companies still rely heavily on search despite AI advances

- **Company philosophy** - "Playing with open cards" approach including telling investor Lachy Groom they'd return money if no product-market fit by year-end, focusing on "P99 engineer" hiring standard
