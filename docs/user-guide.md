# User Guide: Ultimate Agentic Coding Tool

This guide explains how to use the Ultimate Agentic Coding Tool for your daily development tasks, covering its core features and common workflows.

## Table of Contents
1.  [Understanding the Interface (Roo Commander)](#1-understanding-the-interface-roo-commander)
2.  [Core Features and Usage](#2-core-features-and-usage)
    1.  [Proactive Orchestration Engine (POE)](#21-proactive-orchestration-engine-poe)
    2.  [Continuous Learning System (CLS)](#22-continuous-learning-system-cls)
    3.  [Agentic RAG Engine](#23-agentic-rag-engine)
    4.  [Ultimate Agentic Orchestrator](#24-ultimate-agentic-orchestrator)
3.  [Common Workflows and Usage Patterns](#3-common-workflows-and-usage-patterns)
    1.  [Starting a New Task or Feature](#31-starting-a-new-task-or-feature)
    2.  [Investigating an Issue or Bug](#32-investigating-an-issue-or-bug)
    3.  [Understanding Project Architecture or Decisions](#33-understanding-project-architecture-or-decisions)
4.  [Interacting with Autonomous Actions](#4-interacting-with-autonomous-actions)
5.  [Getting Help](#5-getting-help)

## 1. Understanding the Interface (Roo Commander)

The Ultimate Agentic Coding Tool primarily interacts with you through the **Roo Commander** interface. Roo Commander is now enhanced with the new AI engines, providing more intelligent and proactive assistance.

*   **Autonomous Operation:** Remember, the system is designed for autonomous operation (Rule [`23-autonomous-execution-mandate.md`](../../../.roo/rules/23-autonomous-execution-mandate.md)). It will often take initiative, make decisions, and execute tasks without explicit step-by-step prompting if it has high confidence.
*   **Responses:** Expect responses from Roo Commander to be more comprehensive. They will often include:
    *   The direct answer or result of your query/command.
    *   Proactive suggestions for next steps, potential improvements, or risk warnings.
    *   Insights derived from its continuous learning capabilities.

## 2. Core Features and Usage

### 2.1. Proactive Orchestration Engine (POE)

The POE works in the background to analyze your project and provide intelligent suggestions.

*   **How it Works:** The POE continuously monitors your project's state by accessing information stored in ConPort (tasks, decisions, code patterns, etc.). It uses this context to identify potential risks (e.g., overdue tasks, unlinked decisions) and opportunities (e.g., applying a relevant system pattern, optimizing a piece of code).
*   **Receiving Suggestions:** POE suggestions will typically be presented to you by Roo Commander as part of its responses or as standalone notifications if a critical issue or high-value opportunity is detected.
*   **Interacting with Suggestions:**
    *   Since the system operates autonomously, high-confidence suggestions might be acted upon automatically.
    *   For other suggestions, Roo Commander might briefly inform you of the intended action.
    *   Your feedback on these actions (implicit or explicit) feeds into the Continuous Learning System.
*   **Configuration:** POE's behavior (e.g., sensitivity of suggestions) is generally managed by system administrators or through advanced configuration files, not typically by end-users directly.

### 2.2. Continuous Learning System (CLS)

The CLS enables the tool to learn and improve over time.

*   **Feedback Collection:**
    *   **Implicit Feedback:** The system observes your interactions. For example, if you frequently undo an agent's code change, it's taken as negative feedback. If you accept suggestions, it's positive.
    *   **Explicit Feedback (If Applicable):** In some scenarios, Roo Commander might present a way to give explicit ratings or comments. This data is invaluable.
    *   **Agent-Observed Feedback:** Other agents or system components can log feedback about performance.
*   **Performance Analysis:** The CLS analyzes collected feedback and system metrics (e.g., task completion rates, error frequencies) to understand how well different agents and the overall system are performing.
*   **Self-Optimization:** Based on the analysis, the CLS generates "Refinement Proposals." These are suggestions for improving the system itself, such as:
    *   Modifying agent rules or KBs.
    *   Adjusting prompt templates.
    *   Improving error handling.
    *   High-priority, high-confidence refinements might be implemented autonomously.
*   **Your Role:** Your natural interaction with the system (accepting/rejecting suggestions, correcting code, the success/failure of tasks) is the primary way you contribute to the CLS.

### 2.3. Agentic RAG Engine

This engine provides Roo Commander with powerful information retrieval and understanding capabilities.

*   **How it Works:** When you ask a question or the system needs information, the Agentic RAG Engine:
    1.  **Analyzes and Decomposes Queries:** Complex questions are broken down into smaller, manageable sub-queries.
    2.  **Strategic Retrieval:** It uses various strategies (semantic search, keyword search, graph traversal of ConPort data) to find the most relevant information.
    3.  **Iterative Refinement:** If the initial information is insufficient, it can iteratively refine its search or ask clarifying (internal) questions to find better data.
    4.  **Information Synthesis:** It synthesizes the retrieved information into a coherent answer or understanding.
    5.  **Confidence Assessment:** It assesses its confidence in the retrieved information and the synthesized answer.
*   **Usage:** You use it by simply interacting with Roo Commander. When you ask questions like:
    *   "What was the rationale behind the latest ADR for user authentication?"
    *   "Show me examples of how we've implemented payment processing."
    *   "Analyze the performance implications of this code change."
    ...the Agentic RAG engine is working to provide you with accurate, context-rich answers.

### 2.4. Ultimate Agentic Orchestrator

This is the central "brain" that integrates the POE, CLS, and Agentic RAG Engine.

*   **Unified Coordination:** It ensures all components work together. For example, a RAG query might trigger a POE suggestion if the retrieved context reveals a risk. CLS feedback might refine how the RAG engine selects retrieval strategies.
*   **Response Synthesis:** It takes outputs from all engines to formulate the comprehensive responses you receive from Roo Commander.
*   **Performance Monitoring & Optimization:** It oversees overall system performance and can trigger optimization cycles.

## 3. Common Workflows and Usage Patterns

### 3.1. Starting a New Task or Feature

1.  **Describe Your Goal:** Clearly state your objective to Roo Commander.
    *   Example: "Implement a new feature for user profile editing."
2.  **Receive Initial Plan/Suggestions:** Roo Commander, using its agentic capabilities, will likely:
    *   Break down the task (possibly creating an MDTM task).
    *   Retrieve relevant context (existing code, ADRs, similar features).
    *   Offer initial suggestions or a plan of action.
    *   Potentially start implementing foundational parts autonomously.
3.  **Iterative Development:**
    *   Roo Commander will proceed with implementation, leveraging its engines for coding assistance, information retrieval, and proactive checks.
    *   It will log its progress, decisions, and any issues encountered in ConPort.
    *   You can query its progress or ask for specific help at any point.

### 3.2. Investigating an Issue or Bug

1.  **Report the Issue:** Describe the bug or issue to Roo Commander. Provide as much context as possible (error messages, steps to reproduce).
    *   Example: "Users are reporting an error when trying to reset their password. The error message is 'Token expired'."
2.  **Agentic Analysis:** Roo Commander will use the Agentic RAG engine to:
    *   Search ConPort for similar issues, relevant code sections, and ADRs.
    *   Analyze logs (if accessible and relevant).
3.  **Solution Proposal & Execution:**
    *   It will propose a solution or a diagnostic plan.
    *   With high confidence, it may attempt to implement a fix autonomously.
    *   The POE might offer suggestions to prevent similar issues in the future.

### 3.3. Understanding Project Architecture or Decisions

1.  **Ask Specific Questions:**
    *   Example: "What are the security considerations for our current API authentication?"
    *   Example: "Why did we choose microservices for the new billing module?"
2.  **RAG-Powered Answers:** The Agentic RAG engine will query ConPort (decisions, ADRs, documentation) to provide detailed answers, citing sources where possible.

## 4. Interacting with Autonomous Actions

*   **Observation:** Pay attention to the actions Roo Commander takes. It will typically log its significant actions.
*   **Guidance (Implicit):** If the system takes an undesirable autonomous action, your corrective actions (e.g., undoing a change, providing a new instruction) serve as feedback to the CLS.
*   **Trust but Verify (Initially):** While the system aims for high accuracy, especially in early stages of use, it's good practice to review significant autonomous changes until you build confidence in its decision-making for your specific project context.

## 5. Getting Help

*   **Ask Roo Commander:** Your primary point of interaction is Roo Commander. If you're unsure how to proceed or need information, ask it directly.
*   **Consult This Documentation:** Refer to the different sections of this documentation suite for detailed information.

By understanding these core features and workflows, you can effectively leverage the power of the Ultimate Agentic Coding Tool to streamline your development process and build better software.