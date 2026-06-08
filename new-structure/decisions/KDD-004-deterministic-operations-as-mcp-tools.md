---
id: KDD-004
title: Deterministic operations as MCP tools
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 19-glossary-and-references]
tags: [mcp, deterministic, registry]
---

## Context

Deterministic logic (e.g. "calculate VAT") is often hand-wired into application code, creating a second integration path that bypasses the tool registry, identity model, and observability.

## Decision

All operations — deterministic or agentic — are modelled as MCP tools. Deterministic functions sit alongside autonomous agent calls in the same registry.

## Consequences

- Single discovery and governance surface for every capability.
- Deterministic tools benefit from MCP auth, validation, and tracing.
- Code that wants to call a deterministic operation goes through the same MCP plumbing as an agent.

## Source

> for the deterministic way...can be modelled as a tool within MCPs anyway...calculated VAT...you can using MCP expose as a tool

— Ha Duong, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
