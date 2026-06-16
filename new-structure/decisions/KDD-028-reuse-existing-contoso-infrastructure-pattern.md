---
id: KDD-028
title: Reuse existing Contoso infrastructure pattern
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [04-solution-overview, 09-resource-organization]
tags: [subscriptions, contoso, infosec]
---

## Context

Re-opening the subscription model purely for the agentic platform would force an InfoSec review already settled for the existing Contoso topology, with no AI-specific driver to justify it.

## Decision

Keep the current Contoso pattern (non-prod + prod subscriptions, resource groups per domain). Do not restructure to subscription-per-domain unless InfoSec mandates it.

## Consequences

- Subscription strategy stays out of v1 scope (see [OQ-001](../open-questions/OQ-001-subscription-strategy.md)).
- RG-per-domain ([KDD-016](KDD-016-domain-isolated-resource-groups.md)) carries the isolation responsibility for now.
- Re-evaluation triggers: InfoSec mandate or a domain reaching the per-subscription quota ceiling.

## Source

> how we work today...InfoSec must have agreed...it's already working...this is not...AI...way Contoso decided

— George Smith and John Blog, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
