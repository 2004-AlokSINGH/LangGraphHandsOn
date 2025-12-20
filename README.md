# LangGraph Learning Repository

This repository is created to **learn, experiment, and understand core concepts of LangChain and LangGraph**, and how they are used to build **structured, reliable, and scalable LLM applications**.

The focus is on **hands-on learning**, clear examples, and understanding **why** these frameworks are used in real-world systems.

---

## 📌 What is LangChain?

**LangChain** is a framework that helps you build applications powered by Large Language Models (LLMs).

It provides abstractions for:
- Prompt management
- LLM wrappers (OpenAI, Groq, HuggingFace, etc.)
- Chains (sequential logic)
- Memory (conversation state)
- Tools & agents
- Document loading and retrieval (RAG)

### Why use LangChain?
- Simplifies LLM integration
- Makes prompt + logic reusable
- Helps structure complex LLM workflows
- Widely used in industry for RAG, agents, and AI pipelines

---

## 📌 What is LangGraph?

**LangGraph** is an extension built on top of LangChain that allows you to create **stateful, graph-based workflows** for LLM applications.

Instead of linear chains, LangGraph lets you define:
- Nodes (LLM calls, tools, logic)
- Edges (flow control)
- State (shared data across steps)
- Loops, branching, and conditional paths

### In simple terms:
> **LangChain = Linear flow**  
> **LangGraph = Controlled, stateful, graph-based flow**

---

## 🔍 Why LangGraph When We Already Have LangChain?

LangChain is great for **simple and linear flows**, but it becomes hard to manage when:

- Multiple decision points exist
- You need retries or loops
- You want explicit control over execution
- State must persist across steps
- Agent logic becomes complex

LangGraph solves these problems by:
- Making flow **explicit and deterministic**
- Supporting **branching, cycles, and retries**
- Handling **state cleanly**
- Improving **debuggability and reliability**

---

## 🧠 When to Use What?

| Use Case | Recommended |
|--------|------------|
| Simple prompt → response | LangChain |
| Sequential steps | LangChain |
| RAG pipelines | LangChain |
| Agent with tools & decisions | LangGraph |
| Multi-step workflows with state | LangGraph |
| Production-grade AI flows | LangGraph |

---

## 🏗️ What This Repository Contains

This repository includes:
- Core LangChain concepts (LLMs, prompts, chains)
- LangGraph basics (nodes, edges, state)
- Simple examples to understand flow control
- Learning-focused code, not production boilerplate
- Experiments with different models (Groq, HuggingFace, etc.)

The goal is **conceptual clarity first**, optimization later.

---

## 🎯 Learning Objectives

By going through this repo, you should be able to:
- Understand why LangChain exists
- Know the limitations of linear chains
- Explain what LangGraph solves
- Build a simple graph-based LLM workflow
- Reason about stateful AI systems

---

## 🚀 Future Scope

Planned additions:
- RAG with LangGraph
- Tool-using agents
- Error handling & retries
- Comparison: Chain vs Graph
- Production patterns

---

## 📝 Note

This repository is for **learning and experimentation**.  
Code is intentionally kept **simple and readable** to focus on understanding concepts.

---

## ⭐ If You Find This Useful

Feel free to star the repository and use it as a reference while learning LangChain & LangGraph.
