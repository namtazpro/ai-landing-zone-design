---
id: KDD-002
title: MCP as universal tool exposure
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
tags: [mcp, protocol, standardisation]
---

## Context

Without a single tool protocol, every integration becomes bespoke and agent code drifts toward direct REST/SDK calls, breaking the registry and identity model.

## Decision

All tools are exposed via the Model Context Protocol (MCP). MCP is the default standard; non-MCP integration requires a documented justification.

## Consequences

- MCP becomes the surface every agent and tool must speak.
- A formal exception path is needed for non-MCP cases.
- Compliance checks (see [recommendations/kdd-compliance-in-code-reviews.md](../../recommendations/kdd-compliance-in-code-reviews.md)) can flag direct REST calls in agent definitions.

## Source

> use MCP...it needs to be...because we need to align on like a strategy that everything needs to follow this. And if it's go outside, it needs to have like a very specific reason

— Mike Agar and Francisco, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
