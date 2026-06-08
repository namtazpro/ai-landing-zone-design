---
id: OQ-013
title: A2A through MCP
status: Open
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
blocks_kdds: [KDD-024]
tags: [a2a, mcp, orchestration]
---

## Question

Can an agent be invoked as a tool by another agent through MCP, or is cross-agent invocation orchestrator-only?

## Why it matters

The answer constrains whether [KDD-024](../decisions/KDD-024-cross-domain-agent-communication.md) ships as a registry feature or a MAF-Workflows feature.

## Resolution path

- Confirm Foundry support for "agent-as-MCP-tool".
- Decide whether the platform default is MCP-shaped or A2A-channel-shaped.

## Source

— Briefly mentioned in the 22 May call without decision; carried from the v0.1 HLD draft.
