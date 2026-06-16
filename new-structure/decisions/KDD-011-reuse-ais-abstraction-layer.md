---
id: KDD-011
title: Reuse AIS abstraction layer
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
tags: [ais, abstraction, mcp]
---

## Context

The existing AIS API orchestration layer (logic apps + functions) already groups several backend APIs. Building parallel custom MCP servers would duplicate that work and split governance.

## Decision

Reuse the existing AIS API orchestration layer (logic apps + functions) for any API grouping/abstraction. Do not build separate custom MCP servers if AIS already covers the abstraction.

## Consequences

- AIS becomes a first-class source of MCP-exposable abstractions.
- Custom MCP servers are reserved for cases AIS does not cover.
- Reinforces [KDD-012](KDD-012-maximise-work-not-done.md) and [KDD-020](KDD-020-skip-custom-mcp-server-overhead.md).

## Source

> you already have...an abstraction...then you can...expose as MCP...don't have to do further if you need...then you build it yourself

— George Smith and Jacob Phan, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
