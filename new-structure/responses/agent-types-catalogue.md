# Agent types catalogue (first list)

| Field | Value |
| --- | --- |
| Purpose | First-pass catalogue of the agent types an enterprise typically ends up with across Microsoft and third-party platforms. Useful as input for observability scope, governance perimeter, registration / fleet management, and vendor strategy conversations. |
| Status | Draft v1 — 2026-06-23. Expect additions as the market evolves. |
| Author | Microsoft architecture |

The list groups agents by **who builds them** and **where they run**, because those two axes drive everything else (identity, telemetry, cost, governance).

## 1. Microsoft pre-built Copilots

Agents Microsoft ships as a product. The customer adopts and configures them but does not author the agent itself.

| Agent | Surface | Notes |
| --- | --- | --- |
| Microsoft 365 Copilot | Teams, Word, Excel, PowerPoint, Outlook, OneNote, Loop, web | Tenant-wide; central enterprise Copilot. |
| Microsoft 365 Copilot Chat | Web, Teams | Free / pay-as-you-go tier of M365 Copilot. |
| Copilot in Windows | Windows 11 | OS-level assistant. |
| Copilot in Edge | Edge browser | Browser-level assistant. |
| Copilot in Power BI | Power BI service | Embedded analytics Copilot. |
| Copilot in Fabric | Microsoft Fabric workloads | Data engineering, data science, real-time intelligence. |
| Copilot in Azure | Azure portal | Cloud operator assistant. |
| Copilot for Sales | Dynamics 365 Sales, Outlook, Teams | Role-based. |
| Copilot for Service | Dynamics 365 Customer Service, Teams | Role-based. |
| Copilot for Finance | Excel, Outlook, Dynamics 365 | Role-based. |
| Copilot for Security | Microsoft Security stack | SOC analyst assistant. |
| Copilot in Dynamics 365 | Dynamics 365 (CRM, Field Service, Customer Insights, Supply Chain, F&O) | Embedded per workload. |
| Copilot in Power Apps / Power Automate | Power Platform | Maker assistant. |
| GitHub Copilot | IDE, GitHub.com, CLI | Developer assistant. |
| GitHub Copilot Workspace / Coding Agent | GitHub.com | Issue-to-PR autonomous coding agent. |
| Intune Copilot, Defender Copilot, Purview Copilot | Respective admin centres | Operator assistants in security / management. |

## 2. Customer-built agents on Microsoft platforms

Agents the customer authors using Microsoft authoring surfaces. Microsoft hosts the runtime.

| Agent | Authoring surface | Runtime / surface | Notes |
| --- | --- | --- | --- |
| Copilot Studio — declarative agent | Copilot Studio (no-code) | M365 Copilot, Teams, web channels | Topics + actions + knowledge; lightweight. |
| Copilot Studio — custom engine agent | Copilot Studio | M365 Copilot, Teams, web channels | Bring-your-own orchestration / model. |
| Copilot Studio — Microsoft 365 Copilot agent | Copilot Studio | M365 Copilot chat | Published into the M365 Copilot agent store. |
| Copilot Studio — Power Virtual Agents legacy bots | Copilot Studio (evolved) | Teams, web, IVR | Existing PVA bots upgraded. |
| Microsoft 365 Agents Toolkit — declarative agent | VS Code (M365 Agents Toolkit) | M365 Copilot | Pro-code authoring of declarative agents. |
| Microsoft 365 Agents Toolkit — custom engine agent | VS Code (M365 Agents Toolkit) | Teams, M365 Copilot | Pro-code authoring of custom engine agents. |
| Microsoft Foundry — prompt agent | Foundry portal (no-code) | Foundry-hosted | Model + tools + knowledge configuration. |
| Microsoft Foundry — hosted agent | Foundry Agent Service (code: Python / .NET / TS) | Foundry-hosted | Full extensibility on Agent Service. |
| Microsoft Foundry — multi-agent workflow | Foundry | Foundry-hosted | Orchestrated agent graphs. |
| Microsoft Foundry — agent with MCP tools | Foundry | Foundry-hosted | Agents consuming Model Context Protocol tools. |
| Foundry Local — on-device agent | VS Code Foundry Toolkit | Local Windows / macOS | Models and agents running locally. |
| Power Automate — AI flows | Power Automate | Power Platform | RPA / workflow with AI Builder steps. |
| AI Builder models | Power Platform | Power Platform | Embedded models inside apps and flows. |
| Power Apps — Copilot controls | Power Apps | Power Platform | AI-powered components inside apps. |
| Azure AI Bot Service bot | Bot Framework | Azure | Conversational bots predating Copilot Studio. |
| Semantic Kernel / Agent Framework custom agent on Azure | VS Code / IDE | Azure (Container Apps, AKS, App Service, Functions) | Customer code; Microsoft framework. |

## 3. Customer-built agents — self-hosted / code-first

Agents written in customer code and hosted on customer infrastructure (Azure or elsewhere). Maximum flexibility, maximum responsibility.

| Agent | Framework | Typical runtime | Notes |
| --- | --- | --- | --- |
| Semantic Kernel agent | Microsoft Semantic Kernel | Azure Container Apps, AKS, App Service, Functions, on-prem | First-party Microsoft framework. |
| Microsoft Agent Framework agent | Microsoft Agent Framework | Same as above | Newer first-party framework, multi-agent native. |
| AutoGen agent | AutoGen | Azure Container Apps, AKS, on-prem | Microsoft Research-origin multi-agent framework. |
| LangChain agent | LangChain | Azure Container Apps, AKS, App Service, Functions | Popular third-party Python / JS framework. |
| LangGraph agent | LangGraph | Same as above | Graph-style orchestration on top of LangChain. |
| LlamaIndex agent | LlamaIndex | Same as above | RAG-centric. |
| CrewAI agent | CrewAI | Same as above | Multi-agent crew pattern. |
| Custom in-house framework | Hand-rolled | Anywhere | Found in mature engineering orgs. |
| Self-hosted model + agent on AKS with KAITO | Open-source (vLLM, Triton) | AKS | Customer hosts the LLM too. |
| Edge / IoT agent | Custom | Azure IoT Edge, Azure Arc, on-device | Disconnected or latency-bound scenarios. |

## 4. Third-party SaaS agents (vendor-built, customer-licensed)

Agents the customer's SaaS vendors ship inside their own platforms. Observed via vendor telemetry, audit logs, connectors and SaaS-posture tooling.

| Agent | Vendor / platform | Notes |
| --- | --- | --- |
| Joule | SAP (S/4HANA, SuccessFactors, Ariba, Concur) | SAP's enterprise generative AI assistant. |
| Agentforce / Einstein agents | Salesforce | Includes Service, Sales, Marketing agents. |
| Now Assist | ServiceNow | Across ITSM, ITOM, CSM, HRSD. |
| Illuminate / Workday agents | Workday | HR / finance generative AI. |
| Oracle AI Agents / OCI Generative AI Agents | Oracle | Fusion Apps and OCI. |
| Adobe AI Assistant / Firefly agents | Adobe Experience Cloud / Creative Cloud | Marketing and creative workflows. |
| Rovo | Atlassian (Jira, Confluence) | Knowledge / work assistant. |
| Breeze | HubSpot | Marketing / CRM. |
| Box AI | Box | Content / DMS. |
| Notion AI | Notion | Productivity. |
| Slack AI | Slack | Messaging summarisation and search. |
| Zoom AI Companion | Zoom | Meeting assistant. |
| Zendesk AI agents | Zendesk | Support automation. |
| Glean assistant | Glean | Enterprise search and assistant. |
| Snowflake Cortex agents | Snowflake | Analytics-embedded agents. |
| Databricks AI / Mosaic agents | Databricks | Data-platform-embedded agents. |
| AWS Q | AWS | AWS-side operator and business assistants. |
| Google Gemini in Workspace | Google | Inside Docs / Gmail / Meet for users with Google Workspace. |
| ChatGPT Enterprise / Team | OpenAI | Direct OpenAI subscription, often shadow-IT. |
| Anthropic Claude (Console / Projects) | Anthropic | Same. |
| Perplexity Enterprise | Perplexity | Same. |

## 5. Customer-built agents on third-party AI platforms

Agents the customer authors but on non-Microsoft platforms. They count as part of the estate and need observability and governance even though the build surface is not Microsoft's.

| Agent | Platform | Notes |
| --- | --- | --- |
| Bedrock Agents | AWS Bedrock | AWS-native agent service. |
| Vertex AI Agent Builder agent | Google Cloud Vertex AI | Google-native agent service. |
| OpenAI Custom GPT | ChatGPT Enterprise / Team | Per-tenant custom GPTs. |
| OpenAI Assistants API agent | OpenAI direct | Code-first OpenAI agents. |
| Anthropic Claude with tools | Claude API | Code-first Claude agents. |
| Hugging Face Spaces / agents | Hugging Face | Community / OSS hosting. |
| Vendor-specific platform agent | e.g. Salesforce Prompt Builder, ServiceNow Now Assist Studio | Customer customisations on top of vendor SaaS agents. |

## 6. Embedded and endpoint agents

Agents that show up at the edge of the estate — devices, browsers, plug-ins — often outside central IT's natural inventory.

| Agent | Surface | Notes |
| --- | --- | --- |
| Windows Copilot+ on-device agents | Copilot+ PCs (NPU) | Local inference, Recall, Click-to-Do, Cocreator. |
| Mobile Copilot apps | iOS, Android | Personal and enterprise variants. |
| Browser-embedded AI (Edge Copilot, Chrome Gemini, Arc / Brave AI) | Browser | Used by users with or without licence. |
| IDE agents (GitHub Copilot, Cursor, Cline, others) | Developer endpoints | Often licensed individually. |
| Office add-ins / Outlook add-ins with AI | M365 endpoints | Vary by vendor. |
| SaaS in-product AI features | Hundreds of SaaS apps | Granular shadow-AI surface. |
| Voice / IVR agents | Contact-centre platforms | Genesys, NICE, Five9, Microsoft Digital Contact Center Platform. |
| Robotic / physical agents | Industrial / robotics | Out of scope for most enterprise governance today but worth flagging. |

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
