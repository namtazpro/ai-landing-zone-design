---
id: KDD-019
title: Per-agent billing and cost attribution
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [11-management-operations, 14-cost-model]
tags: [cost, billing, chargeback]
---

## Context

Token-based billing alone hides hosting and storage costs, blocks per-agent or per-domain chargeback, and prevents data-driven prioritisation of abstraction work.

## Decision

Track costs per agent and per domain. Combine token counts with service consumption (hosting, storage) for agent-level chargeback. Log analytics + policies for auditing.

## Consequences

- Tagging (domain, agent) is mandatory on every consuming resource.
- Cost dashboards must merge App Insights, Foundry Insights, and Azure billing.
- Justifies abstraction investments via [KDD-010](KDD-010-context-window-optimisation.md).

## Source

> we need to know which agent is consuming how much...agent-wise billing...token...consumption costs...also...hosting costs...will be account data

— Sanjay, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
