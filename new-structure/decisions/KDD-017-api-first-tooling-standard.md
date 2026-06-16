---
id: KDD-017
title: API-first tooling standard
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations, 12-platform-automation]
tags: [api-first, mcp, apim]
---

## Context

If agents reach functions or libraries directly (no HTTP boundary), there is no policy enforcement, no auditing, and no standard way to expose those capabilities as MCP tools.

## Decision

All tools are exposed as APIs. Whether Function App, FastAPI, or native Maximo APIs, every tool becomes an endpoint. No direct agent-to-function calls — everything funnels through API → MCP.

## Consequences

- Every tool author ships an HTTP contract.
- MCP exposure (APIM-native or Foundry Toolbox) is uniform across tool implementations.
- Aligns with [KDD-005](KDD-005-apim-as-central-gateway.md) and [KDD-020](KDD-020-skip-custom-mcp-server-overhead.md).

## Source

> even if it is function up...it's still going to have an endpoint...so that endpoint...needs to be...collapsing all of that in grouping them...MCP server inside of APP

— Francisco and Sanjay, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
