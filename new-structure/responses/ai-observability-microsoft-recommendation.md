# AI Observability — Microsoft platform recommendation

| Field | Value |
| --- | --- |
| Source requirements | [../assets/AI Observability - HLR and Detailed Requirements.docx](../assets/AI%20Observability%20-%20HLR%20and%20Detailed%20Requirements.docx) (V0.1, 2 June 2026) |
| Source extract | [../assets/AI Observability - HLR and Detailed Requirements.source.md](../assets/AI%20Observability%20-%20HLR%20and%20Detailed%20Requirements.source.md) |
| Companion document | [ai-observability-solution-mapping.md](ai-observability-solution-mapping.md) — same requirements anchored to the OCTA HLD baseline. **This document deliberately ignores the OCTA HLD and starts from Microsoft platform capabilities only.** |
| Author | Microsoft architecture |
| Version / date | v1 — 2026-06-22 |
| Status | Draft for review |

## Purpose

This is an independent Microsoft recommendation for the *AI Observability HLR
and Detailed Requirements* document. It answers a single question: given
Microsoft's current platform, how would we observe, govern, report on and
cost-attribute an enterprise AI agent estate that spans **Copilot Studio**,
**Microsoft Foundry prompt agents**, **Microsoft Foundry hosted agents** and
**third-party vendor agents**?

The recommendation is built bottom-up from Microsoft components, then mapped
to the risks, HLRs, FRs and NFRs in the source document. Existing internal
architecture artefacts are not used as input.

## 1. The agent surfaces we need to cover

A realistic enterprise estate today contains four distinct agent build
surfaces. Each has different observability primitives, and the recommendation
must respect those differences rather than try to force one model on all of
them.

| Surface | What it is | Native observability hooks |
| --- | --- | --- |
| **Copilot Studio agents** | Low-code declarative agents and custom Copilot extensions surfaced in Microsoft Teams, M365 Copilot and the web. | Built-in Copilot Studio analytics (sessions, topics, engagement, transcripts), Dataverse activity and conversation transcripts, Power Platform admin centre, Microsoft Purview audit log for M365 Copilot, optional Application Insights export for custom topics and connectors. |
| **Foundry prompt agents** | Declarative agents authored in Microsoft Foundry against a model + tools + knowledge configuration, with limited custom code. | Foundry runs tracing (OpenTelemetry) by default, Foundry Continuous Evaluation, Foundry Responsible AI dashboard, Foundry Content Safety filters, per-project diagnostic settings to Log Analytics / Event Hubs / Storage. |
| **Foundry hosted agents** | Code-first agents deployed through Foundry Agent Service (Python / .NET / TypeScript SDKs) with full extensibility. | Same as prompt agents, plus full freedom to use the OpenTelemetry SDK directly and emit custom spans / metrics / business events. Best surface for adopting a platform SDK. |
| **Third-party vendor agents** | SaaS agent platforms such as SAP Joule, Salesforce Agentforce, ServiceNow Now Assist, Workday, and on-prem / custom agents (LangChain, AutoGen, custom). | Vendor-specific audit log APIs and connectors; Microsoft Sentinel data connectors where available; Microsoft Defender for Cloud Apps for SaaS visibility; for custom code-first agents, direct OpenTelemetry SDK to Azure Monitor; for any agent calling an external model, traffic flows through Azure API Management as the AI Gateway. |

This four-surface reality drives several of the recommendations below — in
particular the use of OpenTelemetry as the wire format, APIM as the common
ingress for model traffic, and Microsoft Fabric as the business-event lake
that all surfaces write into through a shared SDK or adaptor.

## 2. Reference Microsoft stack

The recommendation is organised into six planes. Each plane delivers a set of
capabilities; the planes are independently replaceable and individually
adoptable, so customers can phase the rollout.

| Plane | Role | Microsoft components |
| --- | --- | --- |
| Identity & registration | Give every agent a managed identity and a registered fleet record carrying ownership, lifecycle, compliance evidence. | Microsoft Entra Agent ID (the agent-specific identity primitive), Microsoft Defender for Cloud Apps (SaaS agent inventory), Microsoft Purview Compliance Manager (evidence store). |
| Ingress & AI gateway | One controlled path for every model and tool call; apply auth, quotas, content safety, semantic cache, token metering. | Azure API Management with AI Gateway policies (`llm-token-limit`, `llm-emit-token-metric`, `llm-semantic-cache-store/lookup`, `llm-content-safety`), standard APIM policies for auth, rate limit, JWT validation, IP filtering, and product / subscription keys. |
| Telemetry | Vendor-neutral OpenTelemetry stream into Microsoft observability stores. | Foundry tracing (OTel-native), OpenTelemetry SDKs for hosted and custom agents, Azure Monitor OpenTelemetry distro, Application Insights, Log Analytics workspaces, Azure Data Explorer (Kusto) for high-volume trace analytics, Azure Managed Grafana for SRE dashboards. |
| Business events | Standardised business-meaningful events from all agents, stored once, reportable many times. | Microsoft Fabric Lakehouse on OneLake, Fabric Eventstream for streaming ingestion, Fabric Data Activator for threshold-based business alerts, Microsoft Purview Data Map for schema governance. |
| Reporting & governed NL query | Persona-based dashboards plus a governed natural-language query surface. | Power BI app workspaces on Fabric semantic models (executive, business owner, finance, compliance), Azure Monitor workbooks (engineering / SRE), Microsoft Sentinel workbooks (security), Microsoft Fabric Data Agent for governed NL query, Copilot in Power BI for chart-level Q&A. |
| Governance & Responsible AI | Audit, retention, access control, Responsible AI evidence and continuous quality measurement. | Microsoft Purview (sensitivity labels, DLP, audit, lifecycle, Compliance Manager), Azure AI Content Safety (text moderation, prompt shields, groundedness detection, protected material), Foundry Responsible AI dashboard, Foundry Continuous Evaluation, Microsoft Defender for Cloud (CSPM and regulatory compliance), Microsoft Sentinel as SIEM / SOAR. |

A small platform SDK (NuGet / npm / PyPI), maintained by the customer's
platform team, wraps the Azure Monitor OpenTelemetry distro and provides a
typed `emit_business_event(...)` helper that writes to Fabric via Eventstream.
This SDK is the canonical way Foundry hosted agents and custom code-first
agents emit the central business event schema. Copilot Studio agents and
Foundry prompt agents use thin adaptors described below.

## 3. How each agent surface is observed

### 3.1 Copilot Studio agents

- **Technical telemetry** — enable Application Insights integration on the
  Copilot Studio environment to capture conversation telemetry, topic
  triggers, generative answers, action calls and errors with `traceparent`
  correlation.
- **Audit and compliance** — Microsoft Purview audit logs will capture interactions with any agents published via M365 or connected via SDKs; Dataverse retains conversation transcripts and
  analytics tables; Microsoft Sentinel ingests via the Microsoft 365
  connector.
- **Business events** — a published platform Power Automate cloud flow is
  triggered by Copilot Studio events (topic completed, action invoked,
  handoff to agent). The flow calls a thin Function-app endpoint exposed
  through APIM that runs the platform SDK to write a normalised business
  event into Fabric. This keeps Copilot Studio authors free of telemetry
  code.
- **Cost** — Power Platform admin centre + Microsoft Cost Management surface
  Copilot Studio message capacity consumption; per-agent attribution is
  derived from the Copilot Studio agent ID stored on each business event.

### 3.2 Foundry prompt agents

- **Technical telemetry** — Foundry tracing is enabled per project; diagnostic
  settings route traces and run logs to a Log Analytics workspace and to
  Application Insights.
- **Quality** — Foundry Continuous Evaluation samples production traffic and
  emits groundedness, relevance, coherence, fluency and safety scores. These
  surface in the Foundry Responsible AI dashboard and are exported to Fabric
  via the Foundry → Eventstream connector for cross-agent reporting.
- **Content safety** — Azure AI Content Safety filters configured at the
  Foundry project level; violations recorded as events and forwarded to
  Microsoft Sentinel.
- **Business events** — prompt agents call APIM-fronted tools. The APIM
  policy that fronts each tool emits a business event automatically using a
  `set-body` + `send-request` pattern, populating the central schema. Where
  the prompt agent needs to record a business outcome not implied by a tool
  call, the platform team can attach a small "business event tool" that the
  prompt agent calls explicitly.

### 3.3 Foundry hosted agents

- **Technical telemetry** — the platform SDK initialises the Azure Monitor
  OpenTelemetry distro at start-up. All inbound calls, model calls and tool
  calls become OTel spans automatically.
- **Quality** — Foundry Continuous Evaluation as above, plus the option of
  per-deployment offline evaluation runs in CI/CD with the Foundry
  evaluators.
- **Business events** — direct `emit_business_event(...)` calls from agent
  code. Mandatory fields are enforced by the SDK; the schema reference is
  pulled from Microsoft Purview Data Map at build time.
- **Operational** — the agent runs under a managed identity from Microsoft
  Entra Agent ID; ingress (where the agent exposes endpoints) is through
  APIM.

### 3.4 Third-party vendor agents

- **SaaS agents (SAP Joule, Salesforce Agentforce, ServiceNow Now Assist,
  Workday, similar)** — observed in three layers:
  - **Audit and posture** — Microsoft Sentinel data connector for the vendor
    where one exists; Microsoft Defender for Cloud Apps to inventory the
    SaaS, score the posture and detect anomalies.
  - **Telemetry** — vendor webhook or audit-log polling job lands events on
    APIM, which validates, normalises and forwards them to App Insights
    (technical signals) and Fabric Eventstream (business events).
  - **Model traffic** — where the SaaS calls Microsoft-hosted models, those
    calls are routed through APIM and observed natively.
- **Custom code-first agents (Semantic Kernel, LangChain, AutoGen, others
  on AKS / Container Apps / Functions)** — same recommendation as Foundry
  hosted agents: platform SDK + Entra Agent ID + APIM ingress.

## 4. Mapping to the customer requirements

The recommendation is now mapped onto the source numbering so reviewers can
walk the document directly. The customer requirement text is summarised; the
authoritative wording stays in the source.

### 4.1 Risks (source section 4.3)

| Ref | Risk (summarised) | Microsoft mitigation |
| --- | --- | --- |
| 4.3.1 | Over-broad data exposure through governed NL query | Fabric Data Agent restricted to a curated lakehouse; OneLake item-level permissions and Fabric RLS; queries run under the caller's Microsoft Entra ID; Purview audit + Sentinel monitoring; Defender for Cloud DLP on the workspace. |
| 4.3.2 | Inconsistent / incomplete event data | Platform SDK + APIM validation reject events missing mandatory fields; schema versioned in Purview Data Map; CI pipeline runs schema-diff checks. |
| 4.3.3 | Solution complexity exceeds delivery capacity | Phased rollout: phase 1 = APIM + Foundry tracing + Log Analytics dashboards for one pilot agent; phase 2 = Fabric lakehouse + business events; phase 3 = Fabric Data Agent + Sentinel correlation + Responsible AI dashboards. |
| 4.3.4 | Security, privacy, compliance breach | Purview sensitivity labels + DLP; Defender for Cloud regulatory compliance; CMK encryption in Log Analytics, ADX, Fabric; quarterly access reviews via Microsoft Entra Identity Governance. |
| 4.3.5 | Low adoption by agent teams | Registration in Microsoft Entra Agent ID is the precondition for APIM granting production keys; templates published as `azd` starter packs; engineering scorecards in Foundry track onboarding KPIs. |
| 4.3.6 | Cost growth | Log Analytics commitment tiers + Basic Logs for high-volume telemetry; Archive tier beyond a threshold; Fabric capacity guardrails; APIM `llm-token-limit` + semantic caching reduce model spend; Azure Cost Management views per agent and per business domain. |
| 4.3.7 | Legacy / third-party agents cannot emit required events | APIM-fronted adaptors and webhook receivers per vendor; Sentinel data connectors for SaaS audit; documented minimum-viable-telemetry per agent class. |
| 4.3.8 | Incorrect KPI interpretation | KPI catalogue maintained as a Power BI semantic model with definitions, owners and lineage shown via Microsoft Purview; quarterly review owned by the platform team. |
| 4.3.9 | Responsible-AI evidence incomplete or untraceable | Compliance evidence stored in Microsoft Purview Compliance Manager and referenced from the Microsoft Entra Agent ID fleet record; Power BI surfaces missing or expired evidence; Sentinel scheduled rule raises alerts on overdue items. |
| 4.3.10 | Bias / fairness / proxy discrimination not detected early | Foundry Responsible AI dashboard for groundedness, harm and fairness signals; Azure AI Content Safety as APIM policy; demographic outcome monitoring in Fabric using a protected-characteristic taxonomy in Purview; Sentinel UEBA for anomalous patterns. |

### 4.2 High-level requirements (source section 5.1)

| # | Requirement (summarised) | Microsoft recommendation |
| --- | --- | --- |
| R1 | End-to-end traceability across orchestration, tools, models, retrieval, downstream actions. | OpenTelemetry as the wire format; `traceparent` propagated by Foundry, APIM, the platform SDK and Copilot Studio Application Insights export; traces in App Insights with long-term retention in Azure Data Explorer. |
| R2 | Near-real-time operational metrics. | APIM `llm-emit-token-metric` + Foundry runtime metrics + App Insights live metrics; Azure Monitor workbooks per agent and per model. |
| R3 | Continuous evaluation of output quality. | Foundry Continuous Evaluation jobs sampling production traffic; results exported to Fabric for cross-agent comparison and to Power BI for product owners. |
| R4 | Safety / policy / content-filter monitoring with alerts. | Azure AI Content Safety on APIM and at the Foundry project level; events to Microsoft Sentinel for analytics and case management. |
| R5 | Cost attribution by agent / model / environment. | APIM token metrics tagged with agent ID, project, environment; Azure Cost Management views for infra; Microsoft Cost Management for Power Platform; Fabric semantic model combines token and infra cost per agent. |
| R6 | Prompt and configuration versioning, collaborative review, A/B testing. | Foundry Prompt Flow + Prompt registry, with Azure DevOps / GitHub for review workflows and Foundry deployment slots for A/B. |
| R7 | Auditable record of access, configuration changes, query activity and lineage. | Microsoft Entra audit + Microsoft Purview audit + Microsoft Sentinel as the SIEM of record; Fabric Data Agent query logs; lineage in Purview Data Map. |
| R8 | Enterprise governance, registration, fleet visibility. | Microsoft Entra Agent ID as the agent registry; integrated with Purview Compliance Manager for evidence; Power BI compliance dashboard for fleet posture. |
| R9 | Integration with approved monitoring, dashboarding, reporting. | Azure Monitor / Sentinel / Power BI as defaults; Azure Managed Grafana for teams preferring Grafana; ServiceNow integration via APIM-fronted connector. |
| R10 | Business observability, dashboards, governed AI-assisted access. | Business events in Fabric Lakehouse; Power BI persona dashboards on the semantic model; Fabric Data Agent for NL access. |
| R11 | Multi-model / multi-platform observability. | Foundry model catalogue covers Azure OpenAI, Models-as-a-Service and partner models; APIM normalises observability across all of them irrespective of the upstream provider. |
| R12 | Human-in-the-loop oversight for high-impact decisions. | Foundry agent action gates; Power Automate + Microsoft Teams Approvals for review workflow; outcomes written back as business events; Sentinel scheduled analytics for overdue oversight. |
| R13 | Observability for low-code (Copilot) and external (Joule etc.) agents. | Per section 3.1 (Copilot Studio) and 3.4 (third-party). Copilot Studio via Application Insights + Purview + Power Automate to platform SDK; SaaS via Sentinel connectors, Defender for Cloud Apps and APIM-fronted webhooks. |

### 4.3 Detailed functional requirements (source section 5.3)

| Source ID | Microsoft recommendation |
| --- | --- |
| FR-TECH-001 — End-to-end layered architecture across Dev/Test/Prod | Realise the six-plane stack in section 2 with per-environment Foundry hubs, per-environment APIM instances and per-environment Fabric workspaces, all deployed via Bicep / `azd`. Onboard one pilot agent end to end per environment to demonstrate the architecture. |
| FR-TECH-002 — Mandatory agent logging with required fields | Foundry tracing on by default; APIM enriches every call with `agent_id`, `environment`, `traceparent` and tenant headers; platform SDK enforces business-event field presence; ≥95% conformance gate enforced at onboarding. |
| FR-TECH-003 — Centralised event schema with controlled extensions | Schema modelled in Microsoft Purview Data Map; mandatory and optional fields per the schema in section 5 below; extensions live under a typed `extensions` object with a registered domain schema ID; CI runs schema-diff and rejects breaking changes. |
| FR-TECH-004 — Monitoring and alerting | Azure Monitor metric / log alerts for technical signals; Microsoft Sentinel scheduled analytics for security and policy events; Fabric Data Activator for business-outcome thresholds; ServiceNow integration via APIM connector. |
| FR-TECH-005 — Alert severity and response SLAs | Severity / SLA matrix encoded as Azure Monitor action groups and Sentinel automation rules; on-call schedules and Teams routing in Azure Monitor; ServiceNow priority mapping configured in the APIM connector. |
| FR-TECH-006 — Storage and retention policy | Log Analytics interactive + Basic Logs + Archive tiers per category; Fabric OneLake for business events with Purview retention labels; Microsoft Purview Data Lifecycle Management drives auditable purges. |
| FR-TECH-007 — Low-code and external agent observability | Per section 3.1 and section 3.4. Document minimum viable telemetry per vendor / platform in the LLD; onboard one representative external agent end to end. |
| FR-SEC-002 — Database-level row-level security | Fabric workspace RLS plus OneLake item-level permissions; SQL endpoints inherit RLS; Power BI semantic models reuse the same RLS roles; Fabric Data Agent queries run under the caller's Entra ID. |
| FR-BUS-001 — Business event tracking | Events produced via the platform SDK or APIM event policy; landed on Fabric Eventstream; persisted into a gold-layer delta table per business domain; outcome taxonomy held in Purview Data Map. |
| FR-BUS-002 — AI agent that converts NL to SQL | Microsoft Fabric Data Agent over the curated semantic model; user-context query execution; structured table output; conversation logs to Purview audit. |
| FR-EXEC-001 — Role-based dashboards | Power BI app workspaces per persona on the Fabric semantic model (executive, business owner, finance, compliance); Azure Monitor workbooks for engineering / SRE; Microsoft Sentinel workbooks for security. |
| FR-EXEC-002 — KPI framework | KPIs encoded as DAX measures in the Fabric semantic model with description, owner, cadence metadata; lineage exposed via Purview; baseline KPI list in section 6 below. |
| FR-CMP-001 — Human oversight and escalation | Foundry agent action gates raise approvals through Power Automate to Microsoft Teams; outcome written back as a business event (`review_required`, `review_completed`, `review_bypassed`); Sentinel raises alerts on overdue reviews; Power BI compliance dashboard tracks throughput and aging. |

### 4.4 Non-functional requirements (source section 6)

| Source ID | Microsoft recommendation |
| --- | --- |
| NFR.SEC.1 — Encryption in transit and at rest | TLS 1.2+ enforced end to end; customer-managed keys on Log Analytics, ADX and Fabric via Azure Key Vault; Defender for Cloud regulatory compliance checks verify configuration. |
| NFR.SEC.2 — Audit logging | Microsoft Entra ID sign-in and audit logs + Microsoft Purview audit + Fabric audit + APIM diagnostics, all forwarded to a single Microsoft Sentinel workspace as the audit system of record. |
| NFR.PER.1 — Performance targets | Recommend ≤30 s ingestion lag (App Insights + Log Analytics), Fabric semantic-model refresh on a 15-minute cadence in production, P95 NL query ≤8 s on the curated lakehouse. Targets confirmed in design. |
| NFR.SCL.1 — Scalability | Log Analytics multi-workspace pattern with per-domain workspaces fronted by ADX cross-cluster queries; Fabric capacity sized per environment with autoscale and pause/resume; APIM premium with regional units. Azure Load Testing pack delivered. |
| NFR.AVL.1 — Availability | Target 99.9% on user-facing surfaces; underlying Azure SLAs aggregated and published in the operating handbook. |
| NFR.RES.1 — Resilience | Zone-redundant deployments for APIM, Log Analytics, Fabric and ADX; retry / circuit-breaker policies on APIM; Foundry hubs in paired regions where required. |
| NFR.DR.1 — Disaster recovery | Default RTO 4 h, RPO 1 h for tier-1 data; geo-redundant storage; Fabric mirroring; annual DR drill documented in the operating handbook. |
| NFR.SUP.1 — Operating and support model | Operating handbook delivered in design phase, integrated with the customer's ServiceNow; change approval via Azure DevOps + Microsoft Entra PIM. |
| NFR.DQ.1 — Data quality controls | Fabric Data Quality rules + Microsoft Purview Data Quality scans; APIM schema validation as the first line; Fabric Data Activator alerts on DQ breaches. |
| NFR.CMP.1 — Privacy, retention, residency | Microsoft Purview sensitivity labels and DLP on every store; APIM PII detection policy on requests / responses with optional redaction; region policy enforces residency; right-to-erasure via Purview eDiscovery + a documented purge runbook. |
| NFR.CMP.2 — Responsible-AI evidence | Per-agent evidence stored against the Microsoft Entra Agent ID record (owner, lifecycle, DPIA reference, bias-assessment status, ethics-review status, approval status); artefacts in Purview Compliance Manager; reporting in the Power BI compliance dashboard. |

## 5. Business event schema — Microsoft realisation

The source schema is taken as the minimum contract. Microsoft realisation
notes per field:

| Field | Microsoft realisation |
| --- | --- |
| `event_id` | UUID v7 generated by the platform SDK or APIM event policy; partition key on the Fabric delta table. |
| `request_id` | Equals the OpenTelemetry `traceparent` so business and technical traces join in App Insights / ADX. |
| `agent_id` | Issued by Microsoft Entra Agent ID; immutable per agent. |
| `agent_name` | Sourced from the Entra Agent ID fleet record. |
| `environment` | Enforced by an APIM environment header; values constrained by APIM policy. |
| `business_domain`, `business_process`, `intent` | Controlled vocabularies held in Microsoft Purview Data Map; SDK rejects unregistered values. |
| `business_object_id` | Free text; expected pattern documented per process. |
| `event_type`, `outcome`, `status` | Enumerated by the schema; SDK and APIM event policy reject unknown values. |
| `event_timestamp_utc` | ISO 8601 UTC; SDK and APIM enforce. |
| `duration_ms`, `cost_amount` | Numeric; `cost_amount` derived from APIM token metric and infrastructure cost allocation in the Fabric semantic model. |
| `model_or_provider` | Sourced from APIM AI policy metadata. |
| `handoff_flag` | Boolean; drives the human-handoff-rate KPI. |
| `sensitivity_classification` | Aligned to Microsoft Purview sensitivity labels. |
| `extensions` (proposed addition) | Typed map; `extensions.schema_ref` identifies the registered domain extension schema. |

## 6. KPI baseline — Microsoft realisation

| KPI | Microsoft realisation |
| --- | --- |
| Agent request volume | Counted in App Insights for live SRE views; aggregated in the Fabric semantic model for business reporting. |
| Business completion rate | DAX measure on the gold-layer business events table. |
| Failure rate | Two measures: technical failure (App Insights) and business failure (Fabric). |
| Human handoff rate | DAX measure on `handoff_flag = true` / total attempted business outcomes. |
| Average turnaround time | DAX measure on business events; process-specific filters available. |
| Average cost per successful outcome | DAX measure combining APIM token cost and infrastructure cost (Azure Cost Management) per `agent_id`. |
| Security or access exceptions | Sourced from Microsoft Sentinel; surfaced in the security workbook and Power BI compliance dashboard. |

## 7. Persona-based dashboards

| Persona | Microsoft surface | Refresh |
| --- | --- | --- |
| Executive / leadership | Power BI executive app on the Fabric semantic model; RLS by business domain. | Daily. |
| Business owner / product owner | Power BI business-owner app per business domain. | 15 minutes. |
| Engineering / SRE / platform | Azure Monitor workbook suite + App Insights live metrics + Foundry tracing UI; optional Azure Managed Grafana. | Live. |
| Security / compliance | Microsoft Sentinel workbooks + Power BI compliance dashboard + Microsoft Purview Compliance Manager. | Live (Sentinel), daily (Power BI). |
| Finance / commercial | Power BI finance app combining APIM token metrics and Azure Cost Management views. | Daily. |

Dashboard owner, audience, source and refresh cadence are recorded per
dashboard in the LLD.

## 8. Operating model — minimum viable

The recommendation assumes a small set of operating roles. Microsoft tooling
supports each role natively:

| Role | Responsibility | Microsoft surface |
| --- | --- | --- |
| Agent owner | Owns one or more agents; maintains compliance evidence, approves changes. | Microsoft Entra Agent ID record; Foundry / Copilot Studio per-agent RBAC. |
| Platform engineer | Maintains the observability stack, the platform SDK, APIM policies, Fabric schemas. | Azure DevOps / GitHub repositories; Microsoft Entra PIM for elevated access. |
| SRE | Operates the stack, responds to alerts, runs DR drills. | Azure Monitor, App Insights, Azure Managed Grafana, ServiceNow. |
| Security analyst | Reviews policy events, runs investigations. | Microsoft Sentinel, Microsoft Defender for Cloud Apps. |
| Compliance officer | Ensures Responsible-AI and regulatory evidence is current. | Microsoft Purview Compliance Manager, Power BI compliance dashboard. |
| Business analyst | Defines and reviews KPIs and dashboards per business domain. | Microsoft Fabric, Power BI. |

## 9. Phased rollout

| Phase | Outcome | Components in scope |
| --- | --- | --- |
| Phase 1 — pilot (≈4 weeks) | One pilot agent observed end to end in a single environment. | Foundry tracing, APIM AI Gateway, Log Analytics, App Insights, Azure Monitor workbook, Microsoft Entra Agent ID registration. |
| Phase 2 — business events (≈4 weeks) | Pilot agent emits business events; one Power BI dashboard for one persona. | Platform SDK v1, Fabric Lakehouse and Eventstream, Power BI semantic model, Microsoft Purview Data Map schema registration. |
| Phase 3 — governance and NL query (≈4 weeks) | Fabric Data Agent live for one persona; Sentinel alerts on policy and overdue oversight; Compliance Manager populated. | Fabric Data Agent, Microsoft Sentinel rules, Foundry Continuous Evaluation, Microsoft Purview Compliance Manager. |
| Phase 4 — multi-surface (≈8 weeks) | One agent from each of Copilot Studio, Foundry prompt, Foundry hosted and one third-party vendor onboarded. | Copilot Studio App Insights export, Power Automate adaptor, vendor-specific adaptors / Sentinel connectors, Defender for Cloud Apps. |

Subsequent phases scale onboarding, harden DR, add Responsible-AI dashboards
and tune cost guardrails.

## 10. Known limitations and considerations

- **Microsoft Entra Agent ID** is the agent-specific identity primitive but
  fleet-management features around it are evolving. Where capabilities are
  still in preview, Microsoft Purview Compliance Manager and a small custom
  schema in OneLake fill the gaps for evidence reporting.
- **Copilot Studio Application Insights export** depends on the customer's
  Copilot Studio licensing tier; without it, business events for Copilot
  Studio agents are derived from Power Automate triggers and audit log
  ingestion only.
- **Foundry Continuous Evaluation** cost scales with sampling rate; production
  sampling rate is a per-agent decision and should be encoded in the agent
  record.
- **Fabric Data Agent** quality depends on semantic-model curation; budget
  ongoing data-product effort, not just initial setup.
- **Third-party vendor telemetry** varies. Each vendor needs an agreed
  minimum-viable-telemetry contract before onboarding; Microsoft Sentinel
  connector coverage is good but not universal.
- **Cost controls** matter most for high-volume agents — adopt APIM semantic
  caching, Log Analytics Basic Logs and Fabric capacity guardrails from
  phase 1, not as a later optimisation.

## 11. Change log

| Date | Version | Change | Author |
| --- | --- | --- | --- |
| 2026-06-22 | v1 | Initial Microsoft recommendation, independent of the OCTA HLD baseline. Built bottom-up from Microsoft platform capabilities and mapped to the source requirements. Explicitly covers Copilot Studio, Foundry prompt agents, Foundry hosted agents and third-party vendor agents. | Microsoft architecture |
