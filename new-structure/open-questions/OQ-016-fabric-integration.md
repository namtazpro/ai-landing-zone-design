---
id: OQ-016
title: Fabric integration
status: Open
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
blocks_kdds: []
tags: [fabric, data, integration]
---

## Question

What integration pattern connects Microsoft Fabric (warehouse, ML pipelines, Fabric Data Agent) into agent workflows?

## Why it matters

Fabric is the existing analytical surface for Mitie; without a defined pattern, agents will hand-roll connections and miss the platform's governance.

## Resolution path

- Confirm Fabric Data Agent as the analytical surface (callable from Foundry agents via MCP).
- Document workspace/lakehouse access for the platform service principal.

## Source

— Touched on in the 26 May data-layer discussions; still TBD per HLD section 12.
