---
id: KDD-016
title: Domain-isolated resource groups
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [04-solution-overview, 09-resource-organization, 11-management-operations]
tags: [resource-groups, naming, isolation]
---

## Context

A shared subscription needs an internal partitioning model so that domains can be billed, governed, and access-controlled without owning their own subscriptions yet.

## Decision

Resource groups are created per domain per environment (for example `EFF-Dev`, `EFF-Test`, `HR-Prod`). Enables domain-based billing rollup and RBAC isolation within a subscription.

## Consequences

- RG naming standard is part of platform onboarding.
- Cost reports roll up by RG = domain.
- Tightly coupled to [KDD-028](KDD-028-reuse-existing-contoso-infrastructure-pattern.md); reviewed by [OQ-001](../open-questions/OQ-001-subscription-strategy.md).

## Source

> one subscription...non-product...within that...dev and test per domain resource group...dev...test not product...prod subscription

— Sanjay, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
