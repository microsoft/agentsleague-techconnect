# 💼 Enterprise Agents - Starter Kit

**Track**: Enterprise Agents with M365 Agents Toolkit
**Time Limit**: 100 minutes

Welcome to the Enterprise Agents track! In this challenge, you will build intelligent agents that extend **Microsoft 365 Copilot** to address real-world enterprise scenarios. Your goal is to create agents that seamlessly integrate with Microsoft 365 workloads, leveraging the power of AI to automate tasks, enhance productivity, and deliver exceptional user experiences within the enterprise ecosystem.

---

> [!IMPORTANT]
> ## 🎒 Prerequisites - What to Bring
> Before the hackathon, make sure you have the following ready:
> 
> | Requirement | Description |
> |-------------|-------------|
> | 💻 **Laptop** | Bring your own laptop with your preferred development environment |
> | 🎫 **Microsoft 365 Copilot License** | You need an active Microsoft 365 Copilot license to test and deploy agents |
> | 🏢 **Tenant with Sideloading Enabled** | Access to a Microsoft 365 tenant where you can sideload custom apps for testing |
> | ☁️ **Azure Subscription** | Required to create resources for Custom Engine Agents (CEA) |

---

## 💡 Agent Development Approaches

In this track, we encourage you to create agents that extend **Microsoft 365 Copilot** using one of the following development approaches:

1. **Creating Declarative Agents (DA) with Microsoft 365 Agents Toolkit (ATK) + Visual Studio Code** - Build **Declarative Agents** using the ATK extension in VS Code. This approach allows you to define agent capabilities, actions, and behaviors through declarative configurations, enabling rapid development and iteration of enterprise-grade agents without writing custom code.

2. **Building Custom Engine Agents (CEA) with Microsoft 365 Agents Toolkit (ATK) + Visual Studio Code** - Develop **Custom Engine Agents** using the ATK extension in VS Code. This approach gives you full control over the agent's orchestration logic by writing custom code to handle conversations, integrate with external services, and implement complex business workflows. Custom Engine Agents are ideal when you need advanced customization beyond what declarative configurations offer.

3. **Copilot Studio** - Leverage Microsoft Copilot Studio to create powerful agents with a low-code/no-code experience. Copilot Studio provides a visual designer for building conversational agents that can be easily extended and customized to meet specific business needs.

## Evaluation Summary 
Your project will be evaluated across **three main dimensions**: Technical Implementation, Business Value, and Innovation & Creativity. Each dimension carries equal weight in determining the winners.

---
### 🔧 Technical Implementation (33 points)

#### Core Requirements

- ✅ Microsoft 365 Copilot Chat Agent (Required)
**Pass/Fail - Must have to qualify**

Build a functioning Copilot chat agent with natural conversation flow, context understanding, and error handling.

---

#### Additional Points

-  🌐 External MCP Server Integration (8 points)

Connect to external systems via MCP servers with read/write capabilities.

**Scoring:**
- Read-only: 3 points
- Read + Write: 8 points

---

-  🔐 OAuth Security (5 points)

Implement OAuth 2.0 authentication with secure token handling and proper consent management.

**Scoring:**
- Basic OAuth flow: 2 points
- Complete implementation: 5 points

---

- 🎨 Adaptive Cards (5 points)

Create rich, interactive UI with well-designed Adaptive Cards.

**Scoring:**
- Static cards: 2 points
- Interactive cards with actions: 5 points

---

-  🔗 Connected Agents (15 points)

Build multiple specialized agents that work together or orchestrate complex workflows.

**Scoring:**
- 2-3 agents with basic handoffs: 7 points
- 3+ agents with smart routing: 12 points
- Advanced autonomous orchestration: 15 points

#### Technical Implementation Summary

| Criterion | Points | Status | Copilot Studio | Declarative Agents (DA) with ATK | Custom Engine Agents (CEA) with ATK |
|-----------|--------|--------|----------------|----------------|-----|
| **Microsoft 365 Copilot Chat Agent** | Required | Must have |[https://microsoft.github.io/copilot-camp/pages/make/copilot-studio/04-extending-m365-copilot/](https://microsoft.github.io/copilot-camp/pages/make/copilot-studio/04-extending-m365-copilot/) | [https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/01a-geolocator/](https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/01a-geolocator/)|[https://microsoft.github.io/copilot-camp/pages/custom-engine/agents-sdk/02-agent-with-agents-sdk/](https://microsoft.github.io/copilot-camp/pages/custom-engine/agents-sdk/02-agent-with-agents-sdk/) |
| **External MCP Server Integration (Read/Write)** | 8 | Optional, encouraged |[https://microsoft.github.io/copilot-camp/pages/make/copilot-studio/06-mcp/](https://microsoft.github.io/copilot-camp/pages/make/copilot-studio/06-mcp/) | [https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/08-mcp-server/](https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/08-mcp-server/)|[https://microsoft.github.io/copilot-camp/pages/custom-engine/agent-framework/07-add-mcp-tools/](https://microsoft.github.io/copilot-camp/pages/custom-engine/agent-framework/07-add-mcp-tools/)|
| **OAuth Security for MCP Server** | 5 | Optional | [https://microsoft.github.io/agent-academy/operative/10-mcp/](https://microsoft.github.io/agent-academy/operative/10-mcp/) | [https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/10-mcp-auth/](https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/10-mcp-auth/)| |
| **Adaptive Cards for UI/UX** | 5 | Optional |[https://microsoft.github.io/agent-academy/operative/11-obtain-user-feedback/](https://microsoft.github.io/agent-academy/operative/11-obtain-user-feedback/) | | |
| **Connected Agents Architecture** | 15 | Higher rating |[https://microsoft.github.io/copilot-camp/pages/make/copilot-studio/09-connected-agents/](https://microsoft.github.io/copilot-camp/pages/make/copilot-studio/09-connected-agents/)|[https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/09-connected-agent/](https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/09-connected-agent/) | |
| **TOTAL TECHNICAL POINTS** | **33** | | | | |

---

### 💼 Business Value (33 points)

**What we're looking for:**
- Addresses a genuine pain point in your organization
- Solution is relevant to many users, not just one department
- Clear understanding of current workflow vs. improved workflow

---

### 💡 Innovation & Creativity (34 points)

**What we're looking for:**
- Non-obvious approach to the challenge
- Elegant solutions to complex problems
- Combining capabilities in unexpected ways
- "Aha!" moments in the design

---

### 📊 Final Scoring Overview

| Dimension | Points | % of Total |
|-----------|--------|-----------|
| **Technical Implementation** | 33 | 33% |
| **Business Value** | 33 | 33% |
| **Innovation & Creativity** | 34 | 34% |
| **TOTAL POSSIBLE POINTS** | **100** | 100% |

---

## Real-World Enterprise Scenarios

If you like, take inspiration from the following real-world enterprise scenarios to guide your project:

- **Human Resources (HR) Agent**: Build an agent that helps employees navigate HR policies, submit time-off requests, access benefits information, onboard new hires, or manage performance reviews. The agent could integrate with HR systems to provide personalized responses and automate routine HR tasks.

- **Research & Development (R&D) Agent**: Create an agent that assists R&D teams in accessing research documentation, managing intellectual property, tracking project milestones, or collaborating on innovation initiatives. The agent could help researchers find relevant prior work, summarize technical documents, or coordinate cross-functional teams.

- **Supply Chain Management Agent**: Develop an agent that provides visibility into supply chain operations, tracks inventory levels, monitors supplier performance, or predicts potential disruptions. The agent could help procurement teams make data-driven decisions and optimize logistics operations.

- **Finance & Accounting Agent**: Design an agent that assists with expense reporting, budget tracking, financial forecasting, or compliance reporting. The agent could automate data extraction from invoices, provide spending insights, or alert stakeholders to anomalies.

- **IT Helpdesk Agent**: Build an agent that handles IT support tickets, troubleshoots common issues, guides users through self-service resolutions, or escalates complex problems to human agents. The agent could integrate with IT service management systems to provide contextual assistance.

- **Legal & Compliance Agent**: Create an agent that helps legal teams review contracts, identify compliance risks, track regulatory changes, or manage legal document workflows. The agent could leverage AI to extract key terms and flag potential issues.

- **Sales Enablement Agent**: Develop an agent that provides sales teams with real-time access to product information, competitive intelligence, customer insights, or sales playbooks. The agent could help prepare for meetings and track deal progress.

- **Insurance Claims Processing Agent**: Build an agent that helps insurance adjusters and claims processors manage property damage claims efficiently. The agent assists with tracking claim status, estimating repair costs, coordinating contractor assignments, and prioritizing emergency response cases.

Feel free to combine multiple scenarios or create entirely new use cases that address specific challenges within your organization or industry.

---

## 🚀 Quick Start

Get started quickly by exploring the following resources that provide step-by-step guidance for building enterprise agents:

### Copilot Dev Camp

The **Copilot Dev Camp** is your one-stop destination for learning how to build agents that extend Microsoft 365 Copilot. Access comprehensive tutorials, hands-on labs, and sample code to accelerate your development journey.

🔗 **Main Portal**: [https://aka.ms/copilotdevcamp](https://aka.ms/copilotdevcamp)

### Building with Copilot Studio

Learn how to create powerful agents using Microsoft Copilot Studio's visual designer and low-code capabilities:

🔗 **Copilot Studio Guide**: [https://microsoft.github.io/copilot-camp/pages/make/copilot-studio/](https://microsoft.github.io/copilot-camp/pages/make/copilot-studio/)

### Extending Microsoft 365 Copilot

Discover how to extend Microsoft 365 Copilot with custom agents, plugins, and connectors:

🔗 **Extend M365 Copilot**: [https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/](https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/)

### Building agents for Microsoft 365 Copilot

Discover how to build Custom Engine Agents for Microsoft 365 Copilot:

🔗 **Build for M365 Copilot**: [https://microsoft.github.io/copilot-camp/pages/custom-engine/](https://microsoft.github.io/copilot-camp/pages/custom-engine/)

### Agent Academy

The **Agent Academy** provides structured learning paths and expert-led training to help you master agent creation with Microsoft Copilot Studio. Whether you're new to building agents or looking to enhance your skills, Agent Academy offers curated content to guide you through the entire development lifecycle in Copilot Studio.

🔗 **Agent Academy**: [https://aka.ms/agentacademy](https://aka.ms/agentacademy)

### Getting Started Checklist

1. ✅ Visit the Copilot Dev Camp portal and review the available learning paths
2. ✅ Set up your development environment (VS Code + Microsoft 365 Agents Toolkit or Copilot Studio)
3. ✅ Explore the sample projects and templates provided in the documentation
4. ✅ Identify your target enterprise scenario and define your agent's capabilities
5. ✅ Start building and iterating on your solution

### Step by Step Starter Kit

Follow these step-by-step guides to get started with each development approach:

#### 🔹 Declarative Agents (DA)

Build Declarative Agents using Microsoft 365 Agents Toolkit in Visual Studio Code:

1. **Install Visual Studio Code**
   - Download and install VS Code from [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

2. **Install Microsoft 365 Agents Toolkit (ATK)**
   - Open VS Code and navigate to the Extensions view (`Ctrl+Shift+X`)
   - Search for "Microsoft 365 Agents Toolkit" and click **Install**
   - Alternatively, install from the marketplace: [https://marketplace.visualstudio.com/items?itemName=TeamsDevApp.ms-teams-vscode-extension](https://marketplace.visualstudio.com/items?itemName=TeamsDevApp.ms-teams-vscode-extension)

3. **Install Prerequisites**
   - Install [Node.js](https://nodejs.org/) (LTS version recommended)
   - Ensure you have a Microsoft 365 developer tenant with Copilot enabled
   - Sign in to your Microsoft 365 account in VS Code using ATK

4. **Create a New Declarative Agent**
   - Open the Command Palette (`Ctrl+Shift+P`) and select **M365 Agents Toolkit: Create a New App**
   - Choose **Agent** → **Declarative Agent**
   - Follow the wizard to configure your agent's name, capabilities, and grounding sources
   - ATK will scaffold the project with the declarative manifest and configuration files

5. **Configure and Test**
   - Define your agent's instructions and knowledge sources in the declarative manifest
   - Press `F5` to launch your agent in Microsoft 365 Copilot for testing
   - Iterate on your agent's configuration based on test results

#### 🔹 Custom Engine Agents (CEA)

Build Custom Engine Agents with full code control using Visual Studio and C#:

1. **Install Visual Studio**
   - Download and install Visual Studio 2022 (Community, Professional, or Enterprise) from [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
   - During installation, select the **ASP.NET and web development** workload
   - Also select the **Azure development** workload for cloud deployment capabilities

2. **Install Microsoft 365 Agents Toolkit (ATK)**
   - Open Visual Studio and navigate to **Extensions** → **Manage Extensions**
   - Search for "Microsoft 365 Agents Toolkit" and click **Download**
   - Restart Visual Studio to complete the installation
   - Alternatively, download from the marketplace: [https://marketplace.visualstudio.com/items?itemName=TeamsDevApp.MicrosoftTeamsToolkit2022](https://marketplace.visualstudio.com/items?itemName=TeamsDevApp.MicrosoftTeamsToolkit2022)

3. **Install Prerequisites**
   - Install [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) (required for C# agent development)
   - Install [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) for Azure resource provisioning
   - Ensure you have a Microsoft 365 developer tenant and Azure subscription
   - Sign in to your Microsoft 365 and Azure accounts in Visual Studio

4. **Create a New Custom Engine Agent**
   - In Visual Studio, select **File** → **New** → **Project**
   - Search for "Microsoft 365 Agent" or use the ATK project templates
   - Choose **Custom Engine Agent** with **C#** as the language
   - Configure your project name, location, and solution settings
   - Select an AI model provider (Azure OpenAI recommended for enterprise scenarios)
   - ATK will scaffold the C# project with Bot Framework integration and AI orchestration code

5. **Implement Your Agent Logic**
   - Customize the agent's conversation handling in the generated C# code
   - Use dependency injection and strongly-typed models for maintainable code
   - Integrate with external APIs and MCP servers using HttpClient or SDK libraries
   - Implement authentication flows using Microsoft Entra ID and MSAL.NET
   - Add Adaptive Card responses for rich UI experiences using the AdaptiveCards NuGet package

6. **Test and Deploy**
   - Press `F5` to run your agent locally with the Bot Framework Emulator
   - Use Visual Studio's debugging tools to set breakpoints and inspect variables
   - Test in Microsoft 365 Copilot using the sideloading feature
   - Deploy to Azure App Service or Azure Container Apps using Visual Studio's publish feature or ATK's deployment commands

#### 🔹 Microsoft Copilot Studio (MCS)

Build agents using the low-code/no-code Microsoft Copilot Studio platform:

1. **Access Microsoft Copilot Studio**
   - Navigate to [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
   - Sign in with your Microsoft 365 organizational account
   - Ensure you have the appropriate Copilot Studio license

2. **Create a New Agent**
   - Click **Create** on the home page
   - Choose **New agent** to start from scratch or select a template
   - Provide a name and description for your agent
   - Configure the agent's primary language and tone

3. **Configure Knowledge Sources**
   - Add knowledge sources such as SharePoint sites, websites, or uploaded documents
   - Configure the agent to ground responses in your organizational data
   - Set up data source authentication if required

4. **Design Conversation Topics**
   - Create topics to handle specific user intents
   - Use the visual authoring canvas to design conversation flows
   - Add trigger phrases that activate each topic
   - Configure actions, conditions, and variable handling

5. **Extend with Actions and Tools**
   - Add Power Automate flows to integrate with external systems
   - Configure tools to read/write data from MCP servers or APIs
   - Set up authentication for secure connector access

6. **Publish and Deploy**
   - Test your agent using the built-in test chat
   - Publish your agent to make it available in Microsoft 365 Copilot
   - Configure channels (Teams, web, etc.) for deployment
   - Monitor usage and iterate based on analytics

---

## 📚 Resources

Explore the following resources to deepen your knowledge and accelerate your development:

### Copilot Dev Camp

Your comprehensive learning destination for building agents that extend Microsoft 365 Copilot:

🔗 [https://aka.ms/copilotdevcamp](https://aka.ms/copilotdevcamp)

### Agent Academy

Structured learning paths and expert-led training for mastering agent development with Microsoft Copilot Studio:

🔗 [https://aka.ms/agentacademy](https://aka.ms/agentacademy)

### Microsoft Learn

Access official Microsoft documentation, tutorials, and learning paths:

- **Microsoft 365 Copilot Documentation**: [https://learn.microsoft.com/microsoft-365-copilot/](https://learn.microsoft.com/microsoft-365-copilot/)
- **Copilot Studio Documentation**: [https://learn.microsoft.com/microsoft-copilot-studio/](https://learn.microsoft.com/microsoft-copilot-studio/)
- **Declarative Agents**: [https://aka.ms/declarative-agents-docs](https://aka.ms/declarative-agents-docs)
- **Microsoft 365 Agents Toolkit**: [https://aka.ms/m365-agents-toolkit](https://aka.ms/m365-agents-toolkit)
- **Microsoft Entra ID Documentation**: [https://learn.microsoft.com/entra/identity/](https://learn.microsoft.com/entra/identity/)
- **Adaptive Cards Documentation**: [https://learn.microsoft.com/adaptive-cards/](https://learn.microsoft.com/adaptive-cards/)
- **Model Context Protocol (MCP)**: [https://learn.microsoft.com/azure/ai-services/agents/](https://learn.microsoft.com/azure/ai-services/agents/)


### Additional Resources

- **10 MCP Servers to Get You Started**: [https://developer.microsoft.com/blog/10-microsoft-mcp-servers-to-accelerate-your-development-workflow](https://developer.microsoft.com/blog/10-microsoft-mcp-servers-to-accelerate-your-development-workflow)
- **Microsoft Graph API**: [https://learn.microsoft.com/graph/](https://learn.microsoft.com/graph/)
- **Microsoft 365 Developer Program**: [https://developer.microsoft.com/microsoft-365/dev-program](https://developer.microsoft.com/microsoft-365/dev-program)

---

## 🎯 Winning Strategy Tips

### Balance All Three Dimensions
Don't just focus on technical complexity. A simple but highly valuable solution with great UX can beat a technically sophisticated but impractical one.

### Quality Over Quantity
It's better to do one thing exceptionally well than five things poorly. Nail your core use case first.

### Show, Don't Tell
Your demo should speak for itself. Let judges experience the value rather than just hearing about it.

### Know Your Users
The best solutions come from deep empathy with the people who have the problem. Talk to them early and often.

### Think Production-Ready
Even in a hackathon, show you're thinking about security, scalability, and real-world deployment.
## ❓ FAQ

### Can I use vibe-coding?

**Yes!** You are welcome to use vibe-coding approaches and AI-assisted development tools to build your solution. Leveraging AI coding assistants like GitHub Copilot to accelerate your development is encouraged.

### Can I use community and open source libraries/SDKs?

**Yes!** You can use community-contributed and open source libraries, SDKs, and frameworks in your solution. Open source tools are a great way to accelerate development and leverage the collective work of the developer community.

### Can I use commercial/proprietary libraries/SDKs?

**No.** The use of commercial or proprietary libraries and SDKs that require paid licenses or are not freely available is not permitted. Your solution should be built using open source or freely available tools to ensure accessibility and reproducibility.

### Can I share a real project that I've been working on for my company or for a customer?

**No.** You cannot submit existing projects that were developed for your company or for customers. All submissions must be original work created specifically for this hackathon. This ensures a fair competition and protects any confidential or proprietary information.

### Do I need to use my own tenant?

**Yes.** Candidates are expected to use their own Microsoft 365 tenant for development and testing. We recommend using a dedicated developer tenant to avoid impacting production environments. For detailed information on setting up a Copilot development environment, please refer to the [Microsoft 365 Copilot extensibility prerequisites](https://aka.ms/extend-Copilot-sandbox).

### Is the MCP server integration really optional?
**Yes,** but teams that include it (especially with read/write capabilities) will score significantly higher on technical implementation. It's worth the effort!

### What if we have great business value but simpler technical implementation?
**That's completely fine!** Each dimension is weighted equally. A highly valuable, well-designed solution with solid (not fancy) tech can definitely win.

### Can we score points in Connected Agents without MCP servers?
**Yes!** You could build connected agents that work together within the Copilot ecosystem, even without external integrations.

### Should we build for breadth or depth?
**Depth.** Do one thing incredibly well. It's better to solve one problem end-to-end than to half-solve three problems.

---

Good luck! We can't wait to see what you build. 🚀

**Need help?** Raise your hand - roaming experts are here to assist you!
