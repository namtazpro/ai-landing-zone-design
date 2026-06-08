---
id: KDD-013
title: One Foundry instance per domain
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
tags: [foundry, domains, isolation]
---

## Context

Mixing domains in a single Foundry instance blurs ownership, RBAC, billing rollups, and complicates lifecycle of agents/projects per business domain.

## Decision

Each business domain (EFF, HR, Sales) gets one AI Foundry instance with one Foundry project per use case.

## Consequences

- Domain becomes the unit of Foundry-resource isolation and naming.
- Per-use-case Foundry project gives clean per-agent CI/CD scope.
- Combined with [KDD-014](KDD-014-hub-spoke-for-model-deployments.md), domain instances consume hub-deployed models via APIM.

## Source

> one Foundry instance...one project per use case...one RG per domain...one instance...one project per use case

— Vincent and Sourabh, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
