# Product Requirements Document
## Mini-Agent Reasoning Evaluator
### Author: Rafal Tracz
### Purpose: Demonstrate a structured, cognition-aware approach to evaluating reasoning

---

# 1. Overview

Humans do not reach conclusions by guessing what "sounds right."
We reason the way attorneys structure arguments:

- step by step
- with each claim supported by the one before it
- contradictions flagged
- constraints respected
- conclusions valid only if the reasoning chain holds

Today's LLMs often skip this discipline. They produce convincing text that resembles logic without the accountability of an actual reasoning chain. Imbue's north star is to build agents whose internal logic can be examined, tested, and trusted.

This prototype implements a small-scale evaluator that treats an agent's reasoning like a legal argument. Instead of grading only the outcome, it evaluates the *structure* of the reasoning itself.

---

# 2. Goals

## 2.1 Functional Goals

1. Accept a task definition.
2. Accept an agent's reasoning output.
3. Parse reasoning into discrete steps.
4. Evaluate each step with simple logic rules.
5. Detect reasoning failures (irrelevance, discontinuity, constraint violations).
6. Check the correctness of the final answer.
7. Compute reasoning and correctness scores.
8. Log results as structured JSON.

## 2.2 Non-Functional Goals

- Clarity
- Simplicity
- Determinism
- Extensibility
- Modular design

This is intentionally minimal and cognition-focused.

---

# 3. Non-Goals

This project will **not**:

- attempt to train a model
- produce production-grade evaluation tools
- evaluate deep reasoning or complex logic
- generalize across reasoning domains

It is a conceptual demonstration — not a full system.

---

# 4. User Stories

- **Engineer:** I need to inspect the chain of reasoning to understand where an agent's logic breaks.
- **Researcher:** I need structured failure modes for categorizing reasoning errors.
- **Product thinker:** I need a simple, interpretable scoring method.
- **Reviewer:** I need a human-readable summary explaining reasoning failures.

---

# 5. System Architecture

Reasoning evaluation is modeled on legal argument review:

```
Task (case)
→ Agent Reasoning (argument)
→ Step Parser (issue spotting)
→ Rule Evaluator (applying standards)
→ Final Answer Checker (holding)
→ Error Aggregator (opinion)
→ Scoring Engine (strength of argument)
→ Output Formatter (decision)
→ Logger (record)
```

Each component mirrors how structured human reasoning is reviewed for validity.

---

# 6. Component Requirements

## 6.1 Step Parser
Break the reasoning into claims (steps).
Preserve order. Normalize text.

## 6.2 Rule-Based Evaluator

Rules:

- **Relevance:** Is this step connected to the issue?
- **Continuity:** Does it follow from the prior step?
- **Constraint adherence:** Does it respect the instructions?
- **Contradiction detection:** Does it conflict with earlier claims?

Output: `EvaluatedStep` objects containing validity and errors.

## 6.3 Final Answer Checker
Does the conclusion follow from the task requirements?
Simple comparison for now.

## 6.4 Error Aggregator
Summarize:

- invalid step indices
- error types
- contradiction points

## 6.5 Scoring Engine

```
reasoning_score = (# valid steps / total steps) * 100
correctness_score = 100 if final answer correct, else 0
overall_score = 0.7 * reasoning_score + 0.3 * correctness_score
```

## 6.6 Output Formatter
Produces:

- JSON for machines
- a human-readable explanation for reviewers

## 6.7 Logger
Save structured logs with:

- steps
- evaluations
- scores
- failure modes
- timestamps

---

# 7. Example Tasks

- Sorting task
- Arithmetic word problem
- Constraint-following task
- Simple code behavior task

---

# 8. Risks & Mitigations

- **LLM formatting variance:** mitigate with flexible parsing.
- **Oversimplified rules:** document extensibility.
- **Overengineering risk:** intentionally minimal scope.

---

# 9. Success Criteria

- Clear, interpretable reasoning evaluation
- Step-level analysis, not only final-answer checking
- Modular, extensible design
- Structured logs for comparison
- Demonstrates understanding of how to evaluate reasoning — not just how to generate it
