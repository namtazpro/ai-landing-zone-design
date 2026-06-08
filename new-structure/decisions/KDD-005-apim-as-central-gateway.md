---
id: KDD-005
title: APIM as central gateway
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [04-solution-overview, 05-ai-platform-building-blocks, 11-management-operations]
tags: [apim, gateway, governance]
---

## Context

Without a central gateway, APIs and MCP servers are reachable through multiple paths, defeating policy enforcement, auditing, and rate limiting.

## Decision

Azure API Management (APIM) is the standard gateway for all API exposure. Backend APIs, MCP servers, and integrations funnel through APIM for policy, governance, auditing, and rate limiting.

## Consequences

- APIM is on the data path for every agent-to-tool call.
- APIM policies become the enforcement point for cost, throttling, and content safety.
- Sets up [KDD-006](KDD-006-apim-native-mcp-conversion.md) (APIM-native MCP) and [KDD-027](KDD-027-model-scaling-via-replicas-and-policies.md) (per-domain quotas).

## Source

> everything needs to be on APP...creating an API centre...one place...all the tools, agents, and everything...registry

— Sourabh and Vincent, 22 / 26 May 2026, [Microsoft Support — 22 May](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md) and [Mitie / Microsoft — 26 May](../../transcripts/Mitie_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
