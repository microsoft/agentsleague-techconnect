# 🧠 Reasoning Agents - Starter Kit

**Track**: Reasoning Agents with Microsoft Foundry  
**Time Limit**: 100 minutes

Welcome to the Reasoning Agents track! In this challenge, you'll build intelligent agents using **Microsoft Foundry** (formerly Azure AI Foundry) that can solve complex problems through multi-step reasoning.

---

## 🚀 Getting Started with Microsoft Foundry

### What is Microsoft Foundry?

Microsoft Foundry is your unified platform for building AI applications. It provides:
- Access to powerful AI models (GPT-4o, o1, o3-mini, and more)
- Tools for building agents with reasoning capabilities
- Integration with Azure services
- Built-in evaluation and monitoring

### 👉 [Open Microsoft Foundry](https://ai.azure.com)

---

## 💡 Project Ideas

Here are some ideas that showcase multi-step reasoning:

### Beginner-Friendly
- **Research Assistant** - An agent that researches a topic and summarizes findings
- **Decision Helper** - Help users make decisions by analyzing pros/cons
- **Fact Checker** - Verify claims by reasoning through evidence
- **Problem Solver** - Break down complex problems into steps

### Intermediate
- **Code Explainer** - Explain code step-by-step with reasoning
- **Travel Planner** - Plan trips with logical reasoning about constraints
- **Recipe Recommender** - Suggest recipes based on ingredients with reasoning
- **Debugging Assistant** - Help debug code through systematic analysis

### Advanced
- **Multi-Agent System** - Multiple agents that collaborate on tasks
- **Self-Correcting Agent** - An agent that validates and improves its own responses
- **Chain-of-Thought Visualizer** - Show the agent's reasoning process

---

## 🎯 Quick Start Options

### Option 1: Use Microsoft Foundry Portal (Recommended)

1. Go to [ai.azure.com](https://ai.azure.com)
2. Create or select a project
3. Deploy a model (GPT-4o recommended for reasoning)
4. Use the **Playground** to prototype your agent
5. Export your code when ready

### Option 2: Use the Azure AI SDK

```python
# Install the SDK
pip install azure-ai-projects azure-identity

# Quick example
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint="your-foundry-endpoint"
)

# Build your agent logic here
```

### Option 3: Use GitHub Models

If you have access to GitHub Models, you can prototype quickly:
1. Go to [github.com/marketplace/models](https://github.com/marketplace/models)
2. Try models directly in the browser
3. Copy the code snippet to your project

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

## 📚 Resources

### Microsoft Foundry
- [Microsoft Foundry Portal](https://ai.azure.com)
- [Azure AI Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)

### Reasoning & Prompting
- [Prompt Engineering Guide](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [Chain-of-Thought Prompting](https://www.promptingguide.ai/techniques/cot)
- [ReAct Pattern](https://www.promptingguide.ai/techniques/react)

### Code Samples
- [Azure AI Samples](https://github.com/Azure-Samples/azure-ai-samples)
- [Azure OpenAI Samples](https://github.com/Azure-Samples/openai)

---

## 🆘 Need Help?

- **Raise your hand** - Roaming experts are here to help
- **Ask your tablemates** - Collaborate and learn together
- **Check Microsoft Foundry docs** - [ai.azure.com](https://ai.azure.com)

---

## ❓ FAQ

### What models should I use?

- **GPT-4o** - Great balance of speed and capability
- **o1 / o3-mini** - Best for complex reasoning tasks
- **GPT-4o-mini** - Fast and cost-effective for simpler tasks

### Do I need to write code?

Not necessarily! You can:
- Use the Foundry Playground to build and test
- Export code when you're ready
- Or build entirely in the portal

### What if I don't have Azure access?

Talk to a roaming expert - we can help you get access or find an alternative approach.

---

**Good luck! Build an agent that thinks! 🧠**
