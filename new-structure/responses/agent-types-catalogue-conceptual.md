# Agent types catalogue — conceptual view

| Field | Value |
| --- | --- |
| Purpose | Vendor-neutral classification of the agent types an enterprise estate accumulates. Used as input for observability scope, governance perimeter, identity strategy and licensing conversations. |
| Status | Draft v2.2 — 2026-06-23. Concept-first rewrite of `agent-types-catalogue.md`. Specific products appear only as illustrative examples. Section 6b expanded with sub-agent governance breakdown. |
| Author | Microsoft architecture |

The catalogue is built around two questions:

1. **Who builds the agent?** (vendor, low-code author, pro-code author)
2. **Where does it run?** (vendor SaaS, managed runtime, customer compute, device/edge)

Everything else — identity model, telemetry plane, cost model, governance perimeter — follows from those two answers.

The document is in two parts:

- **Part A — Agent archetypes** (sections 1–6). Six conceptual archetypes that, together, cover the estate.
- **Part B — Cross-cutting axes** (section 7). Orthogonal dimensions used in policy and governance conversations regardless of archetype.

Section 8 lists open additions.

Each archetype is described by the same five attributes:

- **What it is** — one-line definition.
- **Build effort** — what the customer actually authors.
- **Hosting** — whose compute executes the agent.
- **Identity** — how the agent authenticates and acts.
- **Telemetry convention** — the standard observability pattern that fits the archetype, expressed in generic terms (built-in analytics, audit logs, instrumentation, network telemetry).
- **Illustrative examples** — concrete products today, included only to anchor the concept.

---

# Part A — Agent archetypes

## 1. Vendor-shipped assistants

| Attribute | Description |
| --- | --- |
| What it is | Agent is part of a product the customer licenses. The customer adopts and configures, but does not author the agent. |
| Build effort | Tenant configuration, role assignment, data-source connection, prompt scoping. No code, no agent definition. |
| Hosting | Vendor cloud. |
| Identity | Delegated (acts on behalf of the signed-in user). Some vendor-internal automation may use workload identity invisible to the customer. |
| Telemetry convention | Product admin centre / built-in usage dashboard + tenant-wide audit log + SaaS-posture / shadow-AI discovery tool. The customer sees activity but not internal traces. |
| Illustrative examples | Productivity-suite assistants (M365 Copilot family, Workspace Gemini), OS / browser assistants (Copilot in Windows / Edge, Chrome Gemini), role-based assistants (Copilot for Sales / Service / Security, GitHub Copilot), LoB-embedded assistants (Joule for SAP, Agentforce for Salesforce, Now Assist for ServiceNow, Workday Illuminate, Oracle AI Agents). |

## 2. Low-code agents on a vendor authoring platform

| Attribute | Description |
| --- | --- |
| What it is | Customer authors the agent inside a vendor-provided studio — topics, flows, knowledge connectors, tool actions — without writing host code. The vendor runs it. |
| Build effort | Conversation design, knowledge wiring, tool/action configuration, channel publishing. |
| Hosting | Vendor-managed runtime. |
| Identity | Delegated by default; first-class agent identity where the platform offers one. |
| Telemetry convention | Studio analytics + platform audit log + linked APM trace when the platform supports an export. |
| Illustrative examples | Copilot Studio (declarative and custom-engine agents), Microsoft 365 Agents Toolkit declarative agents, Power Virtual Agents (legacy), Salesforce Prompt Builder, ServiceNow Now Assist Studio, low-code paths of Bedrock Agents and Vertex AI Agent Builder. |

## 3. Pro-code agents on a managed agent runtime

| Attribute | Description |
| --- | --- |
| What it is | Customer writes agent code (Python, .NET, TypeScript…) against a managed agent service that owns model wiring, tool calling, threading, evaluation and scaling. |
| Build effort | Code (agent definition, tools, prompts) + datasets + evaluators. The cloud handles the rest. |
| Hosting | Cloud-provider managed runtime. |
| Identity | Workload identity for the agent itself + delegated tokens for user-context tool calls. |
| Telemetry convention | First-class runtime tracing (OpenTelemetry spans for prompt / model / tool) + built-in continuous evaluation + AI-gateway metrics when model traffic is proxied. |
| Illustrative examples | Microsoft Foundry Agent Service (prompt agents, hosted agents, multi-agent workflows, MCP-tool agents), Bedrock Agents (SDK path), Vertex AI Agent Builder (SDK path), OpenAI Assistants API. |

## 4. Pro-code agents on customer infrastructure

| Attribute | Description |
| --- | --- |
| What it is | Customer writes agent code with an open or first-party framework and runs it on their own compute. Maximum flexibility, maximum responsibility. |
| Build effort | Full ownership: agent code, host wiring, prompt management, evaluation harness, observability, deployment pipeline. |
| Hosting | Customer compute — managed PaaS, container platform, Kubernetes, serverless, on-prem, IoT/edge. |
| Identity | Workload identity by default; delegated via on-behalf-of / token exchange when acting for a user. |
| Telemetry convention | OpenTelemetry from the agent framework → APM / log store; AI gateway in front of model endpoints for token metrics, rate-limit and content-safety policies; container or host runtime metrics for the platform plane. |
| Illustrative examples | Semantic Kernel, Microsoft Agent Framework, AutoGen, LangChain / LangGraph, LlamaIndex, CrewAI, hand-rolled in-house frameworks; self-hosted LLM stacks (e.g. KAITO + vLLM on Kubernetes); edge / IoT agents on Azure IoT Edge or Arc. |

## 5. Agents embedded in SaaS the customer already licenses

| Attribute | Description |
| --- | --- |
| What it is | AI features that appear inside SaaS products the customer already uses, often turned on by default or by team-level toggles. Frequently discovered after the fact. |
| Build effort | None to minimal (admin toggle, role-based access). |
| Hosting | Vendor cloud. |
| Identity | Vendor-managed user identity; rarely exposes a workload identity to the customer. |
| Telemetry convention | Vendor audit / events API as system of record + SIEM connector for central correlation + CASB / SaaS-posture tool for discovery, activity policies and shadow-AI surfacing. |
| Illustrative examples | Knowledge / collaboration assistants (Slack AI, Notion AI, Rovo for Atlassian, Box AI, Glean), CRM / marketing assistants (Breeze for HubSpot, Zendesk AI), data-platform assistants (Snowflake Cortex agents, Databricks/Mosaic agents), meeting assistants (Zoom AI Companion). |

## 6. Endpoint and device-local agents

| Attribute | Description |
| --- | --- |
| What it is | Agents executing on the user's device, in the browser, or at the network edge — often outside the central agent inventory. |
| Build effort | None to fleet-policy configuration. The user is often the de facto adopter. |
| Hosting | Device (CPU / GPU / NPU), browser, on-prem appliance, contact-centre platform. |
| Identity | Device identity + signed-in user identity; sometimes only a personal account, which is the shadow-AI risk. |
| Telemetry convention | Device-management + EDR + browser admin reports for managed surfaces; CASB / egress / SWG logs for unmanaged surfaces; vendor connectors for contact-centre and OT platforms. |
| Illustrative examples | On-device AI on AI-PCs (Copilot+ PC features such as Recall and Click-to-Do), mobile Copilot apps, in-browser AI (Edge Copilot, Chrome Gemini, Arc / Brave AI), IDE agents (GitHub Copilot, Cursor, Cline), Office / Outlook add-ins with AI, voice / IVR agents on contact-centre platforms, robotic / OT agents. |

## 6b. Ephemeral sub-agents (runtime composition)

Not a seventh archetype but a runtime pattern that cuts across archetypes 2, 3 and 4 (and increasingly 1). A parent agent spawns short-lived child agents to plan, retrieve, critique, summarise or execute a sub-task, then disposes of them when the parent turn completes.

| Attribute | Description |
| --- | --- |
| What it is | A child agent instantiated and discarded inside a single invocation of a parent agent. The customer does not register or license it separately. |
| Build effort | Authored together with the parent — same code base, same prompts repository, same evaluation suite. No separate onboarding artefact. |
| Hosting | Wherever the parent runs (managed runtime or customer compute). |
| Identity | Usually inherits the parent's workload or delegated identity. A dedicated agent identity for the sub-agent is rare today and only matters when the sub-agent crosses a trust boundary (e.g. acts against a different downstream system under its own credentials). |
| Telemetry convention | Child spans under the parent's distributed trace, with per-sub-agent attributes (role, model, tool count, tokens). Cost attribution rolls up to the parent. AI gateway sees one logical model call per leaf, so token metrics still land at the gateway level. |
| Governance perimeter | The parent. The sub-agent inherits the parent's allowed-tool list, content-safety policies and approval gates. Independent governance is not the goal. |
| When it matters separately | Debugging multi-agent failures ("which sub-agent went off track?"); cost attribution between sub-agents on the same parent; per-sub-agent evaluation in continuous-evaluation pipelines; security review when one sub-agent has a wider tool scope than its siblings. |
| Illustrative examples | Planner / executor / critic patterns; retrieval and tool-selection sub-agents; map-reduce style fan-out where each chunk is handled by a child; "specialist" sub-agents inside Foundry multi-agent workflows, Semantic Kernel / Agent Framework / AutoGen / LangGraph / CrewAI orchestrations. |

The practical implication: when scoping observability and governance for the estate, **sub-agents are not separate inventory items but they are first-class telemetry items**. The trace tree, not the agent registry, is the right unit of analysis for them.

### Governance concerns: sub-agent vs top-level agent

Most security and policy controls are correctly enforced at the parent and propagate to its children for free. A handful of concerns do not inherit cleanly and need explicit sub-agent attention.

| Concern | Inherited from parent (no separate work) | Needs sub-agent-level attention |
| --- | --- | --- |
| Identity and authentication | Yes — sub-agent runs under the parent's identity. | Only when a sub-agent crosses a trust boundary (calls an external API or tool under its own credentials). |
| Tool allow-list | Yes — in principle, a sub-agent can only invoke tools the parent grants. | Verify that the chosen framework actually scopes tools per sub-agent rather than letting every child inherit the parent's full set. Confused-deputy risk otherwise. |
| Network egress, data residency | Yes — runs in the parent's host. | Only if the sub-agent reaches an endpoint the parent does not. |
| DLP, content safety, jailbreak detection | Yes — enforced at the AI-gateway / model entry. | None at the wire level. |
| Human-in-the-loop, approval gates | Yes — placed on user-visible actions owned by the parent. | None. |
| Cost attribution at tenant level | Yes — rolls up to the parent. | **Yes** — per-sub-agent token quotas to prevent recursive or looping cost runaway. |
| System prompt / instruction quality | No — each sub-agent has its own. | **Yes** — independent prompt review and version control per sub-agent. |
| Evaluation and quality | No. | **Yes** — continuous evaluation must score sub-agents individually; overall quality is the product of all of them. |
| Prompt injection between sub-agents | Partial — inbound to the parent is filtered. | **Yes** — output of one sub-agent becomes input of another; treat every inter-agent message as untrusted. |
| Least-privilege context | No. | **Yes** — pass each sub-agent only the data it needs, not the parent's full state. |
| Telemetry granularity | Inherits the parent's pipeline. | **Yes** — per-sub-agent spans are a prerequisite for debugging and cost attribution; without them governance is blind. |
| Change management | Partial — parent versioning. | **Yes** — sub-agent edits often hide inside parent diffs; CI/CD and review processes must surface them explicitly. |

The boundary case: when a sub-agent is reused across parents — exposed as an MCP tool, an A2A endpoint, or a shared library callable by other agents — it stops being a sub-agent and becomes a top-level agent in its own right. The full governance burden of archetypes 3 or 4 then applies (identity, registration, evaluation, lifecycle, licensing).

---

# Part B — Cross-cutting axes

## 7. Orthogonal categorisations

A single agent is described by one archetype above plus a position on each of the following axes. These are the levers in governance, identity, cost and observability conversations.

| Axis | Values | Why it matters |
| --- | --- | --- |
| Authorship | Vendor / Low-code by customer / Pro-code by customer / Embedded (no author) / End-user-installed. | Drives change-management and lifecycle ownership. |
| Composition role | Top-level (invoked directly by a user or upstream system) / Sub-agent (invoked by another agent) / Tool-shaped agent (exposed as a tool to other agents, e.g. via MCP). | Drives identity scope, telemetry granularity, cost attribution and where governance is enforced. |
| Hosting plane | Vendor SaaS / Managed agent runtime / Customer cloud compute / On-prem / On-device. | Drives data-residency, network controls and telemetry plane. |
| Identity model | Delegated (acts on behalf of user) / Workload identity (acts as itself) / Hybrid / Personal-account-only. | Determines token flow, audit attribution, agent-identity strategy. |
| Autonomy level | Suggest only / Act with explicit approval (human-in-the-loop) / Act autonomously within guardrails / Multi-agent autonomous. | Drives Responsible-AI obligations and review gates. |
| Data sensitivity | Public knowledge / Internal / Confidential / Regulated (personal, financial, health, industry-specific). | Drives data-loss-prevention, content-safety and grounding policy. |
| Decision impact | Low (drafts, search) / Medium (triage, routing) / High (employment, financial, safety, legal). | Drives HITL and escalation. |
| Tool reach | None / Read-only retrieval / Read–write to systems of record / Acts on external parties (customers, suppliers, regulators). | Drives blast-radius and approval flows. |
| Licensing / cost model | Per-user subscription / Per-message / Per-token / Per-capacity / Embedded in SaaS / Free or shadow. | Drives cost attribution and FinOps. |
| Visibility to central IT | Sanctioned and inventoried / Sanctioned but uninstrumented / Shadow / Unknown. | Drives discovery and onboarding work. |
| Observability surface | Built-in analytics / Vendor audit + SIEM connector / OpenTelemetry instrumentation / Network and identity telemetry only. | Determines which observability investments apply. |

## 8. Open additions

Items worth confirming or adding as the catalogue matures:

- First-class agent-identity adoption per archetype (which archetypes have stable workload-identity stories today).
- Fine-tuned / customer-specific variants of vendor assistants once they reach scale.
- Industry-specific assistants (healthcare, public sector, financial services) as differentiated SKUs.
- Voice-only and multimodal real-time agents.
- Agentic browser products (computer-use agents that drive the UI rather than call APIs).
- Anything in the customer's estate that does not fit cleanly above — fold it into one of the six archetypes with a one-line rationale.
