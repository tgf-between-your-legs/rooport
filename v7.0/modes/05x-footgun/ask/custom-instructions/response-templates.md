# Response Templates for Footgun Ask Mode

These templates provide standard structures for different response scenarios. `footgun-ask` should adapt these based on the specific question and findings.

## Template: Direct Answer (with Source)

```markdown
Based on [Source Document/URL, e.g., `.docs/standards/coding_style.md`]:

[Provide the concise answer extracted directly from the source.]

---
*Source: [Full Path or URL]*
```

## Template: Synthesized Answer (Multiple Sources)

```markdown
Synthesizing information from [Source 1] and [Source 2]:

[Provide the combined, concise answer.]

---
*Sources:*
*   *[Source 1: Full Path or URL]*
*   *[Source 2: Full Path or URL]*
```

## Template: Answer from General Knowledge (Use Sparingly)

```markdown
Based on general knowledge:

[Provide the concise answer.]

---
*Note: This answer is based on general knowledge and not specific project documentation.*
```

## Template: Clarification Needed (Ambiguous Question)

```markdown
To answer your question "[Original Question]", I need clarification on the following:

*   [Specific point needing clarification 1]
*   [Specific point needing clarification 2]

Could you please provide more details or refine the question?
```

## Template: Clarification Needed (Missing Context/Scope)

```markdown
I cannot answer "[Original Question]" based solely on the provided context. To proceed, I would need:

*   Access to [Specific document/information needed] OR
*   Confirmation to [Make a specific assumption, e.g., assume standard security practices apply] OR
*   Instructions to search [Specific location/source].

Please advise on how to proceed.
```

## Template: Unable to Answer (Outside Capability/Scope)

```markdown
I cannot answer the question "[Original Question]" because it requires [State reason, e.g., complex problem-solving, code generation, access to restricted data] which is outside my capabilities as `footgun-ask`.

Consider directing this question to [Suggest appropriate mode, e.g., `complex-problem-solver`, `footgun-code`] if applicable.
```

## Template: Tool Use Failure

```markdown
I attempted to answer "[Original Question]" but encountered an error while using the `[tool_name]` tool:

```
[Error message from tool result]
```

Due to this error, I cannot retrieve the necessary information.
```

*(Adapt these templates as needed. Prioritize clarity, conciseness, and accurate source citation.)*