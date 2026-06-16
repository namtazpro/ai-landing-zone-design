---
id: KDD-027
title: Model scaling via replicas and policies
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 10-governance, 11-management-operations, 14-cost-model]
tags: [scaling, replicas, apim, models]
---

## Context

Demand for a hosted model can exceed a single deployment's quota. Without a defined scaling path, teams default to per-domain Foundry resources and lose the shared-platform benefit.

## Decision

Hub Foundry deploys multiple replicas of the same model to absorb rate-limit demand. APIM policies enforce per-domain quotas without requiring subscription-level changes.

## Consequences

- Capacity becomes a hub-team lever; domains do not provision their own Foundry to scale.
- APIM policies are the per-domain quota enforcement point ([OQ-002](../open-questions/OQ-002-rate-limiting-and-token-quota.md)).
- Reinforces [KDD-014](KDD-014-hub-spoke-for-model-deployments.md) and [KDD-015](KDD-015-model-lifecycle-control-via-hub.md).

## Source

> multiple instances even in your hub...multiple domains...deploy multiple instances...through load balancing...models...hub...rate limiting

— Vincent, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
