---
id: KDD-015
title: Model lifecycle control via hub
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 10-governance]
tags: [model-lifecycle, governance, apim]
---

## Context

Without a centralised model-usage view, retirement and version deprecation cannot be coordinated; per-domain quotas drift; consumers of deprecated models go undetected.

## Decision

Central hub deployment enables unified control: retirement tracking, version deprecation, per-domain rate-limit capping via APIM policies, no orphaned references.

## Consequences

- Model-usage audit becomes a hub responsibility, not per-domain.
- APIM policies are the per-domain capping enforcement layer.
- Builds on [KDD-014](KDD-014-hub-spoke-for-model-deployments.md); feeds [KDD-027](KDD-027-model-scaling-via-replicas-and-policies.md).

## Source

> when...model retirements...exactly through auditing who is using 4.1...block...throttling...capping

— Vincent, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
