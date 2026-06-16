---
id: OQ-001
title: Subscription strategy
status: Open
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [04-solution-overview, 09-resource-organization, 11-management-operations]
blocks_kdds: [KDD-016, KDD-028]
tags: [subscriptions, governance, infosec]
---

## Question

Subscription-per-domain (stronger RBAC isolation) vs current resource-group-per-domain inside shared subscriptions? Needs InfoSec and Poorna alignment.

## Why it matters

Affects RBAC blast radius, billing rollup, Azure Policy scope, and what InfoSec must approve to deviate from the established Contoso pattern.

## Resolution path

- Conversation with InfoSec and Poorna to test whether RG-per-domain inside two subscriptions remains acceptable.
- Re-open if any one domain reaches a per-subscription quota wall.

## Source

> we need to talk to other colleagues...why are we changing it

— George Smith, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
