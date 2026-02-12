# 🧠 Reasoning Agents - Starter Kit

**Track**: Reasoning Agents with Microsoft Foundry  

**Time Limit**: 100 minutes

Welcome to the Reasoning Agents track! In this challenge, you'll build intelligent agents using **Microsoft Foundry** that can solve complex problems through multi-step reasoning.

---

## ⚠️ Security and Confidentiality Requirements

**CRITICAL: This repository is PUBLIC. Protect confidential information.**

Before submitting your project, you **MUST** ensure your code does NOT contain:

- ❌ **API keys, passwords, tokens, or credentials** - Use Azure Key Vault or environment variables
- ❌ **Customer data or PII** - No real user data, emails, or personal information
- ❌ **Microsoft Confidential information** - Only General-level content is permitted
- ❌ **Azure deployment details** - Remove subscription IDs, resource names, and connection strings
- ❌ **Proprietary algorithms or trade secrets** - Original work or properly licensed code only

### Security Best Practices for Azure/Foundry Projects

✅ **DO:**
- Use Azure Managed Identities for authentication instead of API keys
- Store secrets in Azure Key Vault and reference them securely
- Use environment variables for configuration (`.env` files in `.gitignore`)
- Provide example configuration files with placeholder values
- Use `DefaultAzureCredential` for local development authentication
- Review Azure resource configurations before committing

❌ **DON'T:**
- Hardcode Azure OpenAI endpoints or API keys
- Commit connection strings or SAS tokens
- Include Azure subscription IDs or tenant information
- Share screenshots of Azure Portal containing sensitive details
- Commit deployment credentials or service principal secrets

### Required Actions

1. **Review the Repository Disclaimer**: Read **[../../DISCLAIMER.md](../../DISCLAIMER.md)** for complete guidelines
2. **Scan Your Code**: Check all files, including config files, for sensitive information
3. **Test Locally First**: Ensure your project works without hardcoded credentials
4. **Verify Your Submission**: Confirm your project contains only public, non-confidential content

By submitting your project, you confirm compliance with these security requirements and acknowledge that violations may result in disqualification.

---

> [!IMPORTANT]
> ## 🎒 Prerequisites - What to Bring
> Before the hackathon, make sure you have the following ready:
> 
> | Requirement | Description | Applies To |
> |-------------|-------------|------------|
> | 💻 **Laptop** | Bring your own laptop and make sure you have internet access | Low-code & Code-first |
> | ☁️ **Azure Subscription** | With GPT model quotas available for deploying reasoning models - 100k–300k TPM | Low-code & Code-first  |
> | 🧑‍💻 **A code editor** | Visual Studio code recommended| Code-First |
> | 🐍 **Python 3.10+** | If you plan to use the Python Foundry SDK, ensure Python 3.10 or higher is installed | Code-First |
> | ⌨️ **Azure CLI** | Required for authentication when using the Python Foundry SDK | Code-First |
> | 📦 **pip** | Python package manager needed to install the Foundry SDK and dependencies | Code-First |

---

## 🚀 Getting Started with Microsoft Foundry

### What is Microsoft Foundry?

[Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry/) is your unified platform for building, testing and deploying AI agents and applications. It provides:

- Access to powerful AI models from several providers
- Tools for building agents with reasoning capabilities
- Integration with Azure services
- Built-in evaluation and monitoring
- Enterprise-grade security and compliance
- Interoperability through standard protocols like [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) or [Agent2Agent (A2A)](https://a2a-protocol.org/latest/).

---

## 💡 Project Scenario

The goal of this track is to build an AI agent that can *effectively assists the communication team of a company in creating social media content* for various platforms.
Feel creative and choose a specific industry or type of brand to focus on, such as technology, fashion, food, or travel.

By completing this challenge, you should be able to:

- **Design** and implement an AI agent using Microsoft Foundry
- **Instruct** the agent on the task to achieve and incorporate reasoning patterns to enhance the agent's problem-solving abilities
- **Ground** the AI Agent on data sources relevant to the selected industry or brand
- **Integrate** the agent with external tools via MCP servers or APIs

---

## 📍Project Milestones

1. **Set up your environment in Microsoft Foundry**:
    - Access Microsoft Foundry and set up your project
    - Choose a model suitable for reasoning tasks (e.g., GPT-5.1, GPT-5.2, claude-opus-4-5, etc) and deploy an instance
    - Launch the playground and familiarize yourself with the interface

2. **Create your agent**:
    - Create your **social media communication** agent, based on the LLM model you deployed
    - Define the agent's instructions including:
        - Task description
        - Brand/Industry context
        - Target audience and platforms
        - Tone and style guidelines
    - Implement reasoning patterns (e.g., Chain-of-Thought, ReAct)
    - Test the agent's responses and refine its logic

3. **Add grounding knowledge**:
    - Integrate relevant data sources (e.g., brand guidelines, industry trends)
    - Use retrieval techniques to provide context to the agent
    - Ensure the agent can reference this information in its responses
    
> [!TIP]
> No data source for the chosen use case? Create a *synthetic dataset* - it can be as simple as a file world document or a spreadsheet - using Microsoft 365 Copilot or GitHub Copilot in Visual Studio Code. Then add it to your agent through [*File Search*](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/file-search?view=foundry&pivots=python). An alternative is to use data from the web via web search tools - such as [*Bing Search tool*](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/bing-tools?view=foundry&pivots=python).

4. **Add external tools**:
    Integrate external tools to enable your agent to perform actions beyond text generation. You can integrate with tools exposed by remote MCP servers or APIs via OpenAPI. Examples include:

    - Retrieving validated information to inform social posts using knowledge retrieval tools exposed by MCP servers, such as the [Microsoft Learn MCP server](https://github.com/microsoftdocs/mcp).
    - Saving content drafts in a local file using the [file system MCP server](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem) tools.
    - Scheduling posts using a social media management API, such as the [Linkedin API](https://learn.microsoft.com/linkedin/).
    Feel free to get creative and explore other tools that can enhance your agent's capabilities! A good starting point is to explore the [Visual Studio Code MCP Registry](https://code.visualstudio.com/mcp).

---

## 🎯 Quick Start Options

### Option 1: Use Microsoft Foundry Portal

1. Go to [ai.azure.com](https://ai.azure.com)
1. Enable the 'New Foundry' toggle at the top to access the latest Foundry experience
1. Create a project
1. Deploy a reasoning model from the catalog (e.g. gpt-5.1, gpt-5.2, claude-opus-4-5, etc)
1. Use the **Playground** to prototype your agent
1. (Optional) Export your code when ready

> [!TIP]
> From the *Code* tab in the Playground, you can also *Open in VSCode for the Web* to access and execute the code in a pre-configured environment in your browser.

Learn more at: [Quickstart: Create a new agent with Foundry Portal](https://learn.microsoft.com/azure/ai-foundry/agents/quickstart?view=foundry-classic&pivots=ai-foundry-portal)

### Option 2: Use the Microsoft Foundry SDK

```python
# Install the SDK
pip install azure-ai-projects
pip install azure-identity

# Login to Azure 
az login

# Instantiate the project client
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project_client = AIProjectClient(
    endpoint=os.getenv("PROJECT_ENDPOINT"),
    credential=DefaultAzureCredential(),  
)

# Build your agent logic here
```

Explore the full quickstart example at [Quickstart: Create a new agent with Python Foundry SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/quickstarts/get-started-code?view=foundry-classic&tabs=python).

> [!NOTE]
> The Foundry SDK is available in multiple languages including Python, C#, and Java.

---

## 🧠 Reasoning Patterns to Try

### Chain-of-Thought

Ask the model to think step by step:

```
"Let's solve this step by step:
1. First, I'll identify...
2. Then, I'll analyze...
3. Finally, I'll conclude..."
```

### ReAct (Reasoning + Acting)

Combine thinking with actions:

```
Thought: What do I need to find out?
Action: Search for information
Observation: Here's what I found...
Thought: Based on this, I should...
```

### Self-Reflection

Have the agent check its own work:

```
Initial Answer: [response]
Reflection: Is this correct? What could be wrong?
Revised Answer: [improved response]
```

---

## 🌟 (Bonus) Going Further

If you have extra time, consider adding some enterprise readiness features to your agent:

- **Evaluation**: Set up evaluation metrics to assess your agent's performance using [Foundry's built-in evaluation tools](https://learn.microsoft.com/azure/ai-foundry/how-to/evaluate-generative-ai-app?view=foundry&preserve-view=true).
- **Monitoring**: Implement monitoring to track your agent's usage and performance over time.
- **Safety**: Add safety mitigation layers to ensure your agent adheres to company policy, generate no harmful content, and is protected against prompt injections.

Another suggestion is to further extend your system, enabling your agent to interact with other agents in a **multi-agent architecture**. For example, you can:

- Break down the overall task into smaller, manageable sub-tasks, handled by specialized agents for content ideation, content creation, and content scheduling.
- Create a reviewer agent that checks the content created by the main agent for quality and compliance.

---

## 📚 Resources

### Official Documentation

- **Microsoft Foundry Documentation**: [https://learn.microsoft.com/azure/ai-foundry/](https://learn.microsoft.com/azure/ai-foundry/)
- **Microsoft Foundry Agent Service Overview**: [https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview?view=foundry&preserve-view=true](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview?view=foundry&preserve-view=true)
- **Microsoft Foundry quick starter**: [https://learn.microsoft.com/training/modules/ai-agent-fundamentals/](https://learn.microsoft.com/training/modules/ai-agent-fundamentals/)
- **Observability in Microsoft Foundry**: [https://learn.microsoft.com/azure/ai-foundry/control-plane/overview?view=foundry](https://learn.microsoft.com/azure/ai-foundry/control-plane/overview?view=foundry)
- **Code-first evaluation with Microsoft Foundry SDK**: [https://learn.microsoft.com/azure/ai-foundry/how-to/develop/cloud-evaluation?view=foundry&tabs=python](https://learn.microsoft.com/azure/ai-foundry/how-to/develop/cloud-evaluation?view=foundry&tabs=python)
- **Responsible AI in Microsoft Foundry**: [https://learn.microsoft.com/azure/ai-foundry/responsible-use-of-ai-overview?view=foundry](https://learn.microsoft.com/azure/ai-foundry/responsible-use-of-ai-overview?view=foundry)

### OSS Repos and Samples

- **AI Agents for Beginners Course**: [aka.ms/ai-agents-beginners](https://aka.ms/ai-agents-beginners)
- **AI assisted development with GitHub Copilot**: [https://github.com/github/awesome-copilot](https://github.com/github/awesome-copilot)
- **Step-by-step agent building lab**: [https://jolly-field-035345f1e.2.azurestaticapps.net/](https://jolly-field-035345f1e.2.azurestaticapps.net/)

### Community

- **Microsoft Foundry Discord Community**: [https://aka.ms/foundry/devs](https://aka.ms/foundry/devs) - Connect with other developers, ask questions, and share your projects

---

## 🆘 Need Help?

- **Raise your hand** - Roaming experts are here to help
- **Ask your tablemates** - Collaborate and learn together
- **Join the community** - [Microsoft Foundry Discord Community](https://aka.ms/foundry/devs)
- **Check learning resources above**

---

## ❓ FAQ

### What models should I use?

You can use any of the reasoning-capable models available in Microsoft Foundry, no matter which provider they come from.

### Do I need to write code?

Not necessarily! You can:
- Use the Foundry Playground to build and test
- Export code when you're ready
- Or build entirely in the portal

### What if I don't have Azure access?

Talk to a roaming expert - we can help you get access or find an alternative approach.

---

**Good luck! And have fun 🚀**
