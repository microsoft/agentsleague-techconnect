# 🎨 Creative Apps - Starter Kit

**Track**: Battle #1 - Creative Apps with GitHub Copilot  

Welcome to the Creative Apps track! In this challenge, you will harness the power of **GitHub Copilot** and **VS Code** to build innovative, imaginative applications that push your creativity. Your goal is to create applications that showcase the potential of AI-assisted development while delivering unique, engaging user experiences. All application types are welcome — web apps, CLI tools, games, mobile apps, desktop applications, and beyond—**maximum creativity is encouraged!**

---

## 💡 Project Ideas

In this track, we encourage you to build creative applications that demonstrate the power of AI-assisted development with GitHub Copilot. **We especially welcome [Copilot CLI SDK](https://github.com/github/copilot-sdk) tools and [WorkIQ MCP](https://github.com/microsoft/work-iq-mcp) projects!** Here are some categories and ideas to inspire your project:

### 📊 Business Intelligence & Analytics

Build tools that help organizations make data-driven decisions:

- **Meeting Insights Dashboard**: Aggregate meeting notes and action items across teams to surface trends, overdue tasks, and team bandwidth at a glance
- **Sales Pipeline Analyzer**: A CLI or web tool that visualizes pipeline health, forecasts revenue, and identifies at-risk deals before they slip
- **Customer Feedback Synthesizer**: Aggregate feedback from multiple channels (support tickets, surveys, social) to identify product improvement opportunities

> **MCP Integration Tip**: Use **WorkIQ MCP** to connect with Microsoft 365, pulling data from Teams, Outlook, and SharePoint to create comprehensive business views.

### 🤝 Team Collaboration & Communication

Create applications that improve how teams work together:

- **Smart Standup Bot**: A CLI tool that collects async standup updates from team members, summarizes blockers, and posts digests to your team channel
- **Knowledge Base Builder**: Automatically organize and surface relevant documentation from wikis, code repos, and communication channels

> **MCP Integration Tip**: Use the **GitHub MCP** to pull team activity from repos and issues, then combine with **WorkIQ MCP** to correlate with Teams messages and calendar events.

### 📝 Document & Content Workflow

Build tools that streamline content creation and management:

- **Proposal Generator**: Generate customized business proposals by pulling in project context, client history, and templates
- **Release Notes Automator**: A CLI that aggregates commits, PRs, and issues to generate polished release notes for different audiences (technical, executive, customer-facing)
- **Policy Compliance Checker**: Scan documents against company policies and regulatory requirements, flagging issues and suggesting corrections

> **MCP Integration Tip**: Use **GitHub MCP** to pull commits and PRs for release notes, **Microsoft Learn MCP** to reference documentation standards, and **WorkIQ MCP** to access SharePoint templates.

### 📅 Resource & Project Management

Develop tools that optimize planning and execution:

- **Capacity Planning Assistant**: Analyze team calendars, sprint velocity, and upcoming commitments to recommend realistic project timelines
- **Budget Tracker**: Provide real-time budget vs. actual reporting by connecting financial data with project milestones
- **Vendor Management Dashboard**: Aggregate contract details, renewal dates, and performance metrics to streamline vendor relationships

> **MCP Integration Tip**: **WorkIQ MCP** excels at connecting Microsoft 365 data — combine Outlook calendars, Teams availability, and Planner tasks for comprehensive resource views.

### 🎯 Building Meaningful Projects

When choosing your project, consider these principles:

1. **Solve a Real Problem**: Focus on pain points you or your team experience daily. The best projects address genuine friction in workflows.

2. **Leverage MCP's Strengths**: MCP shines when connecting multiple data sources. Think about what insights emerge when you combine information from different tools.

3. **Consider Your Users**: Who will benefit from this tool? Developers? Managers? The whole organization? Design for their specific needs and workflows.

4. **Start Small, Expand Later**: Begin with a focused MVP that demonstrates value, then plan how MCP connections could extend functionality.

5. **Think About Data Flow**: Map out which systems contain the data you need, what transformations add value, and where results should be surfaced.

> 💡 **Build for GitHub Copilot**: Consider building MCP servers that integrate directly with GitHub Copilot in VS Code! Your MCP server can expose tools and data sources that Copilot can use during chat conversations, making your solution available to developers right where they work. See the [MCP in VS Code documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for how to connect MCP servers to Copilot and the [VS Code blog](https://code.visualstudio.com/blogs/2026/01/26/mcp-apps-support) for the latest on MCP Apps Support.

Feel free to combine categories, invent entirely new concepts, or explore areas not listed here. **There are no restrictions on application type or technology stack — web, CLI, mobile, desktop, embedded, VR/AR, and more are all welcome!**

---

## 🚀 Quick Start

Get started quickly by setting up VS Code and GitHub Copilot. Follow the official [VS Code Setup Guide](https://code.visualstudio.com/docs/setup/setup-overview) for detailed platform-specific instructions.

<details>
<summary><strong>📥 Setup Steps (click to expand)</strong></summary>

### Step 1: Download and Install VS Code

Download and install Visual Studio Code for your platform:

- [macOS](https://code.visualstudio.com/docs/setup/mac)
- [Linux](https://code.visualstudio.com/docs/setup/linux)
- [Windows](https://code.visualstudio.com/docs/setup/windows)

VS Code is lightweight (< 200 MB download) and ships monthly releases with auto-update support.

> **Note:** If you choose to use VS Code Insiders, you will have access to the latest features but you may encounter occasional instability.

### Step 2: Install Additional Components

Install development tools based on your project needs:

- [Git](https://git-scm.com/) for version control
- [Node.js](https://nodejs.org/) for JavaScript/TypeScript development
- Language runtimes for Python, Java, Go, or other languages you plan to use

See the full list of [additional components](https://code.visualstudio.com/docs/setup/additional-components).

### Step 3: Install VS Code Extensions

Customize VS Code with extensions from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/VSCode):

- Formatters
- Language extensions and debuggers
- Tools for your favorite frameworks

### Step 4: Enable AI Features with GitHub Copilot

Follow the [Copilot Setup Guide](https://code.visualstudio.com/docs/copilot/setup) to enable AI-powered coding:

1. Hover over the **Copilot icon** in the Status Bar and select **Use AI Features**
2. Choose a sign-in method and follow the prompts
3. If you don't have a Copilot subscription, you'll be signed up for the [Copilot Free plan](https://github.com/github-copilot/signup) with a monthly limit of inline suggestions and chat interactions
4. Start using Copilot in VS Code!

Learn more about [GitHub Copilot plans](https://docs.github.com/en/copilot/get-started/plans).

### Step 5: Get Started with the VS Code Tutorial

Discover the user interface and key features of VS Code with the [Getting Started Tutorial](https://code.visualstudio.com/docs/getstarted/getting-started).

### Using GitHub Copilot

GitHub Copilot provides powerful AI capabilities directly in VS Code. Learn more in the [Copilot Overview](https://code.visualstudio.com/docs/copilot/overview).

#### Inline Suggestions

Copilot provides inline code suggestions as you type, from single line completions to entire function implementations:

- Type a function signature like `function calculateScore(` to get complete implementations
- Write comments like `// Create a particle system for visual effects` to generate code
- Begin a component with `const AnimatedCanvas = ({` to receive a complete implementation

Press `Tab` to accept suggestions or `Esc` to dismiss.

#### Natural Language Chat

Use natural language to interact with your codebase through the Chat view (`Ctrl+Shift+I` / `Cmd+Shift+I`):

- "How does this animation loop work?"
- "What's causing the rendering issue in the draw function?"
- "Add sound effects when the user clicks the canvas"
- "Create a color palette generator component"

Learn more about [using chat in VS Code](https://code.visualstudio.com/docs/copilot/chat/copilot-chat).

#### Autonomous Coding with Agents

Agents can autonomously plan and execute complex development tasks. In the Chat view, open the mode picker dropdown (next to the chat input box) and select **Agent**:

- "Implement a generative art canvas with multiple brush styles"
- "Create a music visualizer that responds to audio input"
- "Build a story generator with branching narrative paths"

The agent will iterate on the code, running commands and making coordinated changes across multiple files.

#### Inline Chat

For quick edits directly in the editor:

1. Select code and press `Ctrl+I` / `Cmd+I` to open inline chat
2. Ask Copilot to modify, refactor, or explain the selected code
3. Review and accept or reject proposed changes


<details>
<summary><strong>🎛️ Understanding GitHub Copilot Modes (click to expand)</strong></summary>

### Understanding GitHub Copilot Modes

GitHub Copilot offers distinct modes, each designed to enhance your coding workflow in unique ways. Understanding when to use each mode will help you get the most out of Copilot for your creative projects:

#### Ask Mode

Ask Mode is a Q&A assistant that helps you understand code, solve problems, or learn concepts. It allows you to ask questions in natural language, and Copilot responds with explanations, snippets, or suggestions. It does not directly modify any code.

> **Tip**: Ask mode works best for quick clarifications, brainstorming creative solutions, and getting sample implementations for your project ideas.

**Example prompts for creative apps:**
- "How can I create a particle system effect in p5.js?"
- "What's the best approach for generating procedural music?"
- "Explain how color theory applies to generative art"

#### Edit Mode

Edit Mode enables direct code modifications based on natural language instructions. You can highlight specific code blocks or files, describe the desired changes, and Copilot will propose edits. These changes are presented as diffs for your review, ensuring you retain control over the final implementation.

> **Tip**: Try Edit mode for targeted updates, such as refactoring animation code or adding error handling to your creative application.

**Example prompts for creative apps:**
- "Add easing functions to this animation"
- "Refactor this drawing code to support multiple brush types"
- "Add input validation to the user prompt handler"

#### Agent Mode

Agent Mode is the most autonomous and powerful of the modes. It allows Copilot to analyze your entire project, plan tasks, make edits, run commands, and iterate until the goal is achieved. This mode is ideal for multi-step tasks, such as building features, fixing bugs, or scaffolding new components.

> **Tip**: Agent mode will carry out actions beyond just editing—it can write code, create new files, and run terminal commands. Best used for complex creative features that span multiple files.

**Example prompts for creative apps:**
- "Create a complete music visualizer component with audio analysis"
- "Build a story generator with save/load functionality and branching paths"
- "Implement a generative art canvas with multiple brush styles and export options"

#### Plan Mode

Plan Mode helps you outline your coding tasks and objectives more effectively. Copilot assists in creating a structured plan for your project, helping you break down complex creative tasks into manageable steps.

> **Tip**: Use Plan Mode when starting a new creative project to set clear objectives and receive tailored suggestions for your implementation approach.

**Example prompts for creative apps:**
- "Plan the architecture for an interactive fiction engine"
- "Help me break down building a procedural music generator"
- "Create a roadmap for implementing a collaborative art platform"

</details>

### Getting Started Checklist

1. ✅ Download and install VS Code for your platform
2. ✅ Install additional components (Git, Node.js, language runtimes)
3. ✅ Enable AI features and sign in to GitHub Copilot
4. ✅ Explore Copilot Chat and inline chat features
5. ✅ Choose your creative project idea and target platform
6. ✅ Start building and let Copilot accelerate your development!

</details>

---

## ✨ Prompting Tips

Effective prompting is key to getting the most out of GitHub Copilot for creative development. Here are tips and techniques to improve your results:

<details>
<summary><strong>💬 Prompting Techniques & Templates (click to expand)</strong></summary>

### Use File References for Context

When working with GitHub Copilot Chat, use the `#file:filename` syntax to provide specific file context:

1. Type `#` in the Copilot chat window
2. A file picker will appear automatically
3. Select the file you want to reference
4. Then type or paste the rest of your prompt

**Example**: Instead of asking "add an animation function", ask "#file:canvas.js add a smooth easing animation function for the particle system"

### Be Specific About Creative Intent

Vague prompts lead to generic results. Include details about style, mood, and technical requirements:

| ❌ Vague Prompt | ✅ Specific Prompt |
|----------------|--------------------|
| "Generate some art" | "Create a generative art function that draws flowing curves using Perlin noise with a cool color palette" |
| "Make music" | "Generate a chord progression in C major with jazz voicings using Tone.js" |
| "Write a story" | "Create a branching narrative function that generates mystery story segments with 3 choices per scene" |

### Iterate Incrementally

For complex creative features, break your requests into smaller steps:

1. **Start with the foundation**: "Create a basic canvas setup with a render loop"
2. **Add core functionality**: "Add a particle class with position, velocity, and lifespan"
3. **Enhance with creativity**: "Make particles leave colorful trails that fade over time"
4. **Polish the experience**: "Add mouse interaction so particles are attracted to the cursor"

### Validate AI Suggestions

When Copilot generates creative code:

- **Test incrementally**: Run the code after each significant change to catch issues early
- **Trust but verify**: AI suggestions are starting points—review for correctness and style
- **Learn from output**: If a suggestion doesn't match your intent, refine your prompt with more context
- **Use Cheatsheets**: Keep reference documentation handy to validate generated code against known patterns

### Prompt Templates for Enterprise-Style Apps

Here are reusable prompt patterns for common business application workflows you can adapt to creative projects:

**For MCP Integrations:**
```
Create an MCP client that connects to [service/data source] and retrieves [data type]. 
Transform the data to [output format] and expose it via [interface type - CLI/API/UI].
```

**For CLI Tools:**
```
Build a CLI tool that [primary function] by [method/approach]. 
Include commands for [command list] with options for [configuration options].
Output results in [format - table/JSON/markdown].
```

**For Data Aggregation:**
```
Create a [tool type] that pulls data from [source 1] and [source 2], 
correlates them by [relationship/key], and generates [output type] 
highlighting [insights/metrics].
```

**For Workflow Automation:**
```
Implement an automation that monitors [trigger source] for [event type].
When triggered, [action 1], then [action 2], and notify via [channel].
Include error handling for [failure scenarios].
```

### Using Inline Chat Effectively

For quick edits directly in the editor (`Ctrl+I` / `Cmd+I`):

- Select the specific code you want to modify before opening inline chat
- Use follow-up prompts to refine without rewriting the whole request
- Ask for explanations of generated code to understand the approach

</details>

---

## 🤖 Available Models

GitHub Copilot supports a variety of AI models with varying capabilities. You can choose different models based on your needs:

- **GPT Models** - Strong general-purpose coding assistance
- **Claude Models** - Excellent for nuanced explanations and creative tasks  
- **Gemini Models** - Good for multimodal understanding

To learn more about GitHub Copilot's capabilities and plans, visit: [GitHub Copilot Plans](https://github.com/features/copilot/plans)

> **Note**: Model availability may vary based on your subscription plan. The techniques in this starter kit are model-agnostic and work across all supported models.

---

## 📋 Requirements & Evaluation

Your solution will be evaluated based on the following criteria. We're looking for projects that demonstrate both technical excellence and creative innovation:

### Core Requirements

#### 1. GitHub Copilot Usage (Required)

Your project **must** demonstrate meaningful use of **GitHub Copilot** during development. This includes:

- Using Copilot suggestions to accelerate code writing
- Leveraging Copilot Chat for problem-solving, debugging, or code explanation
- Documenting how Copilot assisted in your creative process

> **Bonus**: Consider building your project using the **Copilot CLI SDK** to create command-line interfaces that leverage Copilot's capabilities and integrate with MCP for powerful automation.

#### 2. Creative Application (Required)

Your submission **must** be a creative application that showcases innovation and imagination. The application should:

- Demonstrate a unique or novel concept
- Provide value, entertainment, or utility to users
- Show thoughtful design in user experience

#### 3. MCP Integration (Required)

Your project **must** integrate with the **Model Context Protocol (MCP)** in some form. This includes:

- Using an MCP server to connect with external data sources
- Demonstrating how MCP enables your application to access and combine information from multiple tools or services
- Documenting your MCP integration and the value it provides

### 🏆 Evaluation Criteria

Projects are evaluated using this rubric, which combines scores from expert judges, product teams, and a community vote:

- **Accuracy & Relevance (20%)** — Meets challenge requirements
- **Reasoning & Multi-step Thinking (20%)** — Clear problem-solving approach
- **Creativity & Originality (15%)** — Novel ideas or unexpected execution
- **User Experience & Presentation (15%)** — Clear, polished, demoable
- **Reliability & Safety (20%)** — Solid patterns, avoids obvious pitfalls
- **Community vote (10%)** via the Discord poll available at https://aka.ms/agentsleague/discord

---

## 📚 Resources

Explore the following resources to master GitHub Copilot and accelerate your creative development:

<details>
<summary><strong>📖 Documentation & Learning Resources (click to expand)</strong></summary>

### GitHub Copilot Documentation

Official documentation and guides for GitHub Copilot:

- **Getting Started with GitHub Copilot**: [https://docs.github.com/en/copilot/getting-started-with-github-copilot](https://docs.github.com/en/copilot/getting-started-with-github-copilot)
- **GitHub Copilot in VS Code**: [https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-your-ide](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-your-ide)
- **Copilot Chat Documentation**: [https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)
- **GitHub Copilot Plans**: [https://github.com/features/copilot/plans](https://github.com/features/copilot/plans)

### Learning Resources

Tutorials and courses to enhance your skills:

- **GitHub Copilot Fundamentals**: [https://learn.microsoft.com/training/modules/introduction-to-github-copilot/](https://learn.microsoft.com/training/modules/introduction-to-github-copilot/)
- **GitHub Skills - Code with Copilot**: [https://github.com/skills/copilot-codespaces-vscode](https://github.com/skills/copilot-codespaces-vscode)
- **VS Code Tips and Tricks**: [https://code.visualstudio.com/docs/getstarted/tips-and-tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

### Model Context Protocol (MCP) Resources

Get started with MCP for your projects:

- **MCP Overview**: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
- **MCP Quickstart Guide**: [https://modelcontextprotocol.io/quickstart](https://modelcontextprotocol.io/quickstart)
- **Building MCP Servers**: [https://modelcontextprotocol.io/docs/concepts/servers](https://modelcontextprotocol.io/docs/concepts/servers)
- **MCP in VS Code**: [https://code.visualstudio.com/docs/copilot/chat/mcp-servers](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

#### Useful MCP Servers

Here are some MCP servers to help you get started:

| Server | Description | Repository |
|--------|-------------|------------|
| **WorkIQ** | Connect to Microsoft 365 data (Teams, Outlook, SharePoint, Planner) | [microsoft/work-iq-mcp](https://github.com/microsoft/work-iq-mcp) |
| **Microsoft Learn** | Access Microsoft Learn documentation and training content | [MicrosoftDocs/mcp](https://github.com/MicrosoftDocs/mcp) |
| **GitHub** | Interact with GitHub repos, issues, PRs, and more | [github/github-mcp-server](https://github.com/github/github-mcp-server) |
| **Playwright** | Browser automation and web scraping capabilities | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |

</details>

---

Questions? Join the #creative-apps channel on [Discord](https://aka.ms/agentsleague/discord).