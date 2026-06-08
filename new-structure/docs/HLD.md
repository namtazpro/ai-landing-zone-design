# PRIO Agentic Platform — High-Level Design (HLD)

| Field | Value |
| --- | --- |
| Status | Draft |
| Version | 0.2 (ALZ-aligned restructure) |
| Last updated | 2026-06-08 |
| Source baseline | [20260514 Agentic platform_vF.pptx](../../20260514%20Agentic%20platform_vF.pptx) (14 May 2026) |
| Decision log | [decisions/](../decisions/) (28 KDDs) |
| Open questions | [open-questions/](../open-questions/) (20 OQs) |
| Transcripts | [transcripts/](../../transcripts/) |
| Compliance recommendations | [recommendations/kdd-compliance-in-code-reviews.md](../../recommendations/kdd-compliance-in-code-reviews.md) |

This HLD aligns the PRIO Agentic Platform to the Azure Landing Zone (ALZ) design-area model. Each section either restates a decided position (with KDD references) or flags a gap to be filled in subsequent revisions. The previous flat draft survives unchanged at the repository root as [HLD.md](../../HLD.md); this version is the working artefact going forward.

---

## 1. Introduction and business context

The PRIO Agentic Platform is the Azure target architecture for delivering agent-driven use cases for the Mitie / Microsoft engagement. It standardises how agents are defined, how tools are exposed, how workflows are orchestrated, and how the platform is secured, observed, and shipped through CI/CD. The platform is multi-tenant by domain (for example EFF, HR, Sales), Foundry-centred, and built on Microsoft Agent Framework as the orchestrator.

The platform serves three audiences: app teams building domain-specific agents, the central platform team operating shared services, and governance/security stakeholders enforcing enterprise policy.

---

## 2. Scope, assumptions, constraints

In scope:

- Agent and tool definition, registration, versioning, and CI/CD.
- Orchestration of single-agent and multi-agent workflows including human-in-the-loop (HITL).
- Frontend and backend application layers that expose agents to internal and external users.
- Identity, authorisation, observability, data, and integration patterns.

Out of scope (for v1):

- Multi-region failover topology — see [OQ-004](../open-questions/OQ-004-multi-region-failover.md).
- Fabric data plane integration — see [OQ-016](../open-questions/OQ-016-fabric-integration.md).

Key assumptions:

- The existing Mitie subscription pattern (non-prod + prod, resource-groups per domain) is reused — see [KDD-028](../decisions/KDD-028-reuse-existing-mighty-infrastructure-pattern.md).
- One AI Foundry instance per business domain, with one Foundry project per use case — see [KDD-013](../decisions/KDD-013-one-foundry-instance-per-domain.md).
- Microsoft Entra ID is the enterprise identity authority.

---

## 3. Stakeholders and personas

> Gap section — placeholder. Populate with the personas the platform serves and the responsibilities each carries. Current intent:
>
> - Platform team — owns shared services (hub Foundry, APIM, Toolbox, observability, IaC modules).
> - Domain app teams — author agents, tools, and prompts in their domain spoke.
> - Data scientists / prompt engineers — own evaluations, golden datasets, prompt iterations.
> - Governance — InfoSec, FinOps, compliance reviewers.
> - End users — Mitie internal and external consumers of agent-enabled experiences.
>
> TODO: confirm persona list with stakeholders; tie each persona to expected RBAC roles in section 6.

---

## 4. Solution overview

External and internal users reach the platform through a Web Application Firewall and Application Gateway, authenticate with Microsoft Entra ID, and land on a Next.js frontend hosted on Azure Container Apps. The frontend calls a FastAPI backend, also on Container Apps, which acts as the ingestion and orchestration entry point. The backend invokes the Microsoft Agent Framework orchestration layer, which runs Foundry-hosted agents that consume tools exposed via Azure API Management (APIM) — preferably as MCP servers — and downstream systems such as Maximo (over APIM), SQL Server, Azure Data Lake, and Storage Accounts. Azure Managed Redis carries transient session and workflow state.

Three Entra ID authentication layers are present: user-facing (Entra ID Protection), backend-to-agent (managed identities), and agent-to-tool (per-agent Entra identity with OAuth/OBO). Section 6 expands the identity model.

> Diagram placeholder — see [assets/diagrams/hld/](../assets/diagrams/hld/). TODO: replace deck slide with an HLD-grade logical view.

Decisions: [KDD-005](../decisions/KDD-005-apim-as-central-gateway.md), [KDD-014](../decisions/KDD-014-hub-spoke-for-model-deployments.md), [KDD-016](../decisions/KDD-016-domain-isolated-resource-groups.md), [KDD-028](../decisions/KDD-028-reuse-existing-mighty-infrastructure-pattern.md). Open: [OQ-001](../open-questions/OQ-001-subscription-strategy.md), [OQ-004](../open-questions/OQ-004-multi-region-failover.md), [OQ-005](../open-questions/OQ-005-hub-foundry-instance-count.md).

---

## 5. AI platform building blocks

### 5.1 Foundry and Azure OpenAI footprint

- A central hub Foundry instance in a shared resource group hosts all LLM model deployments. Spoke Foundry instances in domain resource groups consume hub models via APIM. See [KDD-014](../decisions/KDD-014-hub-spoke-for-model-deployments.md).
- Centralised hub gives one place for retirement tracking, version deprecation, and per-domain rate-limit capping. See [KDD-015](../decisions/KDD-015-model-lifecycle-control-via-hub.md).
- Scaling absorbs demand via multiple replicas of the same model in the hub plus APIM load-balancing/quota policies, instead of per-domain Foundry duplication. See [KDD-027](../decisions/KDD-027-model-scaling-via-replicas-and-policies.md).
- One AI Foundry instance per business domain (EFF, HR, Sales) with one Foundry project per use case. See [KDD-013](../decisions/KDD-013-one-foundry-instance-per-domain.md).

Open: [OQ-002](../open-questions/OQ-002-rate-limiting-and-token-quota.md), [OQ-005](../open-questions/OQ-005-hub-foundry-instance-count.md).

### 5.2 Agentic platform

**Conceptual primitives.** The platform composes four primitives: agent, tool, deterministic step, workflow. Deterministic operations are modelled as MCP tools so they sit in the same registry as agentic capabilities ([KDD-004](../decisions/KDD-004-deterministic-operations-as-mcp-tools.md)). Skills and MCP tools are distinct primitives — skills encode workflows the agent should follow; MCP exposes external systems the agent can invoke ([KDD-023](../decisions/KDD-023-skill-vs-mcp-tool-framework.md)). See section 19 for full definitions.

**Agent definition and versioning.** Agents are defined in YAML and deployed through a standard provision script and CI/CD pipeline (section 12). Foundry owns version registry and rollback. The Foundry agent YAML schema fields are:

| Field | Purpose | Example |
| --- | --- | --- |
| `kind` | Asset type. | `prompt` |
| `name` | Unique identifier. | `research-agent` |
| `model` | Model deployment. | `gpt-4.1` |
| `temperature` | Determinism control. | `0.2` |
| `instructions` | Role and task instructions. | `"You are an investment research assistant..."` |
| `tools` | External tools / APIs. | MCP server for SAP data |
| `text` | Structured-output JSON schema. | JSON schema |

**Tool registry.** Tools are exposed via the Model Context Protocol (MCP). MCP is the default standard; non-MCP integration requires a documented exception ([KDD-002](../decisions/KDD-002-mcp-as-universal-tool-exposure.md)). Tools are categorised and grouped by functionality ([KDD-001](../decisions/KDD-001-tool-registry-and-categorisation.md)) and by user intent or business operation, not by source system or 1:1 with APIs ([KDD-003](../decisions/KDD-003-no-1to1-api-to-mcp-mapping.md), [KDD-008](../decisions/KDD-008-group-tools-by-intent-not-by-system.md)).

Two layers of MCP exposure exist:

1. **APIM-native MCP** — Azure API Management exposes OpenAPI specs directly as MCP servers (Terraform-deployable, validated by working demo). See [KDD-006](../decisions/KDD-006-apim-native-mcp-conversion.md), [KDD-020](../decisions/KDD-020-skip-custom-mcp-server-overhead.md).
2. **Foundry Toolbox** — a second-layer MCP gateway above APIM that handles agent-specific filtering, versioning, and selective exposure of tools to individual agents. See [KDD-007](../decisions/KDD-007-foundry-toolbox-as-mcp-gateway.md).

Abstraction strategy follows "maximise work not done": v1 ships 1:1 API→MCP exposure through APIM. Custom abstraction (for example collapsing 14 granular Maximo APIs into 7 intent-driven operations) is introduced only when context-window or accuracy pain is measured. Evidence from internal trials: abstracted grouping cut tool count by ~50%, tokens by ~30%, and improved latency and success rate. See [KDD-010](../decisions/KDD-010-context-window-optimisation.md), [KDD-012](../decisions/KDD-012-maximise-work-not-done.md), [KDD-025](../decisions/KDD-025-maximo-api-abstraction-example.md), [KDD-026](../decisions/KDD-026-no-blanket-abstraction-requirement.md). The existing AIS API orchestration layer (logic apps + functions) is reused for grouping/abstraction wherever it already exists; custom MCP servers are only introduced when AIS does not already cover the abstraction ([KDD-011](../decisions/KDD-011-reuse-ais-abstraction-layer.md)). Every tool — including Function App, FastAPI, or native Maximo — exposes an HTTP endpoint and routes through APIM and MCP ([KDD-017](../decisions/KDD-017-api-first-tooling-standard.md)).

Sensitive tools inside a grouped MCP server are isolated using the MCP `allow_tools` attribute so individual agents only see what they are authorised to call ([KDD-009](../decisions/KDD-009-isolate-sensitive-tools-via-attributes.md)).

**Agent communication.** Communication is standardised on three layers:

- **Foundry runtime** — Foundry agents are invoked through the Azure AI Foundry Agent Framework runtime.
- **A2A (Agent-to-Agent)** — interoperable communication, delegation, and handoffs across distributed agents. Cross-domain agent calls are allowed ([KDD-024](../decisions/KDD-024-cross-domain-agent-communication.md)); domain boundaries govern access control, not communication.
- **MCP** — standardises tool access, context sharing, and external capability integration. Non-Azure systems (for example SAP via CPI) are registered in APIM and exposed as MCP servers ([KDD-021](../decisions/KDD-021-cpi-sap-integration-via-mcp.md)). API Centre (distinct from APIM) is the multi-cloud metadata registry ([KDD-022](../decisions/KDD-022-api-centre-as-separate-registry.md)).

**Orchestration: Microsoft Agent Framework.** MAF is the orchestration substrate. Component summary:

| Component | Responsibility |
| --- | --- |
| Orchestrator | Pro-code, production-grade foundation. |
| Single agent | Foundry agent invoked through `.run()`. |
| Sequential workflow | `SequentialBuilder` for simple flows; `WorkflowBuilder` for typed executors and conditional routing. |
| Group chat | `GroupChatBuilder(participants=[...], max_rounds=10).build()`. |
| HITL | Workflow pauses until user provides feedback. |

MAF coexists with traditional orchestration (Logic Apps, Azure Data Factory) which remains the right choice for deterministic, long-running, asynchronous workflows and rich enterprise connectors. The split is not exclusive: deterministic backbones may invoke agentic steps and vice versa ([KDD-018](../decisions/KDD-018-orchestration-layer-separation.md)). Formal selection criteria are still pending ([OQ-011](../open-questions/OQ-011-maf-vs-logic-apps-selection-criteria.md)).

### 5.3 Data and RAG plane

| Concern | Decision |
| --- | --- |
| Operational data | SQL Server is the system of record for operational business data. |
| Knowledge base | Azure AI Search index (vector + semantic ranker) populated by an indexer skillset over blob/SharePoint, wrapped as a Foundry Knowledge Base object exposing an MCP URL. Agents autonomously call `knowledge_base_retrieve` when needed. |
| Agent / workflow context | Per-agent session memory in Foundry; workflow-shared state via `ctx.set_state(key, value)` / `ctx.get_state(key)`. |
| Persistent storage | SQL Server, Storage Accounts, Mitie Azure Data Lake. |
| Fabric data connection | TBD — see [OQ-016](../open-questions/OQ-016-fabric-integration.md). |

Open: [OQ-015](../open-questions/OQ-015-sql-knowledge-base-access-path.md), [OQ-016](../open-questions/OQ-016-fabric-integration.md).

### 5.4 Tooling and developer experience

Four layers compose end-to-end flow:

1. **Ingestion** — APIs validate inbound requests from external sources (email, apps) and route them into orchestration.
2. **Orchestration** — Microsoft Agent Framework coordinates execution, manages workflow state, and handles HITL pauses.
3. **Agent and tool** — Agents execute tasks against tools registered with MCP servers.
4. **Persistence and state** — Workflow state, job status, and results land in SQL Server for reliability and resumability.

Developer experience leans on platform templates (MAF agent scaffolds, Foundry YAML templates, Terraform module catalogue) and standard CI/CD pipelines (section 12).

---

## 6. Identity and access management

> Gap section — populates from current §13 identity content. Working position:
>
> - **Per-agent Entra identity.** Each Foundry-hosted agent receives a dedicated Microsoft Entra ID identity at deployment, platform-managed, with no stored secrets.
> - **Managed authentication.** When an agent invokes a tool, Foundry performs an OAuth token exchange with Entra ID and retrieves a scoped access token. Token lifecycle is platform-managed.
> - **Delegated / OBO.** OAuth On-Behalf-Of flows let agents access user-specific resources with the user's delegated permissions.
> - **RBAC.** Access to MCP tools, Azure resources, and external systems is governed by RBAC assignments tied to the agent identity, scoped per agent.
>
> TODO: confirm per-agent identity remains the default vs shared service principals for some scenarios — [OQ-014](../open-questions/OQ-014-per-agent-identity-vs-shared-sp.md). Document role catalogue per persona (section 3).

---

## 7. Network topology and connectivity

> Gap section — placeholder. Working intent:
>
> - Adopt the ALZ hub-and-spoke topology. Shared services (APIM, hub Foundry, Toolbox, observability, DNS, Private DNS zones) live in the hub; domain spokes hold agents, tools, and data.
> - All platform traffic uses private endpoints where the resource supports it; public exposure is limited to the Application Gateway / WAF in front of the user-facing frontend.
> - Egress through a controlled path (NVA or Azure Firewall, TBD) for outbound traffic from agents to external systems (such as SAP CPI in [KDD-021](../decisions/KDD-021-cpi-sap-integration-via-mcp.md)).
> - APIM placement and DNS naming convention to be defined.
>
> TODO: confirm hub-spoke ALZ alignment, document IP-range plan, and specify private endpoint scope per resource type.

---

## 8. Security

- **MCP server authentication.** MCP servers validate incoming Entra ID JWTs (issuer, audience, signature) and check the agent's client/object ID against allow-lists or roles to authorise the requested tool. JWT validation profile to be standardised — see [OQ-019](../open-questions/OQ-019-mcp-server-jwt-validation.md).
- **Sensitive tool isolation.** MCP `allow_tools` restricts which agents see which tools inside a grouped MCP server. See [KDD-009](../decisions/KDD-009-isolate-sensitive-tools-via-attributes.md).
- **Hub-side controls.** Hub Foundry consumption is throttled and capped per domain via APIM policies, preventing one domain from starving another ([KDD-014](../decisions/KDD-014-hub-spoke-for-model-deployments.md), [KDD-027](../decisions/KDD-027-model-scaling-via-replicas-and-policies.md)).
- **Per-agent identity, OAuth/OBO, RBAC.** See section 6.

> TODO: complete the section with content-safety stance (Azure AI Content Safety), prompt-injection mitigations, secrets management policy, and data-classification per data store.

Open: [OQ-014](../open-questions/OQ-014-per-agent-identity-vs-shared-sp.md), [OQ-019](../open-questions/OQ-019-mcp-server-jwt-validation.md).

---

## 9. Resource organization

Working layout (carried forward from the current Mitie pattern):

- **Subscriptions.** Two subscriptions — non-prod (dev + test) and prod. No subscription-per-domain split today; see [OQ-001](../open-questions/OQ-001-subscription-strategy.md).
- **Resource groups.** One per domain per environment (for example `EFF-Dev`, `EFF-Test`, `HR-Prod`). See [KDD-016](../decisions/KDD-016-domain-isolated-resource-groups.md), [KDD-028](../decisions/KDD-028-reuse-existing-mighty-infrastructure-pattern.md).
- **Shared hub.** One additional shared resource group hosts the hub Foundry and shared platform services (APIM, Toolbox, observability) — see [KDD-014](../decisions/KDD-014-hub-spoke-for-model-deployments.md).

> TODO: confirm management-group placement, naming convention (per Mitie standard), and tagging schema (domain, environment, agent, cost-centre).

Decisions: [KDD-013](../decisions/KDD-013-one-foundry-instance-per-domain.md), [KDD-016](../decisions/KDD-016-domain-isolated-resource-groups.md), [KDD-028](../decisions/KDD-028-reuse-existing-mighty-infrastructure-pattern.md). Open: [OQ-001](../open-questions/OQ-001-subscription-strategy.md), [OQ-003](../open-questions/OQ-003-domain-definition-logic.md).

---

## 10. Governance

> Gap section — placeholder. Working intent:
>
> - **Azure Policy.** Enforce tagging, region allow-list, and SKU constraints across all subscriptions.
> - **Content safety and responsible AI.** Set guardrail policies per agent at deployment time.
> - **Model lifecycle approval.** Hub-side approval gate for new model deployments and retirement notifications ([KDD-015](../decisions/KDD-015-model-lifecycle-control-via-hub.md)).
> - **Per-domain capping via APIM.** Quota policies prevent unbounded consumption of hub models ([KDD-027](../decisions/KDD-027-model-scaling-via-replicas-and-policies.md), [OQ-002](../open-questions/OQ-002-rate-limiting-and-token-quota.md)).
> - **KDD compliance in code reviews.** See the dedicated [recommendations/kdd-compliance-in-code-reviews.md](../../recommendations/kdd-compliance-in-code-reviews.md).
>
> TODO: write Azure Policy assignment plan and content-safety baseline.

---

## 11. Management and operations

- **Traces.** Application Insights is the single sink for agent and workflow traces, including input, output, token usage, and event runtime.
- **Live dashboards.** App Insights provides cross-platform dashboards for error rates by tool/model, run counts, and token consumption. Foundry adds agent-level dashboards for cost, token usage, error rates, and run volumes.
- **Agent evaluation.**
  - Offline: ground truth saved in blob storage and registered in Foundry; the `evaluate()` function runs custom evaluators per agent.
  - Online: Foundry built-in evaluators cover relevance, coherence, grounding, and similar metrics.
- **Cost surfacing.** Per-agent and per-domain views combine token counts with hosting/service consumption — see [KDD-019](../decisions/KDD-019-per-agent-billing-and-cost-attribution.md) and section 14.
- **Topology.** Hub-spoke for model deployments ([KDD-014](../decisions/KDD-014-hub-spoke-for-model-deployments.md)); one Foundry per domain ([KDD-013](../decisions/KDD-013-one-foundry-instance-per-domain.md)); cross-domain agent calls allowed through the shared registry ([KDD-024](../decisions/KDD-024-cross-domain-agent-communication.md)).

Decisions: [KDD-005](../decisions/KDD-005-apim-as-central-gateway.md), [KDD-007](../decisions/KDD-007-foundry-toolbox-as-mcp-gateway.md), [KDD-011](../decisions/KDD-011-reuse-ais-abstraction-layer.md), [KDD-013](../decisions/KDD-013-one-foundry-instance-per-domain.md), [KDD-014](../decisions/KDD-014-hub-spoke-for-model-deployments.md), [KDD-016](../decisions/KDD-016-domain-isolated-resource-groups.md), [KDD-017](../decisions/KDD-017-api-first-tooling-standard.md), [KDD-019](../decisions/KDD-019-per-agent-billing-and-cost-attribution.md), [KDD-021](../decisions/KDD-021-cpi-sap-integration-via-mcp.md), [KDD-022](../decisions/KDD-022-api-centre-as-separate-registry.md), [KDD-024](../decisions/KDD-024-cross-domain-agent-communication.md), [KDD-025](../decisions/KDD-025-maximo-api-abstraction-example.md), [KDD-027](../decisions/KDD-027-model-scaling-via-replicas-and-policies.md). Open: [OQ-002](../open-questions/OQ-002-rate-limiting-and-token-quota.md), [OQ-003](../open-questions/OQ-003-domain-definition-logic.md), [OQ-004](../open-questions/OQ-004-multi-region-failover.md), [OQ-005](../open-questions/OQ-005-hub-foundry-instance-count.md), [OQ-012](../open-questions/OQ-012-foundry-dashboard-scope.md), [OQ-015](../open-questions/OQ-015-sql-knowledge-base-access-path.md).

---

## 12. Platform automation and DevOps

**Agent CI/CD.** PR validation (every stage blocking before merge): source checkout → YAML schema validation → lint (naming, required fields, model whitelist) → eval tests (golden prompts, regression checks) → security scan (secrets, dependency audit). Deployment (merge-triggered): package agent definitions; resolve semver from git tag → push artefact to ACR/blob → source branch routing (`dev` branch → dev project; `main`/`release` → prod project) → manual approval gate → deploy to Foundry project → register version in Foundry registry → post-deploy verification (smoke prompts, OTel signals, alerts armed, one-click rollback). Gate specifics still pending — see [OQ-010](../open-questions/OQ-010-agent-cicd-gates-and-foundry-versioning.md).

**Backend microservice (FastAPI, Container Apps).** PR gates: `uv sync --frozen` → `ruff` + `mypy` → `pytest ≥ 90%` → SAST + dep audit. Deployment: semver package → ACR push → manual gate → dev/prod env → container startup runs `alembic upgrade head` then `uvicorn` → health/Postman/OTel verification + one-click rollback. See [OQ-018](../open-questions/OQ-018-backend-cicd-detail.md).

**Frontend (Next.js, Container Apps).** PR gates: `npm ci` + `next build` → ESLint + Prettier + `tsc` → Jest ≥ 70% → SAST + dep audit. Deployment: Docker build from base image with `cosign` signing → ACR push → manual gate → dev/prod env → Next.js boot → health/smoke/OTel verification + rollback. See [OQ-017](../open-questions/OQ-017-frontend-cicd-detail.md).

**Base image CI/CD.** Deck slide 18 ("CI/CD – Base Image") was title-only in the source XML.

> TODO: fill from PowerPoint slide notes when accessible.

**IaC.** Terraform-driven modules for Foundry, APIM (including native-MCP exposure), and shared services. APIM-native-MCP module pending ([OQ-009](../open-questions/OQ-009-terraform-pattern-for-apim-native-mcp.md)). Custom FastMCP hosting choice pending ([OQ-020](../open-questions/OQ-020-functions-vs-container-apps-for-fastmcp.md)).

Decisions: [KDD-006](../decisions/KDD-006-apim-native-mcp-conversion.md), [KDD-017](../decisions/KDD-017-api-first-tooling-standard.md), [KDD-020](../decisions/KDD-020-skip-custom-mcp-server-overhead.md). Open: [OQ-009](../open-questions/OQ-009-terraform-pattern-for-apim-native-mcp.md), [OQ-010](../open-questions/OQ-010-agent-cicd-gates-and-foundry-versioning.md), [OQ-017](../open-questions/OQ-017-frontend-cicd-detail.md), [OQ-018](../open-questions/OQ-018-backend-cicd-detail.md), [OQ-020](../open-questions/OQ-020-functions-vs-container-apps-for-fastmcp.md).

---

## 13. Business continuity

> Gap section — placeholder. Working intent:
>
> - Pick the Azure region pair (likely UK South / UK West).
> - Define RPO/RTO targets per service tier (frontend, backend, agents, hub Foundry).
> - Hub-Foundry failover strategy and model-deployment portability.
> - Stateful component recovery (SQL Server, Managed Redis, Storage).
>
> TODO: confirm availability targets — [OQ-004](../open-questions/OQ-004-multi-region-failover.md) — then design failover topology accordingly.

---

## 14. Cost model

> Gap section — placeholder. Working intent:
>
> - **Cost drivers.** Model token spend (hub Foundry), APIM, Container Apps, Application Insights, storage, Managed Redis.
> - **Per-domain attribution.** Tag every resource with `domain` and `environment`; cost queries roll up by tag.
> - **Per-agent attribution.** Combine token counts with hosting cost — see [KDD-019](../decisions/KDD-019-per-agent-billing-and-cost-attribution.md).
> - **Budgeting.** Azure Budgets per domain; alerts at 50% / 80% / 100%.
> - **Token budgeting.** Per-agent prompt-and-completion limits enforced by APIM policies.
>
> TODO: define cost dashboard structure and link to FinOps stakeholders.

---

## 15. Cross-cutting concerns and WAF review

> Gap section — placeholder. One subsection per WAF pillar:
>
> - **Reliability.** SLO targets; pending [OQ-004](../open-questions/OQ-004-multi-region-failover.md).
> - **Security.** Section 6, section 8; pending [OQ-014](../open-questions/OQ-014-per-agent-identity-vs-shared-sp.md), [OQ-019](../open-questions/OQ-019-mcp-server-jwt-validation.md).
> - **Cost optimisation.** Section 14.
> - **Operational excellence.** Section 11, section 12.
> - **Performance efficiency.** Context-window optimisation ([KDD-010](../decisions/KDD-010-context-window-optimisation.md)); model scaling ([KDD-027](../decisions/KDD-027-model-scaling-via-replicas-and-policies.md)).
>
> TODO: complete the formal WAF assessment with scores per pillar.

---

## 16. Key Design Decisions (KDDs)

Each KDD lives as its own file under [decisions/](../decisions/) with full context, decision text, consequences, and a verbatim source quote. Lifecycle and supersession rules are defined in the platform conventions (see [README](../README.md)).

| ID | Title | Status | New HLD sections |
| --- | --- | --- | --- |
| [KDD-001](../decisions/KDD-001-tool-registry-and-categorisation.md) | Tool registry and categorisation | Decided | 5 |
| [KDD-002](../decisions/KDD-002-mcp-as-universal-tool-exposure.md) | MCP as universal tool exposure | Decided | 5 |
| [KDD-003](../decisions/KDD-003-no-1to1-api-to-mcp-mapping.md) | No 1:1 API-to-MCP mapping | Decided | 5 |
| [KDD-004](../decisions/KDD-004-deterministic-operations-as-mcp-tools.md) | Deterministic operations as MCP tools | Decided | 5, 19 |
| [KDD-005](../decisions/KDD-005-apim-as-central-gateway.md) | APIM as central gateway | Decided | 4, 5, 11 |
| [KDD-006](../decisions/KDD-006-apim-native-mcp-conversion.md) | APIM-native MCP conversion | Decided | 5, 12 |
| [KDD-007](../decisions/KDD-007-foundry-toolbox-as-mcp-gateway.md) | Foundry Toolbox as MCP gateway | Decided | 5, 11 |
| [KDD-008](../decisions/KDD-008-group-tools-by-intent-not-by-system.md) | Group tools by intent, not by system | Decided | 5 |
| [KDD-009](../decisions/KDD-009-isolate-sensitive-tools-via-attributes.md) | Isolate sensitive tools via attributes | Tentative | 5, 8 |
| [KDD-010](../decisions/KDD-010-context-window-optimisation.md) | Context-window optimisation | Decided | 5 |
| [KDD-011](../decisions/KDD-011-reuse-ais-abstraction-layer.md) | Reuse AIS abstraction layer | Decided | 5, 11 |
| [KDD-012](../decisions/KDD-012-maximise-work-not-done.md) | Maximise work not done | Decided | 5 |
| [KDD-013](../decisions/KDD-013-one-foundry-instance-per-domain.md) | One Foundry instance per domain | Decided | 5, 11 |
| [KDD-014](../decisions/KDD-014-hub-spoke-for-model-deployments.md) | Hub-spoke for model deployments | Decided | 4, 5, 8, 11 |
| [KDD-015](../decisions/KDD-015-model-lifecycle-control-via-hub.md) | Model lifecycle control via hub | Decided | 5, 10 |
| [KDD-016](../decisions/KDD-016-domain-isolated-resource-groups.md) | Domain-isolated resource groups | Decided | 4, 9, 11 |
| [KDD-017](../decisions/KDD-017-api-first-tooling-standard.md) | API-first tooling standard | Decided | 5, 11, 12 |
| [KDD-018](../decisions/KDD-018-orchestration-layer-separation.md) | Orchestration layer separation | Decided | 5 |
| [KDD-019](../decisions/KDD-019-per-agent-billing-and-cost-attribution.md) | Per-agent billing and cost attribution | Decided | 11, 14 |
| [KDD-020](../decisions/KDD-020-skip-custom-mcp-server-overhead.md) | Skip custom MCP server overhead | Decided | 5, 12 |
| [KDD-021](../decisions/KDD-021-cpi-sap-integration-via-mcp.md) | CPI / SAP integration via MCP | Tentative | 5, 11 |
| [KDD-022](../decisions/KDD-022-api-centre-as-separate-registry.md) | API Centre as separate registry | Tentative | 5, 11 |
| [KDD-023](../decisions/KDD-023-skill-vs-mcp-tool-framework.md) | Skill vs MCP tool framework | Tentative | 5, 19 |
| [KDD-024](../decisions/KDD-024-cross-domain-agent-communication.md) | Cross-domain agent communication | Decided | 5, 11 |
| [KDD-025](../decisions/KDD-025-maximo-api-abstraction-example.md) | Maximo API abstraction example | Decided | 5, 11 |
| [KDD-026](../decisions/KDD-026-no-blanket-abstraction-requirement.md) | No blanket abstraction requirement | Decided | 5 |
| [KDD-027](../decisions/KDD-027-model-scaling-via-replicas-and-policies.md) | Model scaling via replicas and policies | Decided | 5, 10, 11, 14 |
| [KDD-028](../decisions/KDD-028-reuse-existing-mighty-infrastructure-pattern.md) | Reuse existing Mighty infrastructure pattern | Decided | 4, 9 |

---

## 17. Open questions and risks

Each open question lives as its own file under [open-questions/](../open-questions/) with the full context, why-it-matters narrative, resolution path, and source attribution.

| ID | Title | Status | New HLD sections |
| --- | --- | --- | --- |
| [OQ-001](../open-questions/OQ-001-subscription-strategy.md) | Subscription strategy | Open | 4, 9, 11 |
| [OQ-002](../open-questions/OQ-002-rate-limiting-and-token-quota.md) | Rate limiting and token quota | Open | 10, 11 |
| [OQ-003](../open-questions/OQ-003-domain-definition-logic.md) | Domain definition logic | Open | 11 |
| [OQ-004](../open-questions/OQ-004-multi-region-failover.md) | Multi-region failover | Open | 4, 11, 13 |
| [OQ-005](../open-questions/OQ-005-hub-foundry-instance-count.md) | Hub Foundry instance count | Open | 4, 11 |
| [OQ-006](../open-questions/OQ-006-cpi-sap-endpoint-via-mcp.md) | CPI / SAP endpoint via MCP | Open | 5, 11 |
| [OQ-007](../open-questions/OQ-007-api-centre-vs-apim-scope.md) | API Centre vs APIM scope | Open | 5, 11 |
| [OQ-008](../open-questions/OQ-008-custom-abstraction-trade-offs.md) | Custom abstraction trade-offs | Open | 5, 12 |
| [OQ-009](../open-questions/OQ-009-terraform-pattern-for-apim-native-mcp.md) | Terraform pattern for APIM-native MCP | Open | 5, 12, 16 |
| [OQ-010](../open-questions/OQ-010-agent-cicd-gates-and-foundry-versioning.md) | Agent CI/CD gates and Foundry versioning | Open | 12 |
| [OQ-011](../open-questions/OQ-011-maf-vs-logic-apps-selection-criteria.md) | MAF vs Logic Apps selection criteria | Open | 5 |
| [OQ-012](../open-questions/OQ-012-foundry-dashboard-scope.md) | Foundry dashboard scope | Open | 11 |
| [OQ-013](../open-questions/OQ-013-a2a-through-mcp.md) | A2A through MCP | Open | 5 |
| [OQ-014](../open-questions/OQ-014-per-agent-identity-vs-shared-sp.md) | Per-agent identity vs shared SP | Open | 6, 8 |
| [OQ-015](../open-questions/OQ-015-sql-knowledge-base-access-path.md) | SQL knowledge base access path | Open | 5, 11 |
| [OQ-016](../open-questions/OQ-016-fabric-integration.md) | Fabric integration | Open | 5 |
| [OQ-017](../open-questions/OQ-017-frontend-cicd-detail.md) | Frontend CI/CD detail | Open | 12 |
| [OQ-018](../open-questions/OQ-018-backend-cicd-detail.md) | Backend CI/CD detail | Open | 12 |
| [OQ-019](../open-questions/OQ-019-mcp-server-jwt-validation.md) | MCP server JWT validation | Open | 8 |
| [OQ-020](../open-questions/OQ-020-functions-vs-container-apps-for-fastmcp.md) | Functions vs Container Apps for FastMCP | Open | 5, 12 |

---

## 18. Roadmap

> Gap section — placeholder. Working intent: phased build keyed off the Tentative KDDs and high-impact open questions.
>
> - **Phase 0 — Foundations.** Hub-Foundry, shared APIM (with native MCP exposure), Toolbox, observability baseline.
> - **Phase 1 — First domain spoke.** EFF (or other pilot) end-to-end: one Foundry instance, one project, one Maximo MCP abstraction example.
> - **Phase 2 — Hardening.** Close [OQ-002](../open-questions/OQ-002-rate-limiting-and-token-quota.md), [OQ-009](../open-questions/OQ-009-terraform-pattern-for-apim-native-mcp.md), [OQ-010](../open-questions/OQ-010-agent-cicd-gates-and-foundry-versioning.md), [OQ-014](../open-questions/OQ-014-per-agent-identity-vs-shared-sp.md), [OQ-019](../open-questions/OQ-019-mcp-server-jwt-validation.md).
> - **Phase 3 — Multi-domain.** Onboard second/third spoke; resolve [OQ-003](../open-questions/OQ-003-domain-definition-logic.md).
> - **Phase 4 — Resilience.** Close [OQ-004](../open-questions/OQ-004-multi-region-failover.md) and execute BC/DR design from section 13.
>
> TODO: confirm sequencing with PM and platform team.

---

## 19. Glossary and references

**Primitive definitions:**

| Primitive | Definition | When to use | Build-it-well |
| --- | --- | --- | --- |
| Agent | An LLM with a system prompt, optional tools, context, memory, and knowledge. | Natural-language input; output requires synthesis; task involves judgement under ambiguity. | One responsibility per agent; strict I/O contract; only necessary tools and context. |
| Tool | A callable function with inputs and outputs, no prompt, no reasoning. | Agent needs a capability beyond language; capability is invoked conditionally; discrete and reusable. | Single responsibility; typed schemas; stateless and composable. |
| Deterministic step | A plain function in the pipeline with no LLM involvement; same input always yields same output. | Pure transformation; finite rule set; must always execute. | Explicit, testable, composable. Prefer deterministic steps where possible. |
| Workflow | The orchestration layer that connects agents, tools, and deterministic steps into a coherent pipeline. | Multiple primitives must compose; path is conditional or dynamic. | Start sequential and explicit before going dynamic. |
| Skill | A workflow/instruction set the agent follows internally — distinct from a tool ([KDD-023](../decisions/KDD-023-skill-vs-mcp-tool-framework.md)). | Encode standard procedures the agent applies to its reasoning. | Treat as the agent's playbook, not its capability surface. |

**Acronyms:** AIS = existing API orchestration layer (logic apps + functions); APIM = Azure API Management; AVM = Azure Verified Modules; A2A = Agent-to-Agent communication; FDA = Fabric Data Agent; HITL = Human-in-the-Loop; MAF = Microsoft Agent Framework; MCP = Model Context Protocol; OBO = OAuth On-Behalf-Of; TPM/RPM = Tokens-per-minute / Requests-per-minute.

**Source artefacts:**

- Deck baseline — [20260514 Agentic platform_vF.pptx](../../20260514%20Agentic%20platform_vF.pptx).
- Transcript A — [Microsoft Support — Foundry platform and MCP servers, 22 May 2026](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md).
- Transcript B — [Mitie / Microsoft regular technical check-in, 26 May 2026](../../transcripts/Mitie_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md).
- Predecessor draft — [HLD.md](../../HLD.md) (flat v0.1, kept for diff/baseline).
- KDD compliance recommendation — [recommendations/kdd-compliance-in-code-reviews.md](../../recommendations/kdd-compliance-in-code-reviews.md).
