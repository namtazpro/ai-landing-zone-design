# AI Observability — requirements and Microsoft solution mapping

| Field | Value |
| --- | --- |
| Source asset | [../assets/AI Observability - HLR and Detailed Requirements.docx](../assets/AI%20Observability%20-%20HLR%20and%20Detailed%20Requirements.docx) |
| Source version | V0.1, 2 June 2026, Pankaj Arora |
| Response version | Draft v0.1 — 2026-06-22 |
| Response owner | Microsoft architecture (OCTA EA office) |
| Status | Draft — awaiting customer review |

## Purpose

This document is the workable companion to the customer's *AI Observability
HLR/DR* requirements document. It restates each requirement (risks, high-level
requirements, detailed functional requirements, non-functional requirements,
business event schema, KPI framework and personas) and pairs it with the
Microsoft solution we propose, together with status and notes that can be
updated in subsequent iterations.

Everything in the source asset is preserved verbatim where the wording carries
contractual meaning (acceptance criteria, NFR text). Microsoft commentary lives
in dedicated *Microsoft solution* and *Status / notes* columns or sub-sections
so the customer's text remains intact and reviewable.

## Microsoft solution proposition

Our response is anchored on three Microsoft platform pillars, supported by the
wider Azure and Microsoft 365 ecosystem.

| Pillar | Role in this solution |
| --- | --- |
| **Microsoft Entra Agent ID / Agent365** | Enterprise identity, registration, ownership and governance plane for every AI agent in scope, including third-party agents (SAP Joule, Copilot Studio, custom). Source of truth for the agent fleet inventory, compliance posture, lifecycle status, ownership, ethics and DPIA evidence references. |
| **Microsoft Foundry Control Plane** | Build, evaluate, deploy and continuously monitor AI agents and models. Hosts the prompt registry, evaluation runs (groundedness, relevance, coherence, safety), continuous evaluation jobs, content-safety filters, model lifecycle and per-project RBAC. Emits OpenTelemetry traces for all Foundry-hosted execution. |
| **Azure API Management — AI Gateway** | Single ingress for every LLM, MCP and agent API call. Enforces auth, rate limits, token quotas, semantic caching, content safety, jailbreak detection, load balancing, prompt/response logging, cost attribution headers and PII scrubbing before egress. |

These pillars are wired into the rest of the Microsoft platform:

| Capability | Microsoft component |
| --- | --- |
| Telemetry ingestion & tracing | Azure Monitor + Application Insights (OpenTelemetry-native), Foundry tracing, APIM diagnostic logs |
| Long-term storage & analytics | Log Analytics workspaces, Azure Data Explorer (Kusto) for trace and event analytics, Microsoft Fabric for business-event lakehouse and Direct Lake reporting |
| Dashboards | Azure Monitor workbooks (engineering/SRE), Power BI on Fabric (executive, business, finance), Microsoft Sentinel workbooks (security) |
| Governed natural language query | Fabric Data Agent (natural-language to KQL/SQL over curated lakehouse), enforcing RLS via Microsoft Fabric / OneLake security and Entra ID |
| Security, audit and compliance | Microsoft Sentinel, Microsoft Purview (sensitivity labels, data residency, retention), Microsoft Defender for Cloud, Entra ID Privileged Identity Management |
| Cost attribution | APIM token-counting policies, Azure Cost Management, Foundry usage metrics, Microsoft Fabric chargeback model |
| Human-in-the-loop & escalation | Power Automate flows + Microsoft Teams approvals, ServiceNow connector via APIM, Foundry agent action gates |
| Responsible AI evidence | Microsoft Purview Compliance Manager, Foundry Responsible AI dashboard, Azure AI Content Safety, Sentinel UEBA for bias / fairness signals |
| Low-code & external agents | Copilot Studio telemetry export, Microsoft 365 Copilot audit logs, MCP servers via APIM, custom adaptors for SAP Joule / SuccessFactors |

## Reading guide

- Tables follow the source numbering exactly so reviewers can cross-check.
- *Microsoft solution* columns name the primary component first, then supporting
  components. *Status* uses Proposed / Confirmed / Open / Gap (see
  [README.md](README.md)).
- Where a requirement is satisfied by a Microsoft platform default that the
  customer should adopt rather than build, the *Status* column says
  **Platform default**.

---

## 1. Glossary alignment

The source glossary is adopted as-is. Microsoft-specific terminology used in
this response:

| Term | Definition |
| --- | --- |
| Agent365 | Microsoft's enterprise agent management platform (preview), built on Entra Agent ID, providing fleet inventory, ownership, lifecycle and compliance reporting for AI agents across vendors. |
| Foundry Control Plane | The management surface of Microsoft Foundry (project, hub, deployment, evaluation, observability APIs). |
| AI Gateway (APIM) | Azure API Management configured with AI policies (`llm-token-limit`, `llm-emit-token-metric`, `llm-semantic-cache-store/lookup`, `llm-content-safety`). |
| Fabric Data Agent | Microsoft Fabric AI skill that turns natural-language questions into governed queries over a curated lakehouse, honouring OneLake and Entra ID security. |

---

## 2. Scope alignment

| Source scope item | Microsoft mapping | Status |
| --- | --- | --- |
| AI gateway and integration layer | APIM AI Gateway as single ingress for every model and MCP call. | Proposed |
| Operational observability — tracing, metrics, alerts, service health | Azure Monitor + App Insights + Foundry tracing, OpenTelemetry end to end. | Proposed |
| Developer / platform support — onboarding, testing, schema conformance, lifecycle | Foundry projects + Agent365 registration + onboarding gate in CI/CD. | Proposed |
| Enterprise governance — access, audit, retention, policy, agent-level oversight | Entra ID + Agent365 + Purview + Sentinel + Defender for Cloud. | Proposed |
| Business observability — standardised events, HITL, KPIs, decision support | Fabric lakehouse for business events, Power BI dashboards, Foundry HITL controls. | Proposed |
| Dev / Test / Prod separation | Foundry hub-and-project pattern + per-environment APIM + Bicep landing zones. | Proposed |
| Mandatory observability for all in-scope agents | Agent365 registration gate + APIM ingress enforcement + onboarding checks. | Proposed |
| Governed NL query | Fabric Data Agent over curated semantic model with Entra ID and OneLake security. | Proposed |
| Role-based dashboards | Power BI workspaces per persona + Azure Monitor workbooks for engineering. | Proposed |
| AI ethics artefacts — ownership, DPIA, bias, ethics reviews, governance decisions | Agent365 compliance fields + Purview Compliance Manager + Foundry Responsible AI dashboard. | Open — needs confirmation of evidence storage system |
| Internal and external AI systems / vendors | Agent365 vendor onboarding + Copilot Studio / SAP Joule connectors via APIM. | Open — vendor list to confirm |

Out-of-scope items in the source document are accepted as out of scope for this
response.

---

## 3. Risk register — Microsoft mitigations

Source: section 4.3 of the requirements document. Microsoft mitigation is in
addition to (or operationalises) the customer's mitigation, not a replacement.

| Ref | Risk (customer) | Likelihood | Customer mitigation | Microsoft mitigation | Status |
| --- | --- | --- | --- | --- | --- |
| 4.3.1 | Unauthorised or overly broad data exposure through governed NL query | Medium | Approved curated datasets, RBAC, RLS, audit log, no data modification. | Fabric Data Agent restricted to a curated lakehouse with OneLake item-level permissions and Fabric RLS roles; queries pass through Entra ID; all activity captured in Purview audit log and Sentinel; Data Agent runs in read-only mode with Defender for Cloud DLP policies on the workspace. | Proposed |
| 4.3.2 | Inconsistent / incomplete event data, weak schema adoption | Medium | Onboarding conformance checks, required-field validation, schema governance, regression tests. | Foundry onboarding gate runs schema conformance tests against the central Business Event Schema; APIM policy rejects events missing mandatory fields; schema registry held in Purview Data Map with breaking-change CI checks. | Proposed |
| 4.3.3 | Solution complexity exceeds delivery / onboarding / usability | Medium | Phased delivery, prioritised onboarding, role-based dashboards, measurable AC. | MVP phase delivers APIM + Foundry tracing + Log Analytics dashboards for one pilot agent; later phases add Fabric lakehouse, Data Agent and Sentinel correlation. Each phase mapped to AC in section 5.3 below. | Proposed |
| 4.3.4 | Security / privacy / compliance breach | Low | Privacy controls, audit logging, encryption, RBAC, retention, periodic review. | Microsoft Purview sensitivity labels on all event categories; CMK encryption in Log Analytics and Fabric; Defender for Cloud regulatory compliance pack mapped to ISO 27001 / GDPR; quarterly access reviews via Entra ID Identity Governance. | Proposed |
| 4.3.5 | Low adoption by agent teams | Medium | Onboarding standards, named owners, phased rollout, minimum compliance gates. | Agent365 makes registration mandatory before APIM grants production keys; templates published as `azd` blueprints; engineering scorecards in Foundry track onboarding KPIs. | Proposed |
| 4.3.6 | Cost growth — event volumes, retention, dashboard / query patterns | Medium | Retention tiers, archive rules, cost dashboards, query guardrails, periodic review. | Log Analytics commitment tiers + Basic Logs for high-volume telemetry; Archive tier for >90 days; Fabric capacity guardrails; APIM `llm-token-limit` and semantic caching to reduce model spend; Azure Cost Management views per agent and per business domain. | Proposed |
| 4.3.7 | Legacy / third-party agents cannot emit required events | Medium | Approved adaptors, minimum viable telemetry, prioritised onboarding. | APIM-fronted MCP adaptors for legacy systems (Maximo, SAP, ServiceNow already in scope per other KDDs); Copilot Studio telemetry export to App Insights; minimum viable telemetry pattern documented per adapter family. | Proposed |
| 4.3.8 | Incorrect KPI interpretation | Medium | Publish KPI definitions, owners, exclusions, thresholds. | KPI catalogue maintained as a Power BI semantic model with descriptions, owners and lineage shown via Microsoft Purview Data Catalog; review cadence enforced in Agent365 governance workflows. | Proposed |
| 4.3.9 | Compliance evidence (ownership, DPIA, ethics, vendor) incomplete or untraceable | Medium | Mandatory evidence per system, owners, review cadence, exception alerts. | Compliance evidence stored in Microsoft Purview Compliance Manager and referenced from Agent365 fleet records; dashboards in Power BI surface missing or expired evidence; Sentinel scheduled rule raises alerts on overdue items. | Open — confirm Purview Compliance Manager licensing position |
| 4.3.10 | Bias / fairness / proxy discrimination not detected early | High | Fairness monitoring, protected-characteristic rules, proxy review, bias audit evidence, threshold-based exceptions. | Foundry Responsible AI dashboard for groundedness, harm and fairness signals on every evaluation run; Azure AI Content Safety as APIM policy; demographic outcome monitoring in Fabric using protected-characteristic taxonomy stored in Purview; alerting via Sentinel UEBA. Mapped to Mitie *Responsible and Ethical AI Policy* requirements raised in source comment MA5. | Open — needs alignment session with Mitie AI Ethics owner |

---

## 4. High-level requirements (HLRs)

Source: section 5.1. The original "Microsoft comment" column was left empty in
the source; we populate it here.

| # | Requirement | Priority | Audience | Microsoft solution | Status |
| --- | --- | --- | --- | --- | --- |
| **R1** | Provide end-to-end traceability of AI agent execution across requests, orchestration steps, tool calls, model invocations, retrieval steps and downstream actions using correlation identifiers. | Must | Developers, SREs | OpenTelemetry traces emitted by Foundry, APIM AI Gateway and MCP adaptors, all carrying a common `traceparent`; ingested into Application Insights and projected into Azure Data Explorer for long-term querying. | Proposed |
| **R2** | Capture and report near-real-time operational metrics for in-scope AI agents (latency, request volume, error rate, token / consumption metrics, other agreed runtime indicators). | Must | SREs, Platform | APIM `llm-emit-token-metric` policy + Foundry runtime metrics + App Insights live metrics; surfaced via Azure Monitor workbooks per agent and per model. | Proposed |
| **R3** | Continuous evaluation of agreed output quality measures for production AI traffic (groundedness, relevance, coherence, etc.) where appropriate. | Must | Developers, Product | Foundry Continuous Evaluation jobs sampling production traffic; results stored as evaluation runs and surfaced in Foundry + Power BI. | Proposed |
| **R4** | Monitor safety controls, policy checks and content-filtering outcomes and alert on thresholds / exceptions. | Must | Security, Compliance | Azure AI Content Safety as APIM policy + Foundry safety evaluators; events sent to Microsoft Sentinel for alerting and case management. | Proposed |
| **R5** | Cost attribution and reporting by agent, model, environment and other agreed dimensions, including prompt / configuration variants where feasible. | Must | Finance, Product | APIM token metrics tagged with agent / project / environment; Azure Cost Management views for infra cost; Fabric chargeback model combining token cost + infra cost per agent. | Proposed |
| **R6** | Controlled prompt and configuration versioning, collaborative review / annotation, comparative testing (A/B). | Should | Developers | Foundry Prompt Flow and Prompt registry; Foundry deployment slots for A/B; integrated with Azure DevOps / GitHub for review workflows. | Platform default |
| **R7** | Auditable record of data access, configuration changes, query activity and observability data lineage. | Must | Compliance, Legal | Entra ID audit + Purview audit + Sentinel as SIEM; Fabric Data Agent query logs; lineage in Purview Data Map. | Proposed |
| **R8** | Enterprise governance — registration, access controls, fleet visibility, oversight of ownership / status / compliance posture. | Should | IT Admin, Security | Agent365 (Entra Agent ID) as registration and governance plane; integrates RBAC, ownership, lifecycle and compliance evidence. | Proposed |
| **R9** | Integration with approved enterprise monitoring, dashboarding and reporting services, including Azure-native and other agreed platforms. | Should | SREs, Platform | Azure Monitor / Sentinel / Power BI as defaults; Grafana via managed integration; ServiceNow via APIM connector for incident handoff. | Proposed |
| **R10** | Business observability — standardised business events, stakeholder dashboards, governed AI-assisted access to approved reporting data. | Must | Business users, Stakeholders | Business events in Fabric lakehouse using the schema in section 7 below; Power BI persona dashboards on top; Fabric Data Agent for NL access. | Proposed |
| **R11** | Observability across approved model providers / hosting patterns, multi-model or multi-platform scenarios. | Nice | Architecture | Foundry model catalogue covers Azure OpenAI, third-party models via Models-as-a-Service, and on-prem models via Foundry Local; APIM normalises observability across them. | Proposed |
| **R12** | Human-in-the-loop oversight for high-impact AI-supported decisions — review points, escalation, approvals, exceptions, overdue oversight. | Must | Compliance, Risk, Business Owners | Foundry agent action gates + Power Automate / Teams approval flows; Sentinel scheduled analytics for overdue oversight; events recorded against the business event schema. | Proposed |
| **R13** | Technical observability for low-code AI platforms (Copilot) and externally hosted agents (SAP Joule) using native telemetry, APIs, connectors or adaptors. | Should | Architecture, Platform, Security | Copilot Studio telemetry export to App Insights; Microsoft 365 Copilot audit logs to Purview / Sentinel; APIM-fronted adaptors for SAP Joule and other SaaS agents emitting the central business event schema. | Open — adaptor design needed per SaaS vendor |

---

## 5. Detailed functional requirements

Source: section 5.3. Each requirement keeps the source text intact. Microsoft
solution and status follow.

### FR-TECH-001 — End-to-End Layered Architecture

The platform shall provide an end-to-end AI observability architecture across
Development, Test and Production environments that supports technical
telemetry, business event capture, security controls, dashboards and governed
query access for all in-scope AI agents.

- **Pre-requisites**: Azure environment available; AI agents deployed.
- **Acceptance criteria**: documented architecture covers telemetry ingestion,
  business event storage, IAM, dashboarding, alerting and governed query;
  Dev/Test/Prod separated; at least one representative in-scope agent onboarded
  end to end.
- **Microsoft solution**: reference architecture pattern is the OCTA Agentic
  Platform HLD in [../docs/HLD.md](../docs/HLD.md), layered as
  APIM AI Gateway → Foundry Control Plane → Agent runtime (Foundry-hosted,
  Copilot Studio, external) → telemetry plane (App Insights + Log Analytics +
  ADX) → business event plane (Fabric lakehouse) → reporting plane (Power BI,
  Workbooks, Fabric Data Agent). Dev/Test/Prod realised through per-environment
  Foundry hubs and APIM instances deployed via Bicep landing zones.
- **Status**: Proposed.

### FR-TECH-002 — Mandatory Agent Logging

All in-scope AI agents shall emit structured observability records for each
request and each business event to the central observability platform using
the approved schema and mandatory fields defined in this document.

- **Pre-requisites**: logging framework deployed.
- **Acceptance criteria**: request records with unique IDs, agent ID,
  environment, timestamp, status, duration, model / tool usage and correlation;
  business events with mandatory business fields; ≥95% conformance on sampled
  events before production approval.
- **Microsoft solution**: Foundry agents emit OpenTelemetry by default; APIM
  AI Gateway enriches every call with `agent_id`, `environment`, `traceparent`
  and tenant headers; business events emitted via a small SDK (NuGet / npm /
  PyPI) maintained by the platform team that wraps `azure-monitor-opentelemetry`
  and writes to the Fabric lakehouse via Event Streams. Conformance enforced by
  an APIM validation policy and a Foundry onboarding gate.
- **Status**: Proposed.

### FR-TECH-003 — Centralised Event Schema

The platform shall provide a central event schema with mandatory core fields
and controlled extension fields for department-specific business contexts.

- **Pre-requisites**: schema definition agreed.
- **Acceptance criteria**: mandatory fields for identity, agent, environment,
  business context, outcome, timestamps, status, correlation, classification;
  extensions through an approved mechanism that does not change existing field
  meanings; existing queries and dashboards continue to function on extension.
- **Microsoft solution**: schema modelled in Microsoft Purview Data Map with
  versioning; mandatory and optional fields described in section 7 below;
  extension model uses a typed `extensions` object plus a registered schema
  ID per business domain; CI pipeline runs `pyarrow` schema diffs on every PR
  and rejects breaking changes.
- **Status**: Proposed.

### FR-TECH-004 — Monitoring & Alerting

The platform shall monitor technical and business observability signals and
raise alerts on threshold or abnormal-condition breaches.

- **Pre-requisites**: monitoring configured; ServiceNow integration available.
- **Acceptance criteria**: alert rules for latency, error rate, failed
  executions, missing event ingestion, business outcome thresholds; each rule
  has severity, owner, channel, remediation; ServiceNow incidents on
  qualifying alerts.
- **Microsoft solution**: Azure Monitor metric and log alerts for technical
  signals; Microsoft Sentinel scheduled analytics for security and policy
  events; Fabric Data Activator for business-outcome thresholds; ServiceNow
  integration via APIM-fronted REST connector.
- **Status**: Proposed.

### FR-TECH-005 — Alert Severity & Response SLA

The platform shall define alert severity levels and response service levels
for technical, business, security and data-quality alert categories.

- **Pre-requisites**: alert categories, owners and operating model agreed.
- **Acceptance criteria**: per-type severity mapping; per-severity SLAs for
  acknowledgement, investigation, updates, resolution; documented support
  ownership and out-of-hours handling; service-management incidents inherit
  severity and route correctly.
- **Microsoft solution**: severity / SLA matrix encoded as Azure Monitor
  action groups + Sentinel automation rules; out-of-hours routing via
  Microsoft Teams + on-call schedules in Azure Monitor; ServiceNow priority
  mapping configured in the APIM connector.
- **Status**: Open — requires customer-side support model confirmation before
  encoding SLAs.

### FR-TECH-006 — Data Storage & Retention

The platform shall store observability and business event data in line with an
approved retention policy defining periods, archive and deletion rules per
data category.

- **Pre-requisites**: storage platform provisioned.
- **Acceptance criteria**: documented retention policy per data category;
  enforcement automated or scheduled; auditable deletion with exception
  support.
- **Microsoft solution**: Log Analytics interactive + Basic Logs + Archive
  tiers per category; Fabric OneLake for business events with Purview
  retention labels; Microsoft Purview Data Lifecycle Management for policy
  enforcement and auditable purges.
- **Status**: Proposed.

### FR-TECH-007 — Low-Code and External Agent Observability

The platform shall support onboarding and monitoring of approved low-code AI
platforms and externally hosted AI agents, including cases where direct
instrumentation is not available.

- **Pre-requisites**: approved onboarding pattern; provider telemetry / API /
  connector / adaptor identified.
- **Acceptance criteria**: minimum agreed observability record per agent;
  documented telemetry limitations and provenance; at least one representative
  external agent onboarded end to end.
- **Microsoft solution**: Copilot Studio telemetry export to App Insights;
  Microsoft 365 Copilot audit logs forwarded to Sentinel via the standard
  data connector; SAP Joule and SuccessFactors integrated via APIM-fronted
  REST and OData adaptors that translate vendor telemetry into the central
  business event schema; minimum viable telemetry contract documented per
  vendor in the LLD.
- **Status**: Open — confirm vendor list and contractual access to telemetry.

### FR-SEC-002 — Row-Level Security

The system shall implement database-level row-level security.

- **Pre-requisites**: data model defined.
- **Acceptance criteria**: users cannot query unauthorised rows; security
  applies to all access methods.
- **Microsoft solution**: Fabric workspace RLS and OneLake item-level
  permissions; SQL endpoints (Lakehouse SQL endpoint, Synapse Serverless)
  inherit Fabric RLS; Power BI semantic models reuse the same RLS roles; Data
  Agent queries execute under the user's Entra ID context.
- **Status**: Proposed.

### FR-BUS-001 — Business Event Tracking

The platform shall capture standardised business events for AI agent
activities so that business intent, outcome and operational status can be
measured consistently across departments.

- **Acceptance criteria**: events include business intent, outcome, status,
  context IDs per the schema in section 7; reporting by department, agent,
  process, environment, outcome and period; samples distinguish success,
  failure, partial success, handoff and no-action.
- **Microsoft solution**: business events produced via the platform SDK
  (FR-TECH-002), streamed to a Fabric lakehouse via Event Streams; gold-layer
  delta tables modelled per business domain; semantic model in Power BI
  publishes the outcome taxonomy.
- **Status**: Proposed.

### FR-BUS-002 — AI Query Agent

The system shall provide an AI agent that converts natural language queries
into SQL.

- **Pre-requisites**: data schema available.
- **Acceptance criteria**: plain-English querying; SQL generated dynamically;
  results respect RBAC + RLS; output structured (tables only).
- **Microsoft solution**: Microsoft Fabric Data Agent over the curated
  lakehouse semantic model; queries execute under the user's Entra ID
  context and inherit Fabric RLS / OneLake permissions; structured table
  output by default; conversation logs captured in Purview audit.
- **Status**: Proposed.

### FR-EXEC-001 — Dashboarding

The platform shall provide role-based dashboards that present approved
technical, operational and business KPIs for the agreed stakeholder groups.

- **Pre-requisites**: data model implemented.
- **Acceptance criteria**: at least one dashboard per stakeholder group;
  filtering by time / environment / agent / department / process; RBAC on
  dashboards and underlying data.
- **Microsoft solution**: Power BI app workspaces per persona (executive,
  business owner, finance, compliance) on top of the Fabric semantic model;
  Azure Monitor workbooks for engineering / SRE; Sentinel workbooks for
  security; all secured via Entra ID groups.
- **Status**: Proposed.

### FR-EXEC-002 — KPI Framework

The service shall define and publish a baseline KPI framework covering usage,
reliability, business outcomes, cost and governance measures.

- **Acceptance criteria**: per-KPI name, description, formula, source fields,
  owner, cadence, audience; calculable from stored data without manual
  spreadsheets; baseline includes volume, success, failure, handoff, latency,
  cost, governance.
- **Microsoft solution**: KPI definitions encoded as DAX measures in the
  Fabric semantic model with description and owner metadata; lineage exposed
  via Purview; review workflow operated by the Agent365 governance team. See
  section 8 below for the baseline measure set with Microsoft notes.
- **Status**: Proposed.

### FR-CMP-001 — Human Oversight and Escalation

The platform shall support reporting and alerting for human review and
escalation controls for AI-supported decisions that may significantly affect
safety, employment, legal rights or other high-impact outcomes.

- **Acceptance criteria**: record when human review is required / invoked /
  bypassed / completed; report escalation paths, approvers and exception
  outcomes; alert on missing or overdue oversight.
- **Microsoft solution**: Foundry agent action gates raise approval requests
  through Power Automate to Microsoft Teams; outcome of the approval written
  back as a business event (event types: `review_required`, `review_completed`,
  `review_bypassed`); Sentinel scheduled rules raise alerts on missing or
  overdue reviews; Power BI compliance dashboard tracks throughput and aging.
- **Status**: Proposed.

---

## 6. Non-functional requirements

Source: section 6. Source text preserved; Microsoft solution and status added.

| Ref | Description (source) | Category | MoSCoW | Microsoft solution | Status |
| --- | --- | --- | --- | --- | --- |
| NFR.SEC.1 | All observability, business event, audit and query data shall be encrypted in transit using approved transport security controls and encrypted at rest using approved key management controls. Test evidence shall demonstrate encryption is enabled for all production data stores and network paths. | Security | Must | TLS 1.2+ enforced everywhere (APIM, Azure Monitor ingestion, Fabric); CMK on Log Analytics, ADX and Fabric with Key Vault; Defender for Cloud regulatory compliance checks. | Proposed |
| NFR.SEC.2 | The platform shall audit log all administrative access, dashboard access, governed query requests, security policy changes and data access attempts. Records include timestamp, identity, action, target, outcome, correlation. | Security | Must | Entra ID sign-in and audit logs + Microsoft Purview audit + Fabric audit + APIM diagnostics, all forwarded to a Sentinel workspace as the audit system of record. | Proposed |
| NFR.PER.1 | The platform shall publish and meet approved performance targets for telemetry ingestion, dashboard refresh and governed query response. Includes ingestion window, dashboard refresh cadence and query SLA. | Performance | Must | Targets: ≤30 s ingestion lag (App Insights + Log Analytics), Fabric semantic-model refresh on 15-min cadence in production, P95 NL query ≤8 s on curated lakehouse. Final targets confirmed during design. | Open — targets to confirm with customer |
| NFR.SCL.1 | The platform shall scale to growth in onboarded agents, event volume, retained history, concurrent dashboards and queries without redesign of the core data model. Capacity assumptions and scale test evidence shall be documented. | Scalability | Must | Log Analytics multi-workspace pattern with per-domain workspaces fronted by ADX cross-cluster queries; Fabric capacity sized per environment with autoscale and pause/resume; APIM premium with regional units. Load test pack delivered via Azure Load Testing. | Proposed |
| NFR.AVL.1 | The platform shall have a defined availability target for production services covering ingestion, dashboards and governed query, excluding approved maintenance. | Availability | Must | Target 99.9% on the user-facing surfaces; underlying Azure SLAs aggregated and published in the operating handbook. | Open — target to confirm |
| NFR.RES.1 | The platform shall provide resilience controls to prevent single points of failure for critical production components and recover from transient downstream failures. | Resilience | Must | Zone-redundant deployments for APIM, Log Analytics, Fabric and ADX; retry / circuit-breaker policies on APIM; Foundry hubs in paired regions where required. | Proposed |
| NFR.DR.1 | The service shall define DR objectives (RTO / RPO) for critical data and components and maintain a tested recovery procedure. | DR | Must | Default RTO 4 h, RPO 1 h for tier-1 data; geo-replicated storage; Fabric mirroring; annual DR drill documented in the operating handbook. | Open — targets to confirm |
| NFR.SUP.1 | The service shall define an operating and support model covering ownership, hours, severity, escalation and change approval. | Support | Must | Operating handbook delivered in design phase; integrates with customer's ServiceNow; change approval via Azure DevOps + Entra PIM. | Open — needs joint definition |
| NFR.DQ.1 | The platform shall define and monitor data quality controls for required fields, duplicates, schema conformance and timeliness. | Data Quality | Must | Fabric Data Quality rules + Microsoft Purview Data Quality scans; APIM schema validation as first line; Data Activator alerts on DQ breaches. | Proposed |
| NFR.CMP.1 | The platform shall process / store / retain / delete personal or sensitive data in line with approved privacy, lawful processing, retention and data residency. Where prompts / responses / IDs may contain personal data, masking, minimisation, access control and deletion controls shall apply. | Compliance | Must | Purview sensitivity labels and DLP on every data store; APIM PII detection policy on requests / responses with optional redaction before storage; EU data residency enforced by region policy; right-to-erasure via Purview eDiscovery + custom purge runbook. | Proposed |
| NFR.CMP.2 | The platform shall ensure required responsible-AI evidence per in-scope AI system (owner, lifecycle, risk, DPIA, bias, governance, approval) is stored or referenced in a reportable, auditable, attributable way. | Compliance | Must | Compliance evidence captured against the Agent365 agent record (owner, lifecycle, DPIA reference, bias-assessment status, ethics-review status, approval status); evidence artefacts stored in Purview Compliance Manager; reporting in Power BI compliance dashboard. | Open — confirm Compliance Manager licensing |

---

## 7. Business event schema

Source schema (section 5.3) is preserved as the minimum mandatory contract.
Microsoft notes apply across all events.

| Field | Type | Description | Microsoft note |
| --- | --- | --- | --- |
| event_id | String | Unique identifier for the business event record. | UUID v7 generated by the SDK; partition key in the Fabric lakehouse. |
| request_id | String | Identifier linking the event to the underlying agent request or execution trace. | Maps directly to the OpenTelemetry `traceparent` so business and technical traces join. |
| agent_id | String | Unique identifier of the AI agent or service. | Issued by Agent365 (Entra Agent ID); immutable per agent. |
| agent_name | String | Readable name of the AI agent. | Sourced from the Agent365 fleet record. |
| environment | String | Dev / Test / Production. | Enforced by APIM environment header. |
| business_domain | String | Business domain (EFF, HR, ...). | Controlled vocabulary held in Purview. |
| business_process | String | Named business process or workflow step. | Controlled vocabulary held in Purview per domain. |
| business_object_id | String | Identifier of the business object (case, ticket, order, request). | Free text, expected pattern documented per process. |
| event_type | String | Created, attempted, completed, failed, escalated, handed off. | Enumerated; SDK rejects unknown values. |
| intent | String | Intended business purpose, approved taxonomy. | Taxonomy held in Purview; reviewed per domain. |
| outcome | String | Success, failed, partial success, no action, human handoff. | Enumerated. |
| status | String | Started, completed, failed, cancelled, timed out. | Enumerated. |
| event_timestamp_utc | Datetime | UTC timestamp of the event. | ISO 8601, UTC enforced. |
| duration_ms | Number | Elapsed duration. | Long. |
| cost_amount | Number | Direct or estimated cost. | Computed from APIM token metric + infra cost allocation. |
| model_or_provider | String | Model / provider / major runtime component. | Sourced from APIM AI policy metadata. |
| handoff_flag | Boolean | Process handed to human or downstream non-AI process. | Drives the human handoff rate KPI. |
| sensitivity_classification | String | Classification for governance / access control. | Aligned to Microsoft Purview sensitivity labels. |

Microsoft addition for review: an `extensions` object (typed map) for
domain-specific fields, with the schema ID held in `extensions.schema_ref`.
Recorded here as a proposal under FR-TECH-003.

---

## 8. KPI framework

Source KPIs (section 5.3) preserved; Microsoft notes added.

| KPI | Definition / formula | Audience | Microsoft solution |
| --- | --- | --- | --- |
| Agent request volume | Count of agent requests in period. | Executive, Product, Engineering | Computed in Fabric semantic model; live counterpart in App Insights for SRE. |
| Business completion rate | Completed business outcomes / total attempted. | Executive, Product, Business Owner | DAX measure on gold-layer business events. |
| Failure rate | Failed executions or business outcomes / total. | Engineering, Product, Executive | Split into technical-failure (App Insights) and business-failure (Fabric) measures. |
| Human handoff rate | Events with `handoff_flag = true` / total attempted. | Business Owner, Product, Operations | DAX measure; trending in the business owner dashboard. |
| Average turnaround time | Average duration between start and completion of the relevant process / event. | Executive, Business Owner, Engineering | DAX measure; process-specific filters. |
| Average cost per successful outcome | Total attributed cost / number of successful business outcomes in period. | Finance, Product, Executive | Token cost (APIM) + infra cost (Cost Management) allocated per `agent_id`. |
| Security or access exceptions | Count of blocked unauthorised access attempts, policy violations or relevant security exceptions in period. | Security, Compliance | Sourced from Sentinel; surfaced in the security workbook and Power BI compliance dashboard. |

---

## 9. Personas and dashboards

Source: section 5.3. Microsoft mapping per persona:

| Persona | Primary need | Microsoft surface |
| --- | --- | --- |
| Executive / Leadership | Business value, adoption, risk, cost. | Power BI executive app, refreshed daily, with semantic-model RLS by business domain. |
| Business Owner / Product Owner | Process outcomes, adoption, failure points, handoffs. | Power BI business-owner app per domain, refreshed every 15 minutes. |
| Engineering / SRE / Platform | Incidents, performance, reliability. | Azure Monitor workbook suite + Application Insights live metrics + Foundry tracing UI. |
| Security / Compliance | Access, policy compliance, audit. | Sentinel workbooks + Power BI compliance dashboard + Purview Compliance Manager. |
| Finance / Commercial | Cost efficiency, drivers. | Power BI finance app sourcing APIM token metrics + Azure Cost Management views. |

Dashboard requirements from the source are all satisfied by this stack; each
dashboard owner, audience, source and refresh cadence will be recorded in the
LLD when authored.

---

## 10. Open items and decisions needed

The following items must be resolved before the response can move from Draft
to v1.0. Each should be logged as an Open Question under
[../open-questions/](../open-questions/) when picked up.

| # | Topic | Why it matters | Suggested next step |
| --- | --- | --- | --- |
| 1 | Confirm customer-side ServiceNow integration model and severity / SLA matrix (FR-TECH-005, NFR.SUP.1). | Drives APIM connector design and alert automation. | Joint operating model workshop. |
| 2 | Confirm Purview Compliance Manager licensing position (NFR.CMP.2, risk 4.3.9). | Required to host responsible-AI evidence centrally. | Licensing review with customer procurement. |
| 3 | Vendor list for FR-TECH-007 / R13 (SAP Joule, SuccessFactors, others). | Determines adaptor backlog. | Inventory call with customer AI office. |
| 4 | Performance, availability and DR targets (NFR.PER.1, NFR.AVL.1, NFR.DR.1). | Drives sizing and DR design. | Targets workshop. |
| 5 | Bias / fairness monitoring approach (risk 4.3.10). | High-likelihood risk; aligns to *Responsible and Ethical AI Policy*. | Session with Mitie AI Ethics owner referenced in source comment MA5. |
| 6 | Schema extension governance for FR-TECH-003. | Long-term schema stability across domains. | Propose KDD on Purview Data Map ownership. |

---

## 11. Change log

| Date | Version | Change | Author |
| --- | --- | --- | --- |
| 2026-06-22 | Draft v0.1 | Initial Microsoft response derived from source V0.1 (2 June 2026). Microsoft proposition aligned on Agent365, Foundry Control Plane and APIM AI Gateway. | Microsoft architecture (OCTA EA office) |
