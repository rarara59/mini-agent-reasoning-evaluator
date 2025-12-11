# Mini Agent Reasoning Evaluator

This is a small project that tries to answer a simple question:

**Did the agent actually reason well or did it just get lucky?**

Most agent evaluations focus on the final answer. That's useful, but it misses a lot. An agent can arrive at the "right" result while making bad assumptions, skipping steps, or contradicting itself along the way.

This project looks at the reasoning process itself, step by step.

---

## Why I Built This

When you look closely at agent behavior, a correct answer often isn't enough to tell you whether the reasoning was sound.

Some common failure modes:
- The agent introduces an assumption that was never justified
- The agent contradicts an earlier step
- The agent skips over a required constraint
- The reasoning degrades halfway through, but the final answer still looks fine

In most systems, those failures go unnoticed because the output appears correct.

This project treats that as a problem.

**If the reasoning is flawed, the outcome shouldn't get a free pass.**

---

## What This Project Does

At a high level, the evaluator works like this:
1. Take an agent's reasoning trace
2. Break it into individual steps
3. Evaluate each step on basic reasoning standards
4. Aggregate those results into a clear, inspectable score

The goal is not to judge writing style or fluency.
It's to surface logical quality and consistency.

---

## What Gets Evaluated

Each reasoning step is checked for things like:

- **Relevance**
  Does this step actually move the reasoning forward?
- **Continuity**
  Does it logically follow from the previous step?
- **Constraint adherence**
  Is the agent respecting the rules of the task?
- **Contradictions or regressions**
  Does the agent undo or conflict with earlier reasoning?

All of this is done using explicit, rule-based checks. Nothing is hidden.

---

## Example

### Input: Reasoning Trace

```
1. Restate the user's question.
2. Identify relevant information.
3. Introduce an assumption that isn't supported.
4. Use that assumption to reach a conclusion.
```

### Output: Evaluation (Illustrative)

```json
{
  "step_scores": [
    { "step": 1, "relevance": 1.0, "continuity": 1.0 },
    { "step": 2, "relevance": 1.0, "continuity": 1.0 },
    { "step": 3, "relevance": 0.3, "continuity": 0.5, "flags": ["unsupported_assumption"] },
    { "step": 4, "relevance": 0.6, "continuity": 0.4, "flags": ["depends_on_flagged_step"] }
  ],
  "aggregate_score": 0.66,
  "notes": [
    "Reasoning quality drops after an unsupported assumption is introduced."
  ]
}
```

A key point here:

**A correct conclusion reached through flawed reasoning is treated as a failure, not a success.**

---

## Design Principles

A few rules I stuck to while building this:

- **Explainability over cleverness**
  If a score can't be explained, it doesn't belong.
- **Process over outcome**
  The reasoning matters more than the final answer.
- **Minimal surface area**
  This is intentionally small. The point is the evaluation logic, not scale.
- **Readable outputs**
  You should be able to look at the result and understand why a score was given.

---

## What This Is Not

Just to be clear, this is not:
- A benchmark suite
- A production-ready evaluator
- An agent framework
- An LLM-based grader

It's a small, focused prototype for reasoning evaluation.

---

## Where This Could Go

This project is intentionally limited, but it could be extended in a few directions:
- Layering LLM-assisted grading on top of rule-based checks
- Expanding the rule set for specific domains
- Comparing reasoning quality across multiple agent runs
- Visualizing where and how reasoning breaks down

Those are directions, not promises.

---

## Why This Exists

I'm interested in agent evaluation, tooling, and reasoning systems, especially cases where understanding *how* an agent failed matters as much as *that* it failed.

This project is meant to be:
- easy to read
- easy to reason about
- easy to extend

Nothing more than that.
