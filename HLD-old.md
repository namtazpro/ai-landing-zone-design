# OCTA Agentic Platform — High-Level Design (HLD)

| Field | Value |
| --- | --- |
| Status | Draft |
| Version | 0.1 |
| Last updated | 2026-06-05 |
| Source baseline | [20260514 Agentic platform_vF.pptx](20260514%20Agentic%20platform_vF.pptx) (14 May 2026) |
| Decision log | [Section 14 — Key Design Decisions (KDDs)](#14-key-design-decisions-kdds) |
| Open questions | [Section 15 — Open questions](#15-open-questions) |

Draft HLD derived from the May 2026 architecture deck and the 22 May / 26 May technical calls. Each architectural section ends with a "Decisions" line that lists the KDD IDs and open questions traced back to those calls. The two transcripts live in [transcripts/](transcripts).

---

## 1. Purpose and scope

The OCTA Agentic Platform is the Azure target architecture for delivering agent-driven use cases for the Contoso / Microsoft engagement. It standardises how agents are defined, how tools are exposed, how workflows are orchestrated, and how the platform is secured, observed, and shipped through CI/CD. The platform is multi-tenant by domain (for example EFF, HR, Sales), Foundry-centred, and built on Microsoft Agent Framework as the orchestrator.

In scope:

- Agent and tool definition, registration, versioning, and CI/CD.
- Orchestration of single-agent and multi-agent workflows including human-in-the-loop (HITL).
- Frontend and backend application layers that expose agents to internal and external users.
- Identity, authorisation, observability, data, and integration patterns.

Out of scope (for v1):

- Multi-region failover topology (see [OQ-004](#15-open-questions)).
- Fabric data plane integration (see [OQ-016](#15-open-questions)).

---

## 2. Target architecture overview

External and internal users reach the platform through a Web Application Firewall and Application Gateway, authenticate with Microsoft Entra ID, and land on a Next.js frontend hosted on Azure Container Apps. The frontend calls a FastAPI backend, also on Container Apps, which acts as the ingestion and orchestration entry point. The backend invokes the Microsoft Agent Framework orchestration layer, which runs Foundry-hosted agents that consume tools exposed via Azure API Management (APIM) — preferably as MCP servers — and downstream systems such as Maximo (over APIM), SQL Server, Azure Data Lake, and Storage Accounts. Azure Managed Redis carries transient session and workflow state. Observability is consolidated in Application Insights with agent-level dashboards in Foundry.

Three Entra ID authentication layers are present: user-facing (Entra ID Protection), backend-to-agent (managed identities), and agent-to-tool (per-agent Entra identity with OAuth/OBO).

Decisions: [KDD-005](#14-key-design-decisions-kdds), [KDD-013](#14-key-design-decisions-kdds), [KDD-014](#14-key-design-decisions-kdds), [KDD-016](#14-key-design-decisions-kdds), [KDD-028](#14-key-design-decisions-kdds). Open: [OQ-001](#15-open-questions), [OQ-004](#15-open-questions), [OQ-005](#15-open-questions).

---

## 3. Conceptual primitives

The platform composes four primitives:

| Primitive | Definition | When to use | Build-it-well |
| --- | --- | --- | --- |
| Agent | An LLM with a system prompt, optional tools, context, memory, and knowledge. | Input is natural language; output requires synthesis; task involves judgement under ambiguity; solution path is not pre-defined. | One responsibility per agent; strict I/O contract; only necessary tools and context; clear guardrails. |
| Tool | A callable function with inputs and outputs, no prompt, no reasoning. | Agent needs a capability beyond language; capability is invoked conditionally; discrete and reusable. | Single responsibility; typed schemas; stateless and composable; explicit error handling. |
| Deterministic step | A plain function in the pipeline with no LLM involvement; same input always yields same output. | Output is a pure transformation; logic is a finite set of rules; step must always execute. | Explicit, testable, composable. Prefer deterministic steps to reduce cost and increase reliability. |
| Workflow | The orchestration layer that connects agents, tools, and deterministic steps into a coherent pipeline. | Multiple primitives must compose; path is conditional or dynamic; system pauses, resumes, or runs long. | Start sequential and explicit before going dynamic multi-agent (for example group chat); keep agents focused. |

Deterministic operations are modelled as MCP tools so they sit in the same registry as agentic capabilities.

Decisions: [KDD-004](#14-key-design-decisions-kdds), [KDD-018](#14-key-design-decisions-kdds), [KDD-023](#14-key-design-decisions-kdds).

---

## 4. Agent definition and versioning

Agents are defined in YAML and deployed through a standard provision script and CI/CD pipeline. Foundry owns version registry and rollback. Agents are platform-managed; teams do not handle the hosting runtime themselves.

The Foundry agent YAML schema fields are:

| Field | Purpose | Example |
| --- | --- | --- |
| `kind` | Asset type being created. | `prompt` |
| `name` | Unique identifier for the agent. | `research-agent` |
| `model` | Model deployment the agent uses. | `gpt-4.1` |
| `temperature` | Determinism vs randomness control. | `0.2` |
| `instructions` | Role, behaviour, and task instructions. | `"You are an investment research assistant..."` |
| `tools` | External tools/APIs with access and approval settings. | MCP server for SAP data |
| `text` | Structured-output JSON schema. | JSON schema with defined fields |

Decisions: [KDD-013](#14-key-design-decisions-kdds), [KDD-014](#14-key-design-decisions-kdds), [KDD-015](#14-key-design-decisions-kdds), [KDD-027](#14-key-design-decisions-kdds). Open: [OQ-010](#15-open-questions).

---

## 5. Tool definition and registry

Tools are exposed via the Model Context Protocol (MCP). MCP is the default standard; non-MCP integration requires a documented exception. Tools are grouped by user intent or business operation (not by source system or 1:1 with APIs) and packaged as MCP servers. Each MCP server should keep its tool count modest (rule of thumb: < 10) to avoid bloating the agent's context window.

Two layers of MCP exposure exist:

1. **APIM-native MCP** — Azure API Management exposes OpenAPI specs directly as MCP servers (Terraform-deployable, validated by working demo). This avoids running custom FastMCP containers wherever standard APIs already exist.
2. **Foundry Toolbox** — A second-layer MCP gateway above APIM that handles agent-specific filtering, versioning, and selective exposure of tools to individual agents.

Abstraction strategy follows "maximise work not done": v1 ships 1:1 API→MCP exposure through APIM. Custom abstraction (for example collapsing 14 granular Maximo APIs into 7 intent-driven operations like "find work order" or "create service request with duplicate check") is introduced only when context-window or accuracy pain is measured. Evidence from internal trials: abstracted grouping cut tool count by ~50%, tokens by ~30%, and improved latency and success rate.

Sensitive tools inside a grouped MCP server are isolated using the MCP `allow_tools` attribute so individual agents only see what they are authorised to call.

Decisions: [KDD-001](#14-key-design-decisions-kdds), [KDD-002](#14-key-design-decisions-kdds), [KDD-003](#14-key-design-decisions-kdds), [KDD-006](#14-key-design-decisions-kdds), [KDD-007](#14-key-design-decisions-kdds), [KDD-008](#14-key-design-decisions-kdds), [KDD-009](#14-key-design-decisions-kdds), [KDD-010](#14-key-design-decisions-kdds), [KDD-011](#14-key-design-decisions-kdds), [KDD-012](#14-key-design-decisions-kdds), [KDD-017](#14-key-design-decisions-kdds), [KDD-020](#14-key-design-decisions-kdds), [KDD-025](#14-key-design-decisions-kdds), [KDD-026](#14-key-design-decisions-kdds). Open: [OQ-008](#15-open-questions), [OQ-009](#15-open-questions), [OQ-020](#15-open-questions).

---

## 6. Agent communication

Communication is standardised on three layers:

- **Foundry runtime** — Foundry agents are invoked through the Azure AI Foundry Agent Framework runtime, supporting interoperable invocation patterns.
- **A2A (Agent-to-Agent)** — interoperable communication, delegation, and handoffs across distributed agents. Cross-domain agent calls are allowed; domain boundaries govern access control, not communication.
- **MCP (Model Context Protocol)** — standardises tool access, context sharing, and external capability integration. Non-Azure systems (for example SAP via CPI) are registered in APIM and exposed as MCP servers so agents can discover and call them.

Workflow orchestration supports message passing, agent-as-tool patterns, and multi-agent coordination through the Microsoft Agent Framework.

Decisions: [KDD-002](#14-key-design-decisions-kdds), [KDD-018](#14-key-design-decisions-kdds), [KDD-021](#14-key-design-decisions-kdds), [KDD-023](#14-key-design-decisions-kdds), [KDD-024](#14-key-design-decisions-kdds). Open: [OQ-006](#15-open-questions), [OQ-013](#15-open-questions).

---

## 7. Orchestration: Microsoft Agent Framework

The orchestration layer is the Microsoft Agent Framework (MAF). Component summary:

| Component | Responsibility |
| --- | --- |
| Orchestrator | Pro-code, production-grade foundation for deterministic pipelines through to autonomous group collaboration. |
| Single agent | Foundry agent invoked uniformly through `.run()` across all agent types. |
| Sequential workflow | `SequentialBuilder` for simple flows; `WorkflowBuilder` (graph API) for typed executors, conditional routing, fan-out/fan-in. |
| Group chat | `GroupChatBuilder(participants=[...], max_rounds=10).build()` runs agents in a shared conversation with a built-in selector. |
| HITL | Workflow pauses until a user provides feedback; resume re-injects the new payload into the next agent. |

MAF coexists with traditional orchestration (Logic Apps, Azure Data Factory) which remains the right choice for deterministic, long-running, asynchronous workflows and rich enterprise connectors. The split is not exclusive: deterministic backbones may invoke agentic steps and vice versa. The MAF vs Logic Apps trade-off is captured in Section 9.

Decisions: [KDD-018](#14-key-design-decisions-kdds). Open: [OQ-011](#15-open-questions).

---

## 8. CI/CD — Agents

PR validation (every stage blocking before merge):

1. Source checkout.
2. YAML schema validation.
3. Lint — naming, required fields, model whitelist.
4. Eval tests — golden prompts, regression checks.
5. Security scan — secrets, dependency audit.

Deployment (merge-triggered):

1. Package agent definitions; resolve semver from git tag.
2. Push artifact to ACR/blob.
3. Source branch routing: `dev` branch → dev project; `main`/`release` → prod project.
4. Manual approval gate before prod.
5. Deploy to Foundry project.
6. Register agent version in Foundry registry; retain previous versions for rollback.
7. Post-deploy verification: smoke prompts, OTel signals, alerts armed, one-click rollback.

Open: [OQ-010](#15-open-questions).

---

## 9. Orchestrator choice — MAF vs Logic Apps

Logic Apps express **static workflows** where every edge is defined at design time. Branches are enumerated; LLM is a step; tools are workflow actions. Microsoft Agent Framework expresses an **agentic mesh** of agents and tools whose edges emerge at runtime; a supervisor agent handles routing and handoffs over a shared tool registry that any agent can call.

| Aspect | Microsoft Agent Framework | Logic Apps |
| --- | --- | --- |
| Agents | First-class, stateful actors | Isolated LLM or function calls |
| Agent-to-agent | Direct, iterative (critique loops, debate, cooperation) | Indirect; coordinated through workflow logic |
| Coordination | Dynamic across multiple agents without a single controlling workflow | Centralised workflow controller |
| Execution paths | Determined dynamically from agent outputs and evolving state | Defined upfront; limited adaptability |
| Iterative reasoning | Native refine–critique–converge loops | Must be explicitly managed |
| Memory | Session-based state and memory patterns | Implemented manually via workflow logic and external storage |
| Workflow complexity | Modular, graph-based; scales as flows grow dynamic | Grows rapidly as flows become dynamic |
| Developer control | Code-first, fine-grained | Low-code visual, fast for simple flows |
| Infrastructure | Team manages hosting, scaling, resiliency, monitoring | Fully managed |
| Enterprise integration | Build-and-maintain integration layer | Extensive prebuilt connectors |
| Resilience | Code-driven retry / resilience | Built-in retry, timeout, exception policies |

The platform defaults to MAF for agentic workflows and retains Logic Apps for deterministic, long-running, connector-heavy orchestration.

Decisions: [KDD-018](#14-key-design-decisions-kdds). Open: [OQ-011](#15-open-questions).

---

## 10. Observability and evaluation

- **Traces.** Application Insights is the single sink for agent and workflow traces, including input, output, token usage, and event runtime.
- **Live dashboards.** App Insights provides cross-platform dashboards for error rates by tool/model, run counts, and token consumption by model. Foundry adds agent-level dashboards for estimated cost, token usage, error rates, and run volumes.
- **Agent evaluation.**
  - Offline: ground truth saved in blob storage and registered in Foundry; the `evaluate()` function runs custom evaluators per agent.
  - Online: Foundry built-in evaluators cover relevance, coherence, grounding, and similar metrics.
- **Cost attribution.** Per-agent and per-domain billing combines token counts with hosting/service consumption so chargeback is tractable.

Decisions: [KDD-014](#14-key-design-decisions-kdds), [KDD-015](#14-key-design-decisions-kdds), [KDD-019](#14-key-design-decisions-kdds), [KDD-027](#14-key-design-decisions-kdds). Open: [OQ-002](#15-open-questions), [OQ-012](#15-open-questions).

---

## 11. System integration

Four layers compose end-to-end flow:

1. **Ingestion** — APIs validate inbound requests from external sources (email, apps) and route them into orchestration.
2. **Orchestration** — Microsoft Agent Framework coordinates execution, manages workflow state, and handles HITL pauses.
3. **Agent and tool** — Agents execute tasks against tools registered with MCP servers, enabling modular and dynamic tool calling.
4. **Persistence and state** — Workflow state, job status, and results land in SQL Server for reliability, traceability, and resumability of long-running processes.

Existing AIS API orchestration (logic apps + functions) is reused for grouping/abstraction wherever it already exists. Custom MCP servers are only introduced when AIS does not already cover the abstraction.

Topology and tenancy:

- **One AI Foundry instance per business domain** (for example EFF, HR, Sales), with one Foundry project per use case.
- **Hub-spoke for model deployments.** A central hub Foundry instance (shared resource group) hosts LLM model deployments. Spoke Foundry instances in domain resource groups consume those models through APIM, enabling once-deployed, multi-domain consumption and unified retirement/rate-limit control.
- **Resource groups per domain per environment** (for example `EFF-Dev`, `EFF-Test`, `HR-Prod`) within a non-prod and a prod subscription, in line with current Mighty infrastructure conventions.

Decisions: [KDD-005](#14-key-design-decisions-kdds), [KDD-007](#14-key-design-decisions-kdds), [KDD-011](#14-key-design-decisions-kdds), [KDD-013](#14-key-design-decisions-kdds), [KDD-014](#14-key-design-decisions-kdds), [KDD-016](#14-key-design-decisions-kdds), [KDD-017](#14-key-design-decisions-kdds), [KDD-019](#14-key-design-decisions-kdds), [KDD-021](#14-key-design-decisions-kdds), [KDD-022](#14-key-design-decisions-kdds), [KDD-024](#14-key-design-decisions-kdds), [KDD-025](#14-key-design-decisions-kdds), [KDD-027](#14-key-design-decisions-kdds), [KDD-028](#14-key-design-decisions-kdds). Open: [OQ-001](#15-open-questions), [OQ-002](#15-open-questions), [OQ-003](#15-open-questions), [OQ-004](#15-open-questions), [OQ-005](#15-open-questions), [OQ-007](#15-open-questions), [OQ-015](#15-open-questions).

---

## 12. Data

| Concern | Decision |
| --- | --- |
| Operational data | SQL Server is the system of record for operational business data. |
| Knowledge base | Azure AI Search index (vector + semantic ranker) populated by an indexer skillset over blob/SharePoint, wrapped as a Foundry Knowledge Base object exposing an MCP URL. Agents autonomously call `knowledge_base_retrieve` when needed. |
| Agent / workflow context | Per-agent session memory in Foundry; workflow-shared state via `ctx.set_state(key, value)` / `ctx.get_state(key)` accessible across executors in a single run. |
| Persistent storage | SQL Server, Storage Accounts, Contoso Azure Data Lake. |
| Fabric data connection | TBD. |

Open: [OQ-015](#15-open-questions), [OQ-016](#15-open-questions).

---

## 13. Security

- **Per-agent Entra identity.** Each Foundry-hosted agent receives a dedicated Microsoft Entra ID identity at deployment, platform-managed, with no stored secrets.
- **Managed authentication.** When an agent invokes a tool, Foundry performs an OAuth token exchange with Entra ID and retrieves a scoped access token for the target resource. Token lifecycle is platform-managed.
- **RBAC.** Access to MCP tools, Azure resources, and external systems is governed by RBAC assignments tied to the agent identity, scoped per agent and enforced at runtime for least-privilege.
- **Delegated / OBO.** OAuth On-Behalf-Of flows let agents access user-specific resources with the user's delegated permissions while preserving enterprise policy enforcement.
- **MCP server authentication.** MCP servers validate incoming Entra ID JWTs (issuer, audience, signature) and check the agent's client/object ID against allow-lists or roles to authorise the requested tool.
- **Sensitive tool isolation.** MCP `allow_tools` attribute restricts which agents see which tools inside a grouped MCP server.

Decisions: [KDD-009](#14-key-design-decisions-kdds), [KDD-014](#14-key-design-decisions-kdds), [KDD-027](#14-key-design-decisions-kdds). Open: [OQ-014](#15-open-questions), [OQ-019](#15-open-questions).

---

## 14. Key Design Decisions (KDDs)

KDDs cite the relevant call transcript (date, speaker) and the HLD section they bind to. Source files:
[Microsoft Support — Foundry platform and MCP servers, 22 May 2026](transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md) and
[Contoso / Microsoft regular technical check-in, 26 May 2026](transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md).

| ID | Title | Decision | Status | Source (transcript / speaker / quote) | HLD section(s) |
| --- | --- | --- | --- | --- | --- |
| KDD-001 | Tool registry and categorisation | Tools are categorised and grouped by functionality, not assigned individually. Tool groups are wrapped as MCP servers to leverage MCP's input validation, dynamic exposure, and richer descriptions. | Decided | 22 May, Emma Sun: *"tools should be categorised...instead of...individual...we will...systemise, categorise those tools...wrap as MCP server so...leverage benefits"* | §5 |
| KDD-002 | MCP as universal tool exposure | All tools are exposed via MCP. MCP is the default standard; non-MCP requires a documented justification. | Decided | 22 May, Mike Agar and Francisco: *"use MCP...it needs to be...because we need to align on like a strategy that everything needs to follow this. And if it's go outside, it needs to have like a very specific reason"* | §5, §6 |
| KDD-003 | No 1:1 API-to-MCP mapping | Do not create one MCP server per API. Group APIs by use case or domain; one MCP server exposes multiple grouped operations (target < 10 tools per MCP to avoid context-window bloat). | Decided | 22 May, Emma Sun and Ha Duong: *"we won't do one-to-one mapping for sure...group the tools...have one MCP...point for a group of tools instead of just one"* | §5 |
| KDD-004 | Deterministic operations as MCP tools | All operations — deterministic or agentic — are modelled as MCP tools. Deterministic functions (for example "calculate VAT") sit alongside autonomous agent calls. | Decided | 22 May, Ha Duong: *"for the deterministic way...can be modelled as a tool within MCPs anyway...calculated VAT...you can using MCP expose as a tool"* | §3, §5 |
| KDD-005 | APIM as central gateway | Azure API Management (APIM) is the standard gateway for all API exposure. Backend APIs, MCP servers, and integrations funnel through APIM for policy, governance, auditing, and rate limiting. | Decided | 22 May and 26 May, Sourabh and Vincent: *"everything needs to be on APP...creating an API centre...one place...all the tools, agents, and everything...registry"* | §2, §5, §11 |
| KDD-006 | APIM-native MCP conversion | Use Azure API Management's native ability to expose OpenAPI specs as MCP servers. Terraform-driven (working demo). Avoids custom FastMCP overhead where standard APIs already exist. | Decided | 26 May, Vincent and Emma: *"can do Terraform...native resources...APP...Azure APP...MCP...confirmed that there is a protocol solution"* | §5, §16 |
| KDD-007 | Foundry Toolbox as MCP gateway | Foundry Toolbox sits as a second-layer MCP gateway above APIM-exposed MCP servers, handling versioning, agent-specific filtering, and selective exposure. | Decided | 22 May, Emma Sun: *"Foundry toolbox...additional layer...MCP...gateway...to agent...and that I agree with you...versioning and all that"* | §5, §11 |
| KDD-008 | Group tools by intent, not by system | Group tools by user intent / business operation (for example a "checkout workflow"), not by backend system. Combining add-to-cart, remove-from-cart, and checkout into one abstracted operation reduces agent orchestration burden. | Decided | 22 May, Ha Duong: *"group by...intention rather than actual...how would you use...give it to someone to do something...the intention rather than actual...API call"* | §5 |
| KDD-009 | Isolate sensitive tools via attributes | Sensitive endpoints inside a grouped MCP server use the MCP `allow_tools` attribute to restrict which agents see which tools. | Tentative | 22 May, Emma Sun and Sourabh: *"if there is a MCP server...allow tools...attribute...only this list...can be seen by this agent"* | §5, §13 |
| KDD-010 | Context-window optimisation | Prefer abstracted, intent-driven APIs over granular ones. Evidence from internal trial: ~50% fewer tools, ~30% token savings, lower latency, higher success rate. | Decided | 26 May, Ha Duong: *"success rate will be a lot more better...average tokens...less...cost...less"*; Mike: *"we need to focus on this...don't bloat the context window"* | §5 |
| KDD-011 | Reuse AIS abstraction layer | Reuse the existing AIS API orchestration layer (logic apps + functions) for any API grouping/abstraction. Do not build separate custom MCP servers if AIS already covers the abstraction. | Decided | 26 May, Mike and Ha: *"you already have...an abstraction...then you can...expose as MCP...don't have to do further if you need...then you build it yourself"* | §5, §11 |
| KDD-012 | Maximise work not done | Ship v1 as 1:1 API→MCP exposure in APIM. Only introduce abstraction when pain is measured (context-window issues, accuracy drop). Use-case-driven, not anticipatory. | Decided | 26 May, Ha Duong and Mike: *"maximise work not done...don't make that decision...publish it separately...then you make that decision later...when you see performance"* | §5 |
| KDD-013 | One Foundry instance per domain | Each business domain (EFF, HR, Sales) gets one AI Foundry instance with one Foundry project per use case. | Decided | 22 May, Vincent and Sourabh: *"one Foundry instance...one project per use case...one RG per domain...one instance...one project per use case"* | §4, §11 |
| KDD-014 | Hub-spoke for model deployments | A central hub Foundry instance in a shared resource group hosts all LLM model deployments. Spoke Foundry instances in domain resource groups consume hub models via APIM. Enables once-deployed, multi-domain consumption. | Decided | 22 May, Vincent: *"hub RG that's got its own foundry...models...deployed...Through the IPPI gateway...catalogued and registered here...model retirements...exactly who is using 4.1"* | §2, §4, §10, §11, §13 |
| KDD-015 | Model lifecycle control via hub | Central hub deployment enables unified control: retirement tracking, version deprecation, per-domain rate-limit capping via APIM policies, no orphaned references. | Decided | 22 May, Vincent: *"when...model retirements...exactly through auditing who is using 4.1...block...throttling...capping"* | §4, §10 |
| KDD-016 | Domain-isolated resource groups | Resource groups are created per domain per environment (for example `EFF-Dev`, `EFF-Test`, `HR-Prod`). Enables domain-based billing rollup and RBAC isolation within a subscription. | Decided | 26 May, Sourabh: *"one subscription...non-product...within that...dev and test per domain resource group...dev...test not product...prod subscription"* | §2, §11 |
| KDD-017 | API-first tooling standard | All tools are exposed as APIs. Whether Function App, FastAPI, or native Maximo APIs, every tool becomes an endpoint. No direct agent-to-function calls — everything funnels through API → MCP. | Decided | 26 May, Francisco and Sourabh: *"even if it is function up...it's still going to have an endpoint...so that endpoint...needs to be...collapsing all of that in grouping them...MCP server inside of APP"* | §5, §11, §16 |
| KDD-018 | Orchestration layer separation | Traditional orchestration (Logic Apps, ADF) owns deterministic, long-running, asynchronous workflows. Agents own autonomous, real-time, agentic tasks. Both coexist. | Decided | 22 May, Vincent: *"workflows...orchestration layer...more complex...still need...traditional API calls...connectors...mixed with agents...MCP endpoints"* | §3, §7, §9 |
| KDD-019 | Per-agent billing and cost attribution | Track costs per agent and per domain. Combine token counts with service consumption (hosting, storage) for agent-level chargeback. Log analytics + policies for auditing. | Decided | 26 May, Sourabh: *"we need to know which agent is consuming how much...agent-wise billing...token...consumption costs...also...hosting costs...will be account data"* | §10, §11 |
| KDD-020 | Skip custom MCP server overhead | Use APIM's native MCP exposure (Terraform-driven) rather than custom-built FastMCP servers on Container Apps. Reduces operational burden. | Decided | 26 May, Mike: *"why wouldn't we...use APP? If you can tick a box...we don't have...loads of servers...we're managing"* | §5, §16 |
| KDD-021 | CPI/SAP integration via MCP | Non-APIM systems (for example SAP via CPI) are registered in API Management and exposed as MCP servers so agents can access them without direct system coupling. | Tentative | 22 May, Mike: *"might be into...other systems...SAP uses CPI...we want to expose through MCP...discoverable by the AI"* | §5, §6, §11 |
| KDD-022 | API Centre as separate registry | API Centre (distinct from APIM) is the repository for API / MCP / A2A / skill metadata across multi-cloud deployments. Complements APIM's policy layer. | Tentative | 22 May, Ha Duong and Vincent: *"API Centre...separate product...registry...you don't have to...within APP...can be anywhere"* | §5, §11 |
| KDD-023 | Skill vs MCP tool framework | Skills encode deterministic workflows/instructions an agent should follow. MCP exposes external systems an agent can invoke. Do not replicate one as the other. | Tentative | 22 May, Ha Duong: *"skill...workflow...agent...MCP server...interact with other system...make that system available...multiple agents"* | §3, §5, §6 |
| KDD-024 | Cross-domain agent communication | Agents in one domain (for example EFF) may invoke agents in another (for example HR) through a shared agent registry / orchestration layer. Domain boundaries govern access control, not communication. | Decided | 22 May, Mike: *"share those resources...a multifunctional...useful...in the engineering space...Can they talk...cross boundaries"* | §6, §11 |
| KDD-025 | Maximo API abstraction example | Concrete case: collapse ~14 granular Maximo APIs into 7 abstracted operations ("find work order", "create service request with duplicate check"). Reduces agent tool list and improves accuracy. | Decided | 26 May, Ha Duong and Sourabh: *"14...APIs...MCP expose 7...instead of...tree dot...instead of...one dot...duplicate cheque create SR...one endpoint"* | §5, §11 |
| KDD-026 | No blanket abstraction requirement | Not every API set needs custom abstraction. Well-designed, small API sets are exposed 1:1 through APIM MCP. Abstract only when pain occurs. | Decided | 26 May, Ha Duong and Mike: *"if we see the abstractions that needed...then we can implementing...got the place for it...feel the pain...performance degradation"* | §5 |
| KDD-027 | Model scaling via replicas + policies | Hub Foundry deploys multiple replicas of the same model to absorb rate-limit demand. APIM policies enforce per-domain quotas without requiring subscription-level changes. | Decided | 26 May, Vincent: *"multiple instances even in your hub...multiple domains...deploy multiple instances...through load balancing...models...hub...rate limiting"* | §4, §10, §11, §13 |
| KDD-028 | Reuse existing Mighty infrastructure pattern | Keep the current Mighty pattern (non-prod + prod subscriptions, resource groups per domain). Do not restructure to subscription-per-domain unless InfoSec mandates it. | Decided | 26 May, Mike and Vincent: *"how we work today...InfoSec must have agreed...it's already working...this is not...AI...way mighty decided"* | §2, §11 |

---

## 15. Open questions

Items raised in the calls without a final decision. Each blocks (or partially blocks) one or more HLD sections.

| ID | Question / action | Status | Source | HLD section(s) |
| --- | --- | --- | --- | --- |
| OQ-001 | **Subscription strategy.** Subscription-per-domain (stronger RBAC isolation) vs current resource-group-per-domain inside shared subscriptions? Needs InfoSec and Poorna alignment. | Open | 26 May, Mike: *"we need to talk to other colleagues...why are we changing it"* | §2, §11 |
| OQ-002 | **Rate limiting and token quota.** How to enforce TPM/RPM per domain on a central hub Foundry? Can Microsoft raise limits if required? | Open | 26 May, Sourabh and Vincent: *"rate limit...token limit server will impact production...how do we...apply policies"* | §10, §11 |
| OQ-003 | **Domain definition logic.** What is the principled basis for domains (EFF, HR, Sales)? Project-driven naming cannot remain the rationale. | Open | 26 May, Mike: *"why have we divided it this way?...they're just random work streams...cannot be in the KDD"* | §11 |
| OQ-004 | **Multi-region failover.** Required for model deployments? Affects Foundry geography, APIM routing, and SLAs. | Open | 26 May, Mike: *"what availability...targets...failover...we haven't even..."* | §2, §10, §11 |
| OQ-005 | **Hub Foundry instance count.** One hub shared across non-prod domains plus a prod hub, or one hub per environment? | Open | 26 May, Vincent and Sourabh: *"one shared...one maybe one shared for dev...one shared for test"* | §4, §11 |
| OQ-006 | **CPI / SAP endpoint via MCP.** Concrete integration pattern for non-Azure systems through APIM + MCP. | Open | 22 May, Mike mentions CPI — no resolution | §5, §6, §11 |
| OQ-007 | **API Centre vs APIM scope.** Metadata/governance boundary between API Centre and APIM, and sync model. | Open | 22 May, Ha Duong and Vincent | §5, §11 |
| OQ-008 | **Custom abstraction trade-offs.** Decision criteria for when to build custom FastMCP abstraction (for example duplicate-check + create-SR) vs rely on APIM + standard APIs. | Open | 26 May, Ha Duong: *"this is very use case specific...don't think that we can give clear guidance without knowing actual use cases"* | §5, §16 |
| OQ-009 | **Terraform pattern for APIM-native MCP.** Capture Vincent's working demo as repeatable IaC modules. | Open | 26 May, Emma: *"can we do write code to deploy the MCP server in APP...assessment"* | §5, §16, §17 |
| OQ-010 | **Agent CI/CD gates and Foundry versioning.** Define PR gates, version registry semantics, and rollback strategy in detail. | Open | Not directly discussed | §8 |
| OQ-011 | **MAF vs Logic Apps selection criteria.** Formalise when to choose Microsoft Agent Framework vs Logic Apps per workflow. | Open | 22 May, Vincent touches on orchestration layers | §7, §9 |
| OQ-012 | **Foundry dashboard scope.** Required metrics and integration with App Insights. | Open | Not explicitly discussed | §10 |
| OQ-013 | **A2A through MCP.** Can an agent be invoked as a tool by another agent through MCP, or is that orchestrator-only? | Open | Briefly mentioned, no decision | §6 |
| OQ-014 | **Per-agent identity vs shared service principal.** Security and auditability trade-off. | Open | Not discussed in transcripts | §13 |
| OQ-015 | **SQL knowledge base access path.** MCP-wrapped endpoint vs direct SDK? Preference for SDKs per user convention. | Open | Topic 12 mentions both; no decision | §11, §12 |
| OQ-016 | **Fabric integration.** Pattern for Microsoft Fabric (warehouse, ML pipelines) inside agent workflows. Currently TBD. | Open | 26 May, data-layer discussions touch Fabric | §12 |
| OQ-017 | **Frontend CI/CD detail.** Confirm `npm ci`, ESLint, Prettier, `tsc`, Jest 70%, and `cosign` signing. | Open | Not discussed in transcripts | §17 (forthcoming) |
| OQ-018 | **Backend CI/CD detail.** Confirm `uv sync`, `ruff`, `mypy`, `pytest ≥ 90%`, `alembic upgrade head`. | Open | Not discussed in transcripts | §16 (forthcoming) |
| OQ-019 | **MCP server JWT validation.** Issuer, audience, and validation mechanism. | Open | Topic 13 mentions, not discussed | §13 |
| OQ-020 | **Functions vs Container Apps for custom FastMCP.** Hosting trade-off for any custom FastMCP not handled by APIM-native exposure. | Open | 22 May mentions both, no consensus | §5, §16 |

---

## 16. Backend microservice (to be expanded)

Outline from the deck — not yet ratified by the calls:

- FastAPI in Python on Azure Container Apps.
- Entra ID OAuth2 / JWT for authentication; RBAC + Pydantic for authorisation and request validation; audit logging.
- Azure Managed Redis for cache, session, and transient state.
- Shared common layer for DI, SDKs, config, and observability standards.

Decisions: [KDD-017](#14-key-design-decisions-kdds), [KDD-020](#14-key-design-decisions-kdds). Open: [OQ-018](#15-open-questions), [OQ-020](#15-open-questions).

CI/CD outline (deck): PR gates — checkout → `uv sync --frozen` → `ruff` + `mypy` → `pytest ≥ 90%` → SAST + dep audit. Deployment — semver package → ACR push → manual gate → dev/prod env → container startup runs `alembic upgrade head` then `uvicorn` → health/Postman/OTel verification + one-click rollback.

---

## 17. Frontend (to be expanded)

Outline from the deck — not yet ratified by the calls:

- Next.js single-entry UI behind Application Gateway, hosted on Azure Container Apps.
- Entra ID OAuth2 bearer tokens; backend API calls authenticated.
- Aggregates multiple workflows into one experience; supports HITL.

Open: [OQ-017](#15-open-questions).

CI/CD outline (deck): PR gates — checkout → `npm ci` + `next build` → ESLint + Prettier + `tsc` → Jest ≥ 70% → SAST + dep audit. Deployment — docker build from base image with `cosign` signing → ACR push → manual gate → dev/prod env → Next.js boot → health/smoke/OTel verification + rollback.

---

## 18. Base image CI/CD (to be expanded)

Deck slide 18 ("CI/CD – Base Image") was title-only in the source XML and could not be auto-extracted. To be filled in by reading the slide directly in PowerPoint.

---

## 19. Source artefacts

- Deck baseline — [20260514 Agentic platform_vF.pptx](20260514%20Agentic%20platform_vF.pptx).
- Transcript A — [Microsoft Support — Foundry platform and MCP servers, 22 May 2026](transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md).
- Transcript B — [Contoso / Microsoft regular technical check-in, 26 May 2026](transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md).
