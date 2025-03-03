# Lesson 22: Decentralized AI Agents

In this lesson, we will explore how to build AI agents using open-source tools and leverage Large Language Models (LLMs) to power the reasoning process behind agent task execution.

We will also examine how AI Agents can be integrated into Retrieval-Augmented Generation (RAG) pipelines to automate decision-making about information retrieval from various indexes and its application to the generation task at hand.

By the end of this lesson, we will begin our introduction to the subject of decentralized AI agents by leveraging a set of dev tooling for connecting our agents to Web3 wallets.

## Prerequisites

- Proficiency in using a shell/terminal/console/bash on your device
  - Familiarity with basic commands like `cd`, `ls`, and `mkdir`
  - Ability to execute packages, scripts, and commands on your device
- Installation of Python tools on your device
  - [Python](https://www.python.org/downloads/)
  - [Pip](https://pip.pypa.io/en/stable/installation/)
- Proficiency in using `python` and `pip` commands
  - Documentation: [Python](https://docs.python.org/3/)
  - Documentation: [Pip](https://pip.pypa.io/en/stable/)
- Proficiency in using `venv` to create and manage virtual environments
  - Documentation: [Python venv](https://docs.python.org/3/library/venv.html)
- Installation of Node.js on your device
  - [Node.js](https://nodejs.org/en/download/)
- Proficiency in using `npm` and `npx` commands
  - Documentation: [npm](https://docs.npmjs.com/)
  - Documentation: [npx](https://www.npmjs.com/package/npx)
- Proficiency in using `npm install` and managing the `node_modules` folder
  - Documentation: [npm install](https://docs.npmjs.com/cli/v10/commands/npm-install)
- Installation of `git` CLI on your device
  - [Git](https://git-scm.com/downloads)
- Proficiency in using `git` commands to clone repositories
  - Documentation: [Git](https://git-scm.com/doc)
- Create a free account on [LlamaCloud](https://cloud.llamaindex.ai/) and create an [API key](https://cloud.llamaindex.ai/api-key)

## Review of Lesson 21

- AI Agents
- Task planning
- Goals
- Types of agents
- Applications and examples
- Setting up an AI agent

## Building a Simple AI Agent Program

- Defining tools
- Using a Query Engine for processing tasks
- Implementing Query Transformations
- Task planning
- Handling steps
- Evaluating goals

- Practical exercises
  - Exercise 1: Implementing a [Simple AI Agent](./exercises/00-Simple-AI-Agent-With-LlamaIndex.md) using the [Agent Tools](https://docs.llamaindex.ai/en/stable/use_cases/agents/) from [LlamaIndex](https://llamaindex.ai)
  - Exercise 2: Implementing a [Structured Planning AI Agent](./exercises/01-Structured-Planning-AI-Agent.md) using the [Structured Planner](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/)

## Agentic RAG

- Retrieval Agents
  - File search functions
  - Web search functions
  - Chunking data
  - Embeddings
  - Vector search
- Integrating Query Engines into Agent tasks
- Multi-tool invocation
- Implementing Query Transformations
  - Decision-making for information retrieval
- Multi-step queries

- Practical exercise:
  - Exercise 3: Implementing an [Agentic RAG](./exercises/02-Agentic-RAG.md) AI using the [Query Engine Tool](https://docs.llamaindex.ai/en/stable/understanding/agent/rag_agent/) for passing documents to the agent

## Monetizing AI Agents with Tokens

AI Agents can be designed to handle monetary transactions using digital tokens, which are often implemented on blockchain networks. This capability opens up new possibilities for creating autonomous economic systems to incentivize AI-driven services.

### Introduction to Tokenization

- Definition of tokens in the context of blockchain and cryptocurrency
- Types of tokens:
  - Utility tokens
  - Security tokens
  - Governance tokens
  - Non-fungible tokens (NFTs)
- Benefits of using tokens for AI Agent transactions:
  - Programmable money
  - Transparency and auditability
  - Global accessibility
  - Fractional ownership

## Decentralized AI Agents tools

- Building AI Agents with token enabled functions
- Managing wallets and transactions
- Building smart contracts
- Deploying decentralized AI Agents

### Popular Web3 Agent Frameworks and Tools

- **ElizaOS** [Documentation](https://elizaos.github.io/eliza/docs/intro/):
  - Open-source TypeScript framework for building autonomous AI agents
  - Built-in Web3 capabilities through plugins
  - Supports multi-agent architectures and cross-platform interactions

- **Coinbase AgentKit** [Documentation](https://github.com/coinbase/agentkit):
  - Framework for building crypto-native AI agents
  - Native integration with [Coinbase products](https://www.coinbase.com/products)

- **Fleek** [Documentation](https://fleek.xyz/):
  - Web3 native platform for building and deploying AI agents
    - Hosting secure agents in [TEEs](https://fleek.xyz/guides/understanding-tees-and-sgx-fleek/)

## Next Steps

- Building Blockchain-Enabled Autonomous AI Agents
- Developing AI Agents with Tokenized Incentive Structures
- Implementing custom function calling capabilities to AI agents
- Deploying Onchain AI Agents on decentralized hosting providers
