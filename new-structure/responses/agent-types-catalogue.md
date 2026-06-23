# Agent types catalogue (first list)

| Field | Value |
| --- | --- |
| Purpose | First-pass catalogue of the agent types an enterprise typically ends up with across Microsoft and third-party platforms. Useful as input for observability scope, governance perimeter, registration / fleet management, and vendor strategy conversations. |
| Status | Draft v1.1 — 2026-06-23. Added Telemetry column per agent type. Expect additions as the market evolves. |
| Author | Microsoft architecture |

The list groups agents by **who builds them** and **where they run**, because those two axes drive everything else (identity, telemetry, cost, governance).

## 1. Microsoft pre-built Copilots

Agents Microsoft ships as a product. The customer adopts and configures them but does not author the agent itself.

| Agent | Surface | Notes | Telemetry source |
| --- | --- | --- | --- |
| Microsoft 365 Copilot | Teams, Word, Excel, PowerPoint, Outlook, OneNote, Loop, web | Tenant-wide; central enterprise Copilot. | M365 admin centre Copilot dashboard + usage reports; Purview Audit (unified) for interaction logs; Graph activity logs; DCA app governance. |
| Microsoft 365 Copilot Chat | Web, Teams | Free / pay-as-you-go tier of M365 Copilot. | Same as M365 Copilot (Purview Audit, M365 usage). |
| Copilot in Windows | Windows 11 | OS-level assistant. | Intune / Defender for Endpoint diagnostics; Windows telemetry; limited tenant-level interaction logging. |
| Copilot in Edge | Edge browser | Browser-level assistant. | Edge for Business admin reports; Purview Audit (when signed in with work account); DCA shadow-AI discovery. |
| Copilot in Power BI | Power BI service | Embedded analytics Copilot. | Power BI activity log / audit; Fabric capacity metrics; Purview Audit. |
| Copilot in Fabric | Microsoft Fabric workloads | Data engineering, data science, real-time intelligence. | Fabric monitoring hub; capacity metrics app; Purview Audit. |
| Copilot in Azure | Azure portal | Cloud operator assistant. | Azure activity log; Entra sign-in / audit logs. |
| Copilot for Sales | Dynamics 365 Sales, Outlook, Teams | Role-based. | D365 audit; M365 Copilot usage reports; Purview Audit. |
| Copilot for Service | Dynamics 365 Customer Service, Teams | Role-based. | D365 audit + Omnichannel analytics; Purview Audit. |
| Copilot for Finance | Excel, Outlook, Dynamics 365 | Role-based. | M365 + D365 audit; Purview Audit. |
| Copilot for Security | Microsoft Security stack | SOC analyst assistant. | Built-in Copilot for Security usage / audit dashboard; Sentinel ingestion. |
| Copilot in Dynamics 365 | Dynamics 365 (CRM, Field Service, Customer Insights, Supply Chain, F&O) | Embedded per workload. | D365 audit logs; Dataverse activity logs; Purview Audit. |
| Copilot in Power Apps / Power Automate | Power Platform | Maker assistant. | Power Platform admin analytics; CoE Starter Kit; Purview Audit. |
| GitHub Copilot | IDE, GitHub.com, CLI | Developer assistant. | GitHub Copilot usage / metrics API; GHAS / audit log; org-level dashboards. |
| GitHub Copilot Workspace / Coding Agent | GitHub.com | Issue-to-PR autonomous coding agent. | GitHub audit log; Copilot metrics API; PR / Action run logs. |
| Intune Copilot, Defender Copilot, Purview Copilot | Respective admin centres | Operator assistants in security / management. | Admin-centre audit; Purview Audit for cross-Copilot interaction log. |

## 2. Customer-built agents on Microsoft platforms

Agents the customer authors using Microsoft authoring surfaces. Microsoft hosts the runtime.

| Agent | Authoring surface | Runtime / surface | Notes | Telemetry source |
| --- | --- | --- | --- | --- |
| Copilot Studio — declarative agent | Copilot Studio (no-code) | M365 Copilot, Teams, web channels | Topics + actions + knowledge; lightweight. | Copilot Studio Analytics; Application Insights linkage; Purview Audit. |
| Copilot Studio — custom engine agent | Copilot Studio | M365 Copilot, Teams, web channels | Bring-your-own orchestration / model. | Copilot Studio Analytics + App Insights for the custom engine + APIM AI Gateway token metrics on the model call. |
| Copilot Studio — Microsoft 365 Copilot agent | Copilot Studio | M365 Copilot chat | Published into the M365 Copilot agent store. | Copilot Studio Analytics; M365 Copilot usage reports; Purview Audit. |
| Copilot Studio — Power Virtual Agents legacy bots | Copilot Studio (evolved) | Teams, web, IVR | Existing PVA bots upgraded. | Copilot Studio Analytics; App Insights; legacy PVA analytics. |
| Microsoft 365 Agents Toolkit — declarative agent | VS Code (M365 Agents Toolkit) | M365 Copilot | Pro-code authoring of declarative agents. | M365 Copilot usage reports; Purview Audit; Teams admin centre. |
| Microsoft 365 Agents Toolkit — custom engine agent | VS Code (M365 Agents Toolkit) | Teams, M365 Copilot | Pro-code authoring of custom engine agents. | Bot Service Analytics + App Insights (wired by scaffold); Purview Audit. |
| Microsoft Foundry — prompt agent | Foundry portal (no-code) | Foundry-hosted | Model + tools + knowledge configuration. | Foundry Tracing + Continuous Evaluation; Azure Monitor / App Insights; AI inference metrics. |
| Microsoft Foundry — hosted agent | Foundry Agent Service (code: Python / .NET / TS) | Foundry-hosted | Full extensibility on Agent Service. | Foundry Tracing (OpenTelemetry); Continuous Eval; Azure Monitor; Responsible AI dashboards. |
| Microsoft Foundry — multi-agent workflow | Foundry | Foundry-hosted | Orchestrated agent graphs. | Foundry Tracing with span hierarchy per agent; Continuous Eval. |
| Microsoft Foundry — agent with MCP tools | Foundry | Foundry-hosted | Agents consuming Model Context Protocol tools. | Foundry Tracing for agent; APIM AI Gateway / MCP gateway logs for tool calls. |
| Foundry Local — on-device agent | VS Code Foundry Toolkit | Local Windows / macOS | Models and agents running locally. | Local Foundry Toolkit traces; OTel export to App Insights when configured; Defender for Endpoint for device-side signals. |
| Power Automate — AI flows | Power Automate | Power Platform | RPA / workflow with AI Builder steps. | Power Platform admin analytics; CoE Starter Kit; run history. |
| AI Builder models | Power Platform | Power Platform | Embedded models inside apps and flows. | AI Builder analytics; Power Platform admin analytics. |
| Power Apps — Copilot controls | Power Apps | Power Platform | AI-powered components inside apps. | Power Apps analytics; CoE Starter Kit; Purview Audit. |
| Azure AI Bot Service bot | Bot Framework | Azure | Conversational bots predating Copilot Studio. | Bot Analytics; App Insights (default for the Bot Framework SDK). |
| Semantic Kernel / Agent Framework custom agent on Azure | VS Code / IDE | Azure (Container Apps, AKS, App Service, Functions) | Customer code; Microsoft framework. | OpenTelemetry from SK / Agent Framework → App Insights / Log Analytics; APIM AI Gateway token metrics. |

## 3. Customer-built agents — self-hosted / code-first

Agents written in customer code and hosted on customer infrastructure (Azure or elsewhere). Maximum flexibility, maximum responsibility.

| Agent | Framework | Typical runtime | Notes | Telemetry source |
| --- | --- | --- | --- | --- |
| Semantic Kernel agent | Microsoft Semantic Kernel | Azure Container Apps, AKS, App Service, Functions, on-prem | First-party Microsoft framework. | Built-in OpenTelemetry → App Insights / Log Analytics; APIM AI Gateway token metrics; container runtime metrics. |
| Microsoft Agent Framework agent | Microsoft Agent Framework | Same as above | Newer first-party framework, multi-agent native. | Native OTel tracing (per agent / tool span); App Insights; APIM AI Gateway. |
| AutoGen agent | AutoGen | Azure Container Apps, AKS, on-prem | Microsoft Research-origin multi-agent framework. | AutoGen tracing → OTel → App Insights; APIM AI Gateway. |
| LangChain agent | LangChain | Azure Container Apps, AKS, App Service, Functions | Popular third-party Python / JS framework. | LangSmith or OTel exporter → App Insights; APIM AI Gateway llm-emit-token-metric. |
| LangGraph agent | LangGraph | Same as above | Graph-style orchestration on top of LangChain. | Same as LangChain; LangGraph adds graph-state traces. |
| LlamaIndex agent | LlamaIndex | Same as above | RAG-centric. | LlamaIndex callbacks → OTel → App Insights; APIM AI Gateway; AI Search diagnostic logs. |
| CrewAI agent | CrewAI | Same as above | Multi-agent crew pattern. | CrewAI logs + OTel exporter → App Insights; APIM AI Gateway. |
| Custom in-house framework | Hand-rolled | Anywhere | Found in mature engineering orgs. | Whatever the team instruments; recommend OTel + App Insights and routing model calls via APIM. |
| Self-hosted model + agent on AKS with KAITO | Open-source (vLLM, Triton) | AKS | Customer hosts the LLM too. | Azure Monitor for containers; Managed Prometheus / Grafana; KAITO + vLLM metrics; APIM AI Gateway if proxied. |
| Edge / IoT agent | Custom | Azure IoT Edge, Azure Arc, on-device | Disconnected or latency-bound scenarios. | Azure Monitor via Arc; IoT Hub diagnostics; store-and-forward telemetry when reconnected. |

## 4. Third-party SaaS agents (vendor-built, customer-licensed)

Agents the customer's SaaS vendors ship inside their own platforms. Observed via vendor telemetry, audit logs, connectors and SaaS-posture tooling.

| Agent | Vendor / platform | Notes | Telemetry source |
| --- | --- | --- | --- |
| Joule | SAP (S/4HANA, SuccessFactors, Ariba, Concur) | SAP's enterprise generative AI assistant. | SAP audit log; SAP AI Core monitoring; SIEM connector → Sentinel; DCA. |
| Agentforce / Einstein agents | Salesforce | Includes Service, Sales, Marketing agents. | Einstein Trust Layer audit; Salesforce Event Monitoring; DCA connector → Sentinel. |
| Now Assist | ServiceNow | Across ITSM, ITOM, CSM, HRSD. | Now Assist analytics; ServiceNow system / audit logs; SIEM connector → Sentinel. |
| Illuminate / Workday agents | Workday | HR / finance generative AI. | Workday audit reports; integration logs; SIEM connector. |
| Oracle AI Agents / OCI Generative AI Agents | Oracle | Fusion Apps and OCI. | OCI Audit / Logging; Fusion audit; SIEM forwarding. |
| Adobe AI Assistant / Firefly agents | Adobe Experience Cloud / Creative Cloud | Marketing and creative workflows. | Adobe audit log; DCA. |
| Rovo | Atlassian (Jira, Confluence) | Knowledge / work assistant. | Atlassian audit log; admin analytics; DCA. |
| Breeze | HubSpot | Marketing / CRM. | HubSpot audit log + activity API; DCA. |
| Box AI | Box | Content / DMS. | Box events API; DCA connector. |
| Notion AI | Notion | Productivity. | Notion audit log (Enterprise plan); DCA. |
| Slack AI | Slack | Messaging summarisation and search. | Slack audit log API; DCA. |
| Zoom AI Companion | Zoom | Meeting assistant. | Zoom dashboard + audit reports; DCA. |
| Zendesk AI agents | Zendesk | Support automation. | Zendesk audit log; DCA. |
| Glean assistant | Glean | Enterprise search and assistant. | Glean admin analytics; audit export; DCA. |
| Snowflake Cortex agents | Snowflake | Analytics-embedded agents. | Snowflake account_usage / access history; query history. |
| Databricks AI / Mosaic agents | Databricks | Data-platform-embedded agents. | Databricks audit logs; system tables; MLflow tracing. |
| AWS Q | AWS | AWS-side operator and business assistants. | CloudTrail + Q usage logs; SIEM connector. |
| Google Gemini in Workspace | Google | Inside Docs / Gmail / Meet for users with Google Workspace. | Workspace audit logs; admin reports; DCA. |
| ChatGPT Enterprise / Team | OpenAI | Direct OpenAI subscription, often shadow-IT. | OpenAI Compliance API + usage dashboard; DCA / Edge for Business for discovery. |
| Anthropic Claude (Console / Projects) | Anthropic | Same. | Anthropic admin console; usage / billing API; DCA. |
| Perplexity Enterprise | Perplexity | Same. | Perplexity admin console + audit; DCA. |

## 5. Customer-built agents on third-party AI platforms

Agents the customer authors but on non-Microsoft platforms. They count as part of the estate and need observability and governance even though the build surface is not Microsoft's.

| Agent | Platform | Notes | Telemetry source |
| --- | --- | --- | --- |
| Bedrock Agents | AWS Bedrock | AWS-native agent service. | CloudWatch + CloudTrail; Bedrock model invocation logs; export to Sentinel via SIEM connector or S3 ingest. |
| Vertex AI Agent Builder agent | Google Cloud Vertex AI | Google-native agent service. | Cloud Logging + Cloud Trace; Vertex audit logs; SIEM export. |
| OpenAI Custom GPT | ChatGPT Enterprise / Team | Per-tenant custom GPTs. | OpenAI Compliance API + usage dashboard; DCA. |
| OpenAI Assistants API agent | OpenAI direct | Code-first OpenAI agents. | OpenAI usage / Assistants run logs; client-side OTel; APIM AI Gateway if proxied. |
| Anthropic Claude with tools | Claude API | Code-first Claude agents. | Anthropic console + usage API; client-side OTel; APIM AI Gateway if proxied. |
| Hugging Face Spaces / agents | Hugging Face | Community / OSS hosting. | HF Spaces logs; client-side OTel; DCA discovery. |
| Vendor-specific platform agent | e.g. Salesforce Prompt Builder, ServiceNow Now Assist Studio | Customer customisations on top of vendor SaaS agents. | Inherits parent SaaS audit + analytics (see section 4). |

## 6. Embedded and endpoint agents

Agents that show up at the edge of the estate — devices, browsers, plug-ins — often outside central IT's natural inventory.

| Agent | Surface | Notes | Telemetry source |
| --- | --- | --- | --- |
| Windows Copilot+ on-device agents | Copilot+ PCs (NPU) | Local inference, Recall, Click-to-Do, Cocreator. | Intune / Defender for Endpoint device diagnostics; Windows diagnostic data; very limited interaction logging. |
| Mobile Copilot apps | iOS, Android | Personal and enterprise variants. | Intune app protection + sign-in logs; M365 Copilot usage reports for enterprise variant. |
| Browser-embedded AI (Edge Copilot, Chrome Gemini, Arc / Brave AI) | Browser | Used by users with or without licence. | Edge for Business reports; DCA for shadow-AI URL discovery; network egress logs / SWG. |
| IDE agents (GitHub Copilot, Cursor, Cline, others) | Developer endpoints | Often licensed individually. | GitHub Copilot metrics API for sanctioned; DCA + endpoint EDR for unsanctioned tools. |
| Office add-ins / Outlook add-ins with AI | M365 endpoints | Vary by vendor. | M365 admin centre add-in inventory; Purview Audit; DCA. |
| SaaS in-product AI features | Hundreds of SaaS apps | Granular shadow-AI surface. | DCA app catalogue + activity policies; SWG / proxy logs. |
| Voice / IVR agents | Contact-centre platforms | Genesys, NICE, Five9, Microsoft Digital Contact Center Platform. | Contact-centre analytics; call-recording / transcript stores; Azure Communication Services + App Insights for MS DCCP. |
| Robotic / physical agents | Industrial / robotics | Out of scope for most enterprise governance today but worth flagging. | OT telemetry (Sentinel for IoT / OT, Defender for IoT); vendor robot-fleet consoles. |

## 7. Common cross-cutting categories

A few orthogonal categorisations that recur in policy discussions, regardless of where the agent lives.

| Axis | Values |
| --- | --- |
| Identity model | Acts on behalf of a user (delegated) / Acts as itself (workload identity, Microsoft Entra Agent ID) / Hybrid (delegated + own identity for tool calls). |
| Autonomy level | Suggest only / Act with approval (HITL) / Act autonomously / Multi-agent autonomous. |
| Data sensitivity | Public knowledge / Internal / Confidential / Regulated (personal data, financial, health, regulated industry). |
| Decision impact | Low-impact (drafts, search) / Medium (triage, scheduling) / High (employment, financial, safety, legal) — drives HITL and Responsible AI obligations. |
| Hosting model | Microsoft-hosted / Customer-hosted on Microsoft cloud / Customer-hosted on third-party cloud / Customer on-prem / Vendor-hosted SaaS / On-device. |
| Licensing model | Per-user (Copilot SKUs) / Per-message (Copilot Studio messages) / Per-token (Foundry, OpenAI, Anthropic) / Per-capacity (Power Platform, Fabric) / Embedded in SaaS subscription / Free / shadow. |

## 8. Open additions

Items worth confirming or adding as this list matures:

- Microsoft Entra Agent ID coverage per agent type (which agents get a first-class agent identity vs only a workload / user identity today).
- Microsoft Copilot Tuning / fine-tuned Copilot variants once GA at scale.
- Industry-specific Copilot SKUs (healthcare, public sector, financial services) as they emerge.
- Voice-only / multimodal agents (Speech Service real-time, Azure AI Voice Live API, vendor equivalents).
- Agentic browser products (OpenAI Operator, Anthropic Computer Use, others).
- Anything else the customer's estate already has that does not fit cleanly above — track it in section 4 or 5 with a one-line note.
