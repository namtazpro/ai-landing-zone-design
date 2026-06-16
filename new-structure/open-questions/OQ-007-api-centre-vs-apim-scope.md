---
id: OQ-007
title: API Centre vs APIM scope
status: Open
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
blocks_kdds: [KDD-022]
tags: [api-centre, apim, registry]
---

## Question

What is the metadata/governance boundary between API Centre and APIM, and what is the sync model?

## Why it matters

Without a clear split, the two registries drift; reviewers cannot tell which is authoritative for any given API.

## Resolution path

- Define API Centre as the cross-cloud catalogue; APIM as the runtime gateway.
- Pick a sync model (push from APIM publish pipelines, or pull from API Centre on schedule).

## Source

— Discussion between Jacob Phan and John Blog, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md); no resolution captured.
