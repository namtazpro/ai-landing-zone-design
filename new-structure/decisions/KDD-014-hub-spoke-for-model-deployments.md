---
id: KDD-014
title: Hub-spoke for model deployments
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [04-solution-overview, 05-ai-platform-building-blocks, 08-security, 11-management-operations]
tags: [hub-spoke, foundry, models, apim]
---

## Context

Per-domain LLM deployments multiply quota consumption, complicate retirement, and obscure who consumes which model. A shared hub solves auditing and retirement at the cost of cross-domain coupling.

## Decision

A central hub Foundry instance in a shared resource group hosts all LLM model deployments. Spoke Foundry instances in domain resource groups consume hub models via APIM. Enables once-deployed, multi-domain consumption.

## Consequences

- Single retirement and version-deprecation point ([KDD-015](KDD-015-model-lifecycle-control-via-hub.md)).
- Cross-domain rate-limit and throttling policy lives in APIM ([KDD-027](KDD-027-model-scaling-via-replicas-and-policies.md)).
- Hub becomes a tier-1 platform resource with its own SLO.

## Source

> hub RG that's got its own foundry...models...deployed...Through the IPPI gateway...catalogued and registered here...model retirements...exactly who is using 4.1

— Vincent, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
