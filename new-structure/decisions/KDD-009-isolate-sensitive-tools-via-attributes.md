---
id: KDD-009
title: Isolate sensitive tools via attributes
status: Tentative
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 08-security]
tags: [mcp, security, allow_tools]
---

## Context

A single MCP server typically exposes several tools at varying sensitivity levels. Removing sensitive operations from a group fragments the catalogue; leaving them exposed inflates blast radius.

## Decision

Sensitive endpoints inside a grouped MCP server use the MCP `allow_tools` attribute to restrict which agents see which tools.

## Consequences

- Tool catalogues stay coherent; sensitivity is a binding-time concern.
- Foundry Toolbox ([KDD-007](KDD-007-foundry-toolbox-as-mcp-gateway.md)) is the enforcement layer.
- Requires a per-agent catalogue of which tools are "sensitive".

## Source

> if there is a MCP server...allow tools...attribute...only this list...can be seen by this agent

— Emma Sun and Sourabh, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
