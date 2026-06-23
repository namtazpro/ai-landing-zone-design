IS High-Level/Detailed Requirements Document

|  |  |
| --- | --- |
| Change/Project reference: | AI Observability |
| Heading: | PRIO |

***Change
History***

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created / Updated** | **Details of Change** | **Author (s) or  Updated by** |
| V0.1 | 02/06/2026 | Initial Draft | Pankaj Arora |
|  |  |  |  |

***Glossary***

|  |  |
| --- | --- |
| **Abbreviation / Term** | **Definition** |
| CAFM | **C**omputer **A**ided **F**acilities **M**anagement system. (In this project the CAFM in use is IBM’s enterprise asset management software ‘Maximo’)  Note: Maximo has its own direct access web-based user interface.  https://fortemaximo.mitie.com/maximo/webclient/login/login.jsp |
| FR | **F****unctional** **R****equirement** |
| NFR | **N****on-****F****unctional** **R****equirement** |
| SR | **S****ervice** **R****equest  Sometimes referred to as ‘Job’ or ‘SR Job’** |
| WO | **W**ork **O**rder |

***Key Terminology***

|  |  |
| --- | --- |
| **Term** | **Definition** |
| AI Agent | A software system powered by a large language model (LLM) that can reason about tasks, make decisions, use tools (such as search, email, or databases), and take actions autonomously or semi-autonomously on behalf of a user. |
| Large Language Model (LLM) | The AI “brain” behind agents. Models like GPT-4o, Claude, or Gemini that understand and generate human language. They are accessed via cloud APIs and charged by token usage. |
| Observability | The ability to understand the internal state and behaviour of a system by examining its external outputs. In traditional software, this means logs, metrics, and traces. For AI systems, it extends to prompt/response quality, token costs, safety violations, and model drift. |
| Tracing | Recording the full execution path of a request as it flows through multiple services, models, and tools. In AI agents, a single user query may trigger multiple LLM calls, tool invocations, and retrieval steps—tracing captures all of these as a connected timeline. |
| Token | The basic unit of text that LLMs process. Roughly, one token equals about 0.75 words. Tokens directly determine cost: every prompt and response consumes tokens, and cloud providers charge per token. |
| Prompt Engineering | The practice of designing and refining the instructions (prompts) given to an LLM to achieve desired outputs. Observability tools help by tracking which prompt versions produce better results. |
| Groundedness | A quality metric that measures whether an AI’s response is supported by the source data it was given. Low groundedness indicates the model is “hallucinating”—generating plausible but unsupported claims. |
| RAG (Retrieval-Augmented Generation) | A pattern where the AI retrieves relevant documents from a knowledge base before generating a response. This improves accuracy but introduces additional components (search, vector databases) that need monitoring. |
| OpenTelemetry (OTel) | An open-source, vendor-neutral standard for collecting telemetry data (traces, metrics, logs) from software systems. It prevents lock-in to any single observability vendor and is the foundation for most modern AI observability tools. |
| MCP (Model Context Protocol) | An emerging open protocol that standardises how AI agents connect to external tools and data sources. It is supported by Azure Foundry and enables agents to securely invoke databases, APIs, and enterprise systems. |
| Model Drift | When an AI model’s behaviour changes over time—either because the provider updates the model or because the input data patterns shift—causing previously reliable outputs to degrade. |
| Guardrails | Automated rules and filters that prevent AI agents from producing harmful, off-topic, or policy-violating outputs. Observability tools monitor whether guardrails are being triggered and how often. |
| AI Gateway | A specialised API gateway that sits between your applications and LLM providers. It manages authentication, rate limiting, token quotas, load balancing across model deployments, semantic caching, and content safety filtering. Think of it as a traffic controller for all AI API calls. |
| Agent Orchestration Platform | A platform that discovers, registers, routes, and governs AI agents across an organisation. It ensures agents from different teams, vendors, and platforms can work together securely rather than operating as disconnected silos. |
| A2A (Agent-to-Agent Protocol) | An open protocol that enables AI agents to communicate and collaborate with each other, regardless of which platform or framework they were built on. Complementary to MCP, which handles agent-to-tool connections. |
| Semantic Caching | A technique where previous LLM responses are cached and reused for semantically similar (not just identical) prompts. This reduces token consumption, lowers costs, and improves response times. |

Contents

1.     Introduction. 5

1.1.       Document
Purpose. 5

2.     Business
Need. 5

2.1.       Project
Background. 5

2.2.       Objective(s) 5

2.3.       Scope. 6

2.4.       Out of
Scope. 7

3.     Business
Processes/Models/Overview.. 8

4.     Assumptions,
Dependencies, Risks & Constraints. 9

4.1.       Assumptions. 9

4.2.       Dependencies. 9

4.3.       Risks
& Issues. 9

4.4.       Constraints. 11

5.     Functional
Requirements. 12

5.1.       High
Level Requirements. 12

5.2.       Detailed
Requirements. 13

6.     Non-Functional
Requirements. 21

7.     Requirement
Traceabilty Matrix. 23

8.     Document
Review and Sign Off. 23

---

# 1.   Introduction

## 1.1.       Document Purpose

This
document defines the high-level and detailed requirements for an enterprise AI
Observability capability that will monitor, govern and report on AI agent
activity across the organisation.
It is intended to provide a common basis for review, design, delivery,
governance and approval by business stakeholders, product owners, architecture,
security, operations and technical teams.

# 2.   Business Need

## 2.1.       Project Background

Mitie is deploying AI agents across multiple business functions and delivery
teams. As adoption increases, a consistent enterprise approach is required to
observe how these agents operate, what business outcomes they produce, what
risks they introduce and what value they deliver.
At present, the organisation does not have a single, governed capability for
technical tracing, business outcome reporting, cost visibility,
access-controlled reporting and governed query access across the AI agent
estate.

·
No standardised enterprise mechanism to trace AI agent requests,
actions, dependencies and execution outcomes across teams.

·
Limited ability to measure business outcomes, handoffs,
exceptions, completion rates and value delivered by AI-supported processes.

·
No governed, role-based mechanism for stakeholders to query
observability and business reporting data across the AI estate.

This initiative will establish a governed AI observability
capability that provides technical telemetry, business event reporting,
stakeholder-specific dashboards and controlled query access across in-scope AI
agents.

## 2.2.       Objective(s)

·
Establish an end-to-end AI observability capability covering
telemetry, business event capture, dashboards, governed query access and
security controls for in-scope AI agents.

·
Enable measurement of business outcomes, process performance,
handoffs, failures and value indicators in addition to technical metrics.

·
Provide governed natural language query capability for authorised
users against approved curated observability and business reporting datasets.

·
Ensure that observability data, dashboards and query results are
protected through approved role-based access controls, row-level restrictions
and audit logging where required.

·
Provide role-based dashboards for executive, business,
engineering, security and operational stakeholders with actionable KPIs and
filtered views appropriate to each audience.

## 2.3.       Scope

·
Implementation of an end-to-end observability architecture for
in-scope AI agents covering the following capability layers:

o
AI gateway and integration layer for capturing requests, model
usage and execution context where applicable.

o
Operational observability for tracing, metrics, alerts and
service health monitoring.

o
Developer and platform support capabilities for onboarding,
testing, schema conformance and lifecycle management.

o
Enterprise governance for access control, auditability,
retention, policy enforcement and agent-level oversight.

o
Business observability for standardised business event capture,
human in the loop reporting, KPI reporting and stakeholder decision support.[MA1] [PA2]

·
Provisioning and support of Development, Test and Production
environments with separated configuration, deployment controls and access
management.

·
Mandatory observability and business event logging for all
in-scope AI agents and approved supporting components.

·
Governed natural language query capability for approved
observability and business datasets, subject to security and audit controls.

·
Role-based dashboards and reporting views for agreed stakeholder
personas.

o
Secure access, audit logging and policy enforcement across
storage, dashboards, query interfaces and supporting services.

·
Monitoring of AI ethics artefacts and approvals, including
ownership, risk assessments, DPIA status, bias audits, ethical reviews and
governance decisions where applicable.

·
Monitoring of internal and externally sourced AI systems and
vendors where they are in scope for responsible AI, privacy, fairness, security
or contractual compliance obligations.

## 2.4.       Out of Scope

·
General observability for non-AI systems except where those
systems are required to support, integrate with or contextualise in-scope AI
agent monitoring.

·
Creation of standalone manual reporting processes or
spreadsheet-based reporting outside the governed observability capability.

·
Replacement of source business applications, operational systems
or core process platforms used by departments adopting AI agents.[MA3] [PA4]

·
Execution of formal ethics approvals, legal determinations, DPIA
completion or governance board decision-making processes, except for storing,
tracking and reporting their status and outcomes where such evidence is
required for observability and compliance reporting.

·
Jeopardy management, handling of exceptions, and the execution of
human-in-the-loop actions are not in scope.

# 3.   Business Processes/Models/Overview

This section provides a top-down view of the AI observability
capability described in this document. The overall model can be understood in
three complementary sections: **Technical observability**, which captures
runtime execution, health and control signals; **Business observability**,
which captures business events, outcomes and process performance; and **Dashboards**,
which present role-based views of approved data for different stakeholder
groups.
Together, these three sections provide an end-to-end view from AI agent
execution through to business impact and governed stakeholder reporting.

·
**Technical observability** covers how AI agents execute
requests, tasks, jobs or workflow steps within defined technical contexts and
how their telemetry is captured.

·
It includes structured records for execution steps, model usage,
tool calls, performance, failures, alerts and service health using approved
schemas and central storage.

·
**Business observability** covers how AI-driven activity is
translated into measurable business events, outcomes, statuses, handoffs and
process indicators.

·
It enables approved data to be stored and analysed in a governed
way so that business value, completion patterns, failure trends and operational
impact can be reported consistently across departments.

·
**Dashboards** provide the stakeholder-facing reporting layer
through which authorised users consume approved technical and business
observability data.

·
These dashboards support role-based reporting, auditability and
governed query access for executive, business, engineering, security and
operational audiences.

1.     Role-based
dashboards for operational, business, executive and compliance reporting.

2.     Governed
natural language query capability for authorised users against approved curated
datasets.



The model supports multiple domains and workstreams, such as EFF,
HR and others, while allowing each area to map its local process concepts to a
shared core observability model. This allows different definitions of work
items, such as job, request, case or task, to be reported consistently without
losing domain-specific meaning.



# 4.   Assumptions, Dependencies, Risks & Constraints

## 4.1.       Assumptions

·
In-scope AI agents and approved supporting platform components
will emit the telemetry and business events required for central observability.

·
Named engineering, platform and business owners will be assigned
for service design, onboarding, operations and change approval before
production rollout.

·
Azure is the preferred enterprise hosting and integration
platform unless an exception is explicitly approved through enterprise
architecture and security governance.

·
Authorised business users may use governed natural language
querying where approved curated datasets, role permissions and audit controls
are in place.

## 4.2.       Dependencies

·
In-scope AI agent frameworks and runtimes must support the
approved telemetry and business event emission approach or provide an approved
adaptor.

·
Approved CI/CD tooling must support deployment automation,
environment separation, approval gates and infrastructure release management
for this service.

·
Approved monitoring and alerting tooling must support technical
and business alert evaluation, notification routing and operational integration
for in-scope events.

·
Where operational support integration is required, ServiceNow
support incident creation, ownership routing and status synchronisation for
qualifying alerts.

·
Applicable data governance, privacy, security, retention and
access control policies must be defined and available before production data
onboarding.

## 4.3.       Risks & Issues

|  |  |  |  |
| --- | --- | --- | --- |
| **Ref** | **Risk** | **Risk likelihood to occur** | **Mitigation** |
| 4.3.1 | Unauthorised or overly broad data exposure through governed natural language query capability | Medium | Restrict querying to approved curated datasets, enforce RBAC and row-level security, audit log access and prohibit data modification actions. |
| 4.3.2 | Inconsistent or incomplete event data caused by weak schema adoption, missing mandatory fields or uncontrolled extensions | Medium | Use onboarding conformance checks, required field validation, approved schema governance and dashboard query regression testing. |
| 4.3.3 | Solution complexity exceeds delivery capacity, onboarding needs or stakeholder usability requirements | Medium | Apply phased delivery, prioritised onboarding, role-based dashboards and measurable acceptance criteria for each release increment. |
| 4.3.4 | Security, privacy or compliance breach caused by weak controls, misconfiguration or inappropriate data retention and access handling | Low | Apply approved privacy controls, audit logging, encryption, role-based access control, retention policy enforcement and periodic control review. |
| 4.3.5 | Low adoption by agent teams leading to incomplete onboarding and limited business value. | Medium | Define onboarding standards, named owners, phased rollout and minimum compliance gates for production use. |
| 4.3.6 | Cost growth due to high event volumes, long retention periods, dashboard demand or expensive query patterns. | Medium | Define retention tiers, archived storage rules, cost dashboards, query guardrails and periodic cost review. |
| 4.3.7 | Legacy or third-party agents cannot emit the required events without significant custom integration effort. | Medium | Allow approved adaptors, define minimum viable telemetry and prioritise onboarding based on business value and feasibility. |
| 4.3.8 | Incorrect KPI interpretation leads to poor decisions or false confidence in automation outcomes. | Medium | Publish KPI definitions, owners, exclusions, thresholds and caveats, and review them with business stakeholders. |
| 4.3.9 | Required policy evidence such as ownership, DPIA status, risk assessments, ethical reviews, governance approvals or vendor compliance records is incomplete, outdated or not traceable for audit and assurance. | Medium | Make compliance artefacts mandatory for in-scope systems, assign owners, define review cadence and surface missing evidence through dashboard exceptions and alerts. |
| 4.3.10 | Bias, fairness or proxy discrimination risks are not detected early enough because protected characteristic usage, proxy features or demographic outcome patterns are not being monitored consistently. | High | Define fairness monitoring requirements, protected characteristic handling rules, proxy feature review, bias audit evidence capture and threshold-based exception reporting. |

## 4.4.       Constraints

·
The solution must enforce approved role-based access control and,
where required, row-level or hierarchical access restrictions consistently
across dashboards, query interfaces and underlying data stores.

·
The solution must comply with GDPR, approved privacy, lawful
processing, data residency and deletion requirements applicable to stored
prompts, responses, identifiers and observability records.

·
The solution must enforce approved retention, archive and purge
rules by data category and support auditable deletion where required.

·
The solution must use approved infrastructure-as-code and
deployment automation patterns that support repeatable environment
provisioning, approval controls and auditable release management.





# 5.   Functional Requirements

## 5.1.       High Level Requirements[MA5] [PA6]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***#*** | ***Requirement*** | ***Priority*** | ***Audience*** | ***Microsoft comment*** |
| **R1** | **Provide end-to-end traceability of AI agent execution across requests, orchestration steps, tool calls, model invocations, retrieval steps and downstream actions using correlation identifiers.** | **Must Have** | **Developers, SREs** |  |
| **R2** | **Capture and report near-real-time operational metrics for in-scope AI agents, including latency, request volume, error rate, token or consumption metrics and other agreed runtime indicators.** | **Must Have** | **SREs, Platform Team** |  |
| **R3** | **Support continuous evaluation of agreed output quality measures for production AI traffic, such as groundedness, relevance, coherence or other approved quality dimensions where these are appropriate to the use case.** | **Must Have** | **Developers, Product** |  |
| **R4** | **Monitor safety controls, policy checks and content-filtering outcomes for in-scope AI interactions and generate alerts when defined thresholds, failures or policy exceptions occur.** | **Must Have** | **Security, Compliance** |  |
| **R5** | **Provide cost attribution and reporting by agent, model, environment and other agreed cost dimensions, including prompt or configuration variants where such attribution is feasible and approved.** | **Must Have** | **Finance, Product** |  |
| **R6** | **Support controlled prompt and configuration versioning, collaborative review or annotation, and comparative testing capabilities such as A/B testing where these are required for ongoing optimisation.** | **Should Have** | **Developers** |  |
| **R7** | **Maintain an auditable record of data access, configuration changes, query activity and lineage of observability data sufficient to support compliance, assurance and investigation needs.** | **Must Have** | **Compliance, Legal** |  |
| **R8** | **Provide enterprise governance capabilities for registering in-scope AI agents, managing access controls, maintaining fleet-level visibility and supporting oversight of ownership, status and compliance posture.** | **Should Have** | **IT Admin, Security** |  |
| **R9** | **Support integration with approved enterprise monitoring, dashboarding and reporting services, including Azure-native capabilities and other agreed existing platforms where required.** | **Should Have** | **SREs, Platform Team** |  |
| **R10** | **Provide business observability capabilities that capture standardised business events, surface stakeholder dashboards and support governed AI-assisted access to approved reporting data.** | **Must Have** | **Business users, Project Stakeholders** |  |
| **R11** | **Support observability across approved model providers or hosting patterns, including multi-model or multi-platform scenarios where these are part of the agreed enterprise architecture.** | **Nice to Have** | **Architecture** |  |
| **R12** | **Provide human-in-the-loop oversight capabilities for high-impact AI-supported decisions, including reporting of review points, escalation paths, approvals, exceptions and overdue oversight actions where required by policy or risk assessment.** | **Must Have** | **Compliance, Risk, Business Owners** |  |
| **R13** | **Support technical observability for low-code AI platforms and externally hosted AI agents, such as Microsoft Copilot-based solutions and third-party agent platforms such as SAP Joule, using approved native telemetry, APIs, connectors or adaptors where direct instrumentation is not available.** | **Should Have** | **Architecture, Platform Team, Security** |  |



## 5.2.       Requirement Linkage and Coverage

The high-level requirements in section 5.1 describe the business
and stakeholder outcomes the solution must achieve. The detailed requirements
in section 5.2 define the implementable capabilities, controls and acceptance
criteria that collectively satisfy those high-level requirements. A single
high-level requirement may be supported by multiple detailed requirements, and
some detailed requirements contribute to more than one high-level outcome.

|  |  |  |
| --- | --- | --- |
| ***High-Level Requirements*** | ***Supported By Detailed Requirement(s)*** | ***Coverage Summary*** |
| **R1** | **FR-TECH-001, FR-TECH-002, FR-TECH-003** | **Provides layered architecture, mandatory logging and central schema needed for end-to-end traceability.** |
| **R2** | **FR-TECH-002, FR-TECH-004, FR-TECH-005, FR-EXEC-001, FR-EXEC-002** | **Supports near-real-time operational metrics, alerting, dashboards and KPI reporting for runtime monitoring.** |
| **R3** | **FR-TECH-004, FR-EXEC-001, FR-EXEC-002** | **Partially supports continuous quality monitoring through monitoring, dashboards and KPI framework; additional explicit quality-evaluation detail may still be needed if retained as a core requirement.** |
| **R4** | **FR-TECH-004, FR-TECH-005, FR-CMP-002, FR-CMP-004, FR-CMP-006, FR-CMP-009, FR-CMP-010, FR-CMP-013** | **Links runtime monitoring with policy compliance, fairness monitoring, escalation and challenge routes.** |
| **R5** | **FR-BUS-001, FR-EXEC-001, FR-EXEC-002** | **Provides cost attribution and reporting through business event capture, dashboards and KPI definitions.** |
| **R6** | **No direct detailed requirement currently mapped** | **Controlled prompt versioning, collaborative review and comparative testing are part of Azure standard.** |
| **R7** | **FR-TECH-006, FR-SEC-002, NFR.SEC.2, NFR.CMP.2, FR-CMP-011, FR-CMP-012** | **Provides auditability, access control, retention, compliance evidence and audit review visibility.** |
| **R8** | **FR-CMP-001, FR-CMP-002, FR-CMP-003, FR-CMP-011, FR-CMP-012** | **Supports ownership, compliance posture, lifecycle visibility, governance evidence and audit review status.** |
| **R9** | **FR-TECH-001, FR-TECH-004, FR-EXEC-001** | **Provides baseline integration and reporting support, though named platform integration requirements could be strengthened if needed.** |
| **R10** | **FR-BUS-001, FR-BUS-002, FR-EXEC-001, FR-EXEC-002** | **Links business event capture, dashboards, KPI framework and governed AI-assisted query capability.** |
| **R11** | **FR-TECH-001** | **Partially supported through the overall end-to-end architecture requirement; multi-model and multi-platform support is not yet explicit in the detailed requirements.** |
| **R12** | **FR-CMP-001** | **Provides explicit coverage for required human oversight, escalation visibility, review status reporting and overdue oversight alerting for high-impact decisions.** |
| **R13** | **FR-TECH-007** | **Provides explicit detailed coverage for onboarding and monitoring low-code AI platforms and externally hosted AI agents using approved native telemetry, APIs, connectors or adaptors where direct instrumentation is not available.** |

##

## 5.3.       Detailed Requirements



|  |
| --- |
| FR-TECH-001 End-to-End Layered Architecture     The platform shall provide an end-to-end AI observability architecture across Development, Test and Production environments that supports technical telemetry, business event capture, security controls, dashboards and governed query acccess for all in-scope AI agents.     **Pre-requisites**  ·         Azure environment available  ·         AI agents deployed     **Acceptance Criteria**  ·         A documented architecture exists covering telemetry ingestion, business event storage, identity and access control, dashboarding, alerting and governed query access.  ·         Development, Test and Production environments are provisioned with separated configuration, deployment pipelines and access controls.  ·         At least one representative in-scope AI agent is onboarded end to end and produces telemetry, business events, dashboard data and auditable access records in each non-production and production-ready environment as applicable. |
| FR-TECH-002 Mandatory Agent Logging       All in-scope AI agents shall emit structured observability records for each request and each business event to the central observability platform using the approved schema and mandatory fields defined in this document.  **Pre-requisites**  ·         Logging framework deployed  **Acceptance Criteria**  ·         For each production request, the platform records a unique request identifier, agent identifier, environment, timestamp, execution status, duration, model or tool usage summary and correlation identifiers required to trace execution.  ·         For each business action completed or attempted by an AI agent, the platform records a business event containing the mandatory business fields defined in the Business Event Schema section.  ·         Onboarding checks demonstrate that required fields are present for at least 95% of sampled events before an agent is approved for production reporting. |
| FR-TECH-003 Centralised Event Schema     The platform shall provide a central event schema comprising mandatory core fields for all agents and controlled extension fields for department-specific business contexts.    **Pre-requisites**  ·         Schema definition agreed  **Acceptance Criteria**  ·         The schema includes mandatory fields for event identity, agent identity, environment, business context, outcome, timestamps, status, correlation and security classification.  ·         Department-specific extension fields may be added only through an approved extension mechanism that preserves the mandatory core fields and does not change existing field meanings.  ·         Existing approved queries and dashboards continue to function when a new department-specific extension is introduced. |
| FR-TECH-004 Monitoring & Alerting     The platform shall monitor technical and business observability signals for in-scope AI agents and raise alerts when configured thresholds or abnormal conditions are breached.    **Pre-requisites**  ·         Monitoring configured  ·         ServiceNow integration available  **Acceptance Criteria**  ·         The platform supports alert rules for at least latency, error rate, failed executions, missing event ingestion and business outcome thresholds.  ·         Each alert rule has a defined severity, owner, notification channel and remediation path.  ·         Where ServiceNow integration is enabled, qualifying alerts create or update incidents or support records according to the agreed routing rules. |
| FR-TECH-005 Alert Severity & Response SLA     The platform shall define alert severity levels and response service levels for agreed categories of technical, business, security and data quality alerts.     **Pre-requisites**  ·         Alert categories and owners agreed  ·         Operational support model defined  **Acceptance Criteria**  ·         Each alert type is mapped to a severity level such as Critical, High, Medium or Low, with defined examples and escalation paths.  ·         For each severity level, the service defines target times for acknowledgement, investigation start, update frequency and resolution or workaround communication.  ·         Support ownership, notification channels and out-of-hours handling are documented for each severity level.  ·         Where service management integration is enabled, incidents raised from alerts carry the assigned severity and route to the correct support group. |
| FR-TECH-006 Data Storage & Retention    The platform shall store observability and business event data in accordance with an approved retention policy that defines retention periods, archive rules and deletion or purge rules by data category.    **Pre-requisites**  ·         Storage platform provisioned  **Acceptance Criteria**  ·         A documented retention policy exists for at least raw telemetry, business events, audit logs, prompt or response content if stored, derived aggregates and archived data.  ·         The platform enforces the approved retention and archival rules automatically or through scheduled operational processes.  ·         Deletion or purge processes are auditable and support legal, regulatory or governance exceptions where approved. |
| FR-SEC-002 Row-Level Security    The system shall implement database-level row-level security.    **Pre-requisites**   * Data model defined   **Acceptance Criteria**   * Users cannot query   unauthorised rows * Security applies to all   access methods |
| **FR-BUS-001 Business Event Tracking**    The platform shall capture standardised business events for AI agent activities so that business intent, business outcome and operational status can be measured consistently across departments.    **Acceptance Criteria**  ·         Each business event includes a defined business intent, business outcome, execution status and business context identifiers as specified in the Business Event Schema section.  ·         The data model supports reporting by department, agent, process, environment, outcome type and time period.  ·         Sample reports can distinguish successful completion, failed completion, partial completion, human handoff and no-action outcomes where these states are relevant to the onboarded process. |
| FR-BUS-002 AI Query Agent    The system shall provide an AI agent that converts natural language queries into SQL.    **Pre-requisites**   * Data schema available   **Acceptance Criteria**   * Users can query data in   plain English * System generates SQL   dynamically * Results respect RBAC + RLS * Output is structured   (tables only) |
| FR-EXEC-001 Dashboarding    The platform shall provide role-based dashboards that present approved technical, operational and business KPIs for the stakeholder groups defined for this service.    **Pre-requisites**  ·         Data model implemented  **Acceptance Criteria**  ·         At least one dashboard is provided for each agreed stakeholder group such as executive, product or business owner, engineering or operations, and security or compliance.  ·         Dashboards support filtering by time period, environment, agent, department or process where applicable.  ·         Access to dashboards and underlying data is restricted according to approved role-based access controls. |
| FR-EXEC-002 KPI Framework     The service shall define and publish a baseline KPI framework for AI observability covering usage, reliability, business outcomes, cost and governance measures.    **Acceptance Criteria**  ·         Each KPI has a unique name, business description, formula, source fields, owner, reporting cadence and intended audience.  ·         Each KPI is calculable from approved stored data without reliance on manual spreadsheet manipulation.  ·         The baseline KPI set includes measures for volume, success, failure, handoff, latency or turnaround, cost and access or governance activity, as applicable to the onboarded processes. |
| FR-CMP-001 Human Oversight and Escalation    The platform shall support reporting and alerting for human review and escalation controls for AI-supported decisions that may significantly affect safety, employment, legal rights or other high-impact outcomes, where such controls are required by policy or risk assessment.    **Acceptance criteria**  ·         Ability to record when human review is required, invoked, bypassed or completed  ·         Report escalation paths, approvers and exception outcomes  ·         Generate alerts when required human oversight steps are missing or overdue |

|  |
| --- |
| FR-TECH-007 Low-Code and External Agent Observability    The platform shall support onboarding and monitoring of approved low-code AI platforms and externally hosted AI agents, including cases where direct instrumentation is not available, by using approved native telemetry, APIs, connectors or adaptors to capture minimum required observability data.    **Pre-requisites**  ·         Approved onboarding pattern defined for low-code and external agent platforms  ·         Provider telemetry source, API, connector or adaptor identified and approved  **Acceptance Criteria**  ·         For each onboarded low-code or externally hosted AI agent, the platform captures and stores a minimum agreed observability record including agent identifier, platform or provider, environment where relevant, event timestamp, execution status or outcome, and any available request, usage, failure or policy signal exposed by the approved telemetry source.  ·         Where full trace-level instrumentation is not available, the onboarding record documents the telemetry limitations, data provenance and approved minimum monitoring coverage for that platform or agent.  ·         At least one representative low-code or externally hosted AI agent can be onboarded using an approved connector, API or adaptor and its telemetry is visible in central monitoring and reporting views. |



**Business Event Schema**
**The
following draft schema is proposed as the minimum mandatory business event
contract for all in-scope AI agents. Each business event should include
mandatory core fields and may include approved extension fields for
department-specific use cases.**

|  |  |  |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| **event\_id** | **String** | **Unique identifier for the business event record.** |
| **request\_id** | **String** | **Identifier linking the business event to the underlying agent request or execution trace.** |
| **agent\_id** | **String** | **Unique identifier of the AI agent or service that produced the event.** |
| **agent\_name** | **String** | **Readable name of the AI agent.** |
| **environment** | **String** | **Environment in which the event occurred such as Development, Test or Production.** |
| **business\_domain** | **String** | **Business domain or department such as EFF, HR or another approved domain.** |
| **business\_process** | **String** | **Named business process or workflow step that the event relates to.** |
| **business\_object\_id** | **String** | **Identifier of the business object being acted on, for example case ID, ticket ID, order ID or request ID.** |
| **event\_type** | **String** | **Business event category such as created, attempted, completed, failed, escalated or handed off.** |
| **intent** | **String** | **The intended business purpose of the action, expressed using an approved taxonomy.** |
| **outcome** | **String** | **Business outcome such as success, failed, partial success, no action or human handoff.** |
| **status** | **String** | **Operational execution status such as started, completed, failed, cancelled or timed out.** |
| **event\_timestamp\_utc** | **Datetime** | **UTC timestamp of when the event occurred.** |
| **duration\_ms** | **Number** | **Execution time or elapsed duration for the relevant action.** |
| **cost\_amount** | **Number** | **Direct attributed cost of the execution or estimated cost where direct cost is not available.** |
| **model\_or\_provider** | **String** | **Model, provider or major runtime component used for the action where relevant.** |
| **handoff\_flag** | **Boolean** | **Indicates whether the process was handed to a human or downstream non-AI process.** |
| **sensitivity\_classification** | **String** | **Classification of the event data for governance and access control purposes.** |







**KPI Framework**
The following draft KPI framework is proposed as the minimum baseline
set. KPI formulas and thresholds should be approved with business, product and
operational owners during solution design and onboarding.

|  |  |  |  |
| --- | --- | --- | --- |
| **KPI** | **Definition / Formula** | **Audience** | **Notes** |
| Agent request volume | Count of agent requests in period. | Executive, Product, Engineering | Useful for adoption and capacity trends. |
| Business completion rate | Completed business outcomes divided by total attempted business outcomes. | Executive, Product, Business Owner | Should use standard outcome taxonomy. |
| Failure rate | Failed executions or failed business outcomes divided by total executions or attempts, depending on agreed metric scope. | Engineering, Product, Executive | Can be split into technical and business failure measures. |
| Human handoff rate | Count of events with handoff\_flag true divided by total attempted business outcomes. | Business Owner, Product, Operations | Indicates containment and automation limits. |
| Average turnaround time | Average duration between start and completion of the relevant process or event type. | Executive, Business Owner, Engineering | Can be process specific. |
| Average cost per successful outcome | Total attributed cost divided by number of successful business outcomes in period. | Finance, Product, Executive | Supports value and efficiency tracking. |
| Security or access exceptions | Count of blocked unauthorised access attempts, policy violations or relevant security exceptions in period. | Security, Compliance | Supports governance reporting. |















**Personas and Dashboard
Requirements**

The following draft personas and dashboard requirements are
proposed to clarify who the platform serves, what questions each stakeholder
group needs answered, and what dashboard capabilities should be provided. This
section is intended to strengthen the role-based dashboard design and review.

|  |  |  |
| --- | --- | --- |
| **Persona** | **Primary Need** | **Typical Questions** |
| Executive / Leadership | Understand business value, adoption, risk and cost. | Which agents deliver measurable value? Which business areas are benefiting? What are the risk and cost trends? |
| Business Owner / Product Owner | Track process outcomes, adoption, failure points and handoffs. | What is the completion rate? Where do human handoffs occur? Which journeys are failing most often? |
| Engineering / SRE / Platform | Detect incidents, performance issues and reliability regressions. | What is failing right now? Which agents exceed latency thresholds? Are events ingesting correctly? |
| Security / Compliance | Monitor access, policy compliance and auditability. | Who accessed what? Were any unauthorised attempts blocked? Are required audit records present? |
| Finance / Commercial | Track cost efficiency and cost drivers. | What is cost per successful outcome? Which agents or models are the main cost drivers? |

**Dashboard Requirements**

·
The platform shall provide at least one dashboard view for each
agreed stakeholder persona.

·
Each dashboard shall display only the data and KPIs approved for
that role.

·
Dashboards shall support filtering by time period, environment,
department, agent and business process where those attributes are available.

·
Executive dashboards shall focus on business outcomes, adoption,
risk posture and cost trends rather than raw technical telemetry.

·
Business owner dashboards shall show completion rate, failure
rate, human handoff rate, turnaround time and process-specific business KPIs.

·
Engineering and operational dashboards shall show health,
latency, failures, ingestion status, alert state and diagnostic drill-down
paths.

·
Security and compliance dashboards shall show access events,
policy exceptions, audit completeness and relevant control status.

·
Each dashboard shall identify its owner, intended audience, data
sources and refresh cadence.

# 6.   Non-Functional Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Ref** | **Description** | **Category** | **MoSCoW rating** |
| **NFR.SEC.1** | All observability, business event, audit and query data shall be encrypted in transit using approved transport security controls and encrypted at rest using approved key management controls.  Test evidence shall demonstrate that encryption is enabled for all production data stores and network paths carrying in-scope data. | **Security** | **Must** |
| **NFR.SEC.2** | The platform shall audit log all administrative access, dashboard access, governed query requests, security policy changes and data access attempts relevant to in-scope observability data.  Audit records shall include timestamp, user or service identity, action performed, target resource, outcome and correlation identifier where available. | **Security** | **Must** |
| **NFR.PER.1** | The platform shall publish and meet approved performance targets for telemetry ingestion, dashboard refresh and governed query response for the agreed production workload.  Performance targets shall include at minimum: business and technical events available for reporting within an agreed ingestion window, dashboard data refreshed on the agreed cadence, and authorised query responses returned within an agreed service target for standard result sizes. | **Performance** | **Must** |
| **NFR.SCL.1** | The platform shall scale to support growth in onboarded AI agents, event volume, retained history and concurrent dashboard and query usage without requiring redesign of the core data model.  Capacity planning assumptions, growth thresholds and scale test evidence shall be documented for the agreed target operating model. | **Scalability** | **Must** |
| NFR.AVL.1 | The platform shall have a defined availability target for production services covering data ingestion, dashboard access and governed query capability, excluding approved maintenance windows. | Availability | Must |
| NFR.RES.1 | The platform shall provide resilience controls to prevent single points of failure for critical production components and to recover gracefully from transient downstream failures. | Resilience | Must |
| NFR.DR.1 | The service shall define disaster recovery objectives including recovery time objective and recovery point objective for critical data and service components, and shall maintain a tested recovery procedure. | Disaster Recovery | Must |
| NFR.SUP.1 | The service shall define an operating and support model covering support ownership, support hours, incident severity definitions, escalation paths and change approval responsibilities. | Support | Must |
| NFR.DQ.1 | The platform shall define and monitor data quality controls for required event fields, duplicate handling, schema conformance and timeliness of data availability for reporting. | Data Quality | Must |
| **NFR.CMP.1** | The platform shall process, store, retain and delete personal or sensitive data in accordance with approved privacy, lawful processing, retention and data residency requirements applicable to the service.  Where prompt content, responses or identifiers may contain personal data, approved masking, minimisation, access control and deletion controls shall be applied. | **Compliance** | **Must** |
| **NFR.CMP.2** | The platform shall ensure that required responsible AI compliance evidence for each in-scope AI system, including owner, lifecycle status, risk assessment status, DPIA status, bias assessment status, governance review status and approval status where applicable, is stored or referenced in a manner that is reportable, auditable and attributable. | **Compliance** | **Must** |







# 7.   Requirement Traceabilty Matrix

The RTM can be accessed via the following link:



---

# 8.   Document Review and Sign Off

As part of the review and sign off process, it is important to
refer to the following criteria to ensure that the document is fit for purpose.
There are two types of review criteria:

·
Generic
criteria – which can apply to any document.

·
Specific criteria – that assess specific areas within a
particular document type.

The Generic criteria that must be used when considering
deliverables are:

|  |  |
| --- | --- |
| 1. | Has each section of the document been addressed to the expected level? |
| 2. | Could this deliverable, in its current state, be used as an input into a subsequent document? |

**Specific Criteria**

For this deliverable, the following specific criteria should be
applied to the review:

|  |  |
| --- | --- |
| 1. | Does the document clearly identify the background to the change? |
| 2. | Does the document clearly identify what areas are in and out of scope for the change? |
| 3. | Does the document clearly identify and adequately describe the specific business processes/scenarios which may be impacted by a solution to the business problem/opportunity? |
| 4. | Are key Assumptions, Issue & Dependencies identified? |



As part of the review and sign off process, it is important to
refer to the following criteria to ensure that the document is fit for purpose.

|  |
| --- |
| Has each section of the document been addressed to the expected level? |
| Could this deliverable, in its current state, be used as an input into a subsequent document? |

Approval emails must be added and attached to the appropriate
sections below.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | ***Approver (Accountable)*** | | |  | | Name | Role | Approval (email/e-signature) | Date | |  |  |  |  |       |  |  |  |  | | --- | --- | --- | --- | | ***Authors (Responsible)*** | | |  | | Name | Role | Date | | |  |  |  | | |  |  |  |  |       |  |  |  |  |  | | --- | --- | --- | --- | --- | | ***Reviewers*** ***(Consulted)*** | |  | | | | Name | Role | | Contribution |  | |  |  | |  |  | |  |  | |  |  | |  |  | |  |  | |  |  |  |  |  |      |  |  |  | | --- | --- | --- | | ***Distributed (Informed)*** | | | | Name | Role | Comment | |  |  |  | |

---

*<end document>*

---

[MA1]Are
we covering Human in the Loop / actionable dashboards here?

[PA2]No
- I will keep it separate for now as a control panel requirement however we may
want to know how many & how often decisions are being made by Humans &
why which is an observability requirement & I have added it.

[MA3]Should
we be looking (maybe long term) at bringing external AI logs into this main
control tower (E.g. SuccessFactors's Joule)

[PA4]From
a PRIO’s scope perspective, in my opinion that is out of scope. Happy to
discuss & keep it open for future

[MA5]https://mitiegrp.sharepoint.com/sites/MitieQHSE/Integrated%20Management%20System/Forms/AllItems.aspx?id=%2Fsites%2FMitieQHSE%2FIntegrated%20Management%20System%2FResponsible%20and%20Ethical%20AI%20Policy%5FMG%28POL%29871%2Epdf&parent=%2Fsites%2FMitieQHSE%2FIntegrated%20Management%20System

we have the AI policy, we need to make sure these
requirements deliver against what that policy demands.

For example, the policy states "Mitie will
actively avoid unfair or biased outcomes in AI systems. Bias detection methods
will

be applied during development, and both data and
decision processes will be tested regularly

for potential bias. Where bias is identified,
corrective action must be taken promptly." - so we need to build this into
up front and regular reporting capability? "AI systems must not
discriminate on the basis of protected characteristics such as age,

ethnicity, disability, or gender. Where monitoring
identifies unintended or unfair outcomes,

corrective action must be taken promptly to address the
issue and prevent recurrence"

" AI models will be developed with a focus on
transparency and interpretability. Documentation

of model development, including algorithms used,
training data, and evaluation metrics, will be

maintained and controlled. Before deployment, all AI
models will undergo rigorous bias

detection and mitigation testing. Techniques will be
applied to ensure fair and equitable

outcomes, and continuous monitoring will be conducted
after deployment"

"AI decisions must be explainable to relevant
stakeholders. We commit to using explainable AI

techniques to ensure that decisions can be understood
and justified. We will update our

whistleblowing and other reporting mechanisms to
include reports of ethical concerns related

to AI. "

"To maintain confidence in our systems, we will
implement ongoing monitoring of AI

performance, including regular assessments of
effectiveness, fairness, and security. In addition,

both internal and external audit teams will conduct
periodic reviews of AI processes and

systems to test compliance with ethical standards and
regulatory requirements.

"

" All decisions of significance must include
human review, particularly where outcomes could

affect safety, employment or legal rights. Automated
decisions that impact individual rights

must always provide a clear route for human
reconsideration"

". Mitie will maintain clear internal escalation
paths so that employees and customers can

challenge AI outputs to ensure that concerns are
addressed and that human accountability

remains central to AI use"

"Correlations between model outputs and protected
characteristics will be routinely assessed

and features causing significant correlation with
protected characteristics must be reviewed

and modified or removed"

etc. I think we need to make sure we have done a full
review against this!

[PA6]Thanks
@Michael Agar. I have added AI Ethics in scope
& also a detailed requirement for human in the loop, however I am not sure
all the AI ethics policies need to be observed via this requirement.

I have added couple of related NFR’s.

Many of these policies are set at inception of the project & part of
development. They need to be governed & policed but I am not sure how they
would fit into this framework that we are trying to build. Probably need more
thoughts post an MVP for these requirements.