# Research Methodologies

This document outlines approaches for planning and executing research tasks.

## 1. Planning the Research

*   **Understand the Goal:** What specific question(s) need answering? What is the desired output format (e.g., summary, comparison, list of options)? Who is the audience?
*   **Define Key Questions:** Break down the main topic into specific, answerable questions.
*   **Identify Potential Sources:** Brainstorm where the information might be found:
    *   **Internal:** Project documentation (`.docs/`, `.tasks/`, `.decisions/`, `.planning/`), existing code (`src/`), team knowledge (via user interaction).
    *   **External:** Official documentation for technologies, reputable technical blogs/articles, academic papers (if applicable), specific forums (Stack Overflow), competitor analysis.
*   **Prioritize Sources:** Rank potential sources based on likely relevance and authority (e.g., official docs > blog post > forum comment).
*   **Log the Strategy:** Record the key questions and planned sources in the task log.

## 2. Gathering Information

*   **Execute Systematically:** Work through the prioritized source list.
*   **Use Appropriate Tools:**
    *   `read_file`: For local project documents.
    *   `browser`: For web searches (use targeted keywords) and accessing specific URLs.
    *   `use_mcp_tool`: If specialized tools like `firecrawl-specialist` or `crawl4ai-specialist` are available and appropriate for large-scale web data gathering.
*   **Evaluate Sources:** Assess credibility: Is it official documentation? Is the author reputable? Is the information up-to-date? Are claims supported by evidence? Be wary of outdated or biased information.
*   **Extract Key Information:** Focus on data directly answering the research questions. Copy relevant snippets, quotes, code examples, or data points.
*   **Log Findings & Sources:** For each significant piece of information gathered, record it in the task log along with its source (URL, file path, page title). This is crucial for synthesis and citation.

## 3. Synthesizing Findings

*   **Review Gathered Data:** Read through the logged findings and raw data.
*   **Group & Theme:** Organize information based on the initial research questions or emerging themes. Identify patterns, contradictions, and key takeaways.
*   **Structure the Summary:** Plan the structure of the final report (e.g., using the `report-template.md`).
*   **Draft the Summary:** Write concise sections, starting with an executive summary. Use clear language. Integrate findings logically.
*   **Incorporate Examples:** Include relevant code snippets or data examples where appropriate, keeping them brief and illustrative.
*   **Cite Sources:** Ensure every key finding or piece of data is attributed to its source using the agreed `citation-formats.md`. Create a final reference list.
*   **Review and Refine:** Check for accuracy, clarity, conciseness, and completeness based on the original query. Ensure all questions are addressed.

*(Adapt these methodologies based on the specific research task.)*