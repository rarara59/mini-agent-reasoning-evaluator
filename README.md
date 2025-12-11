# mini-agent-reasoning-evaluator

This project is a small prototype that evaluates how an agent reasons through a task — not just whether it arrives at the right answer.

The central idea is borrowed from legal reasoning:
a conclusion is only as strong as the chain of logic that supports it.

Just as a court evaluates an argument by examining each claim and sub-claim for relevance, consistency, and adherence to constraints, this tool examines an agent's reasoning step-by-step.

Instead of assuming that a "good-sounding" answer reflects good reasoning, the evaluator:
- parses the agent's step-by-step logic
- treats each step like a claim in an argument
- tests steps for relevance, continuity, and constraint adherence
- checks for contradictions
- evaluates the final answer
- generates a reasoning score, correctness score, and an overall assessment
- logs each evaluation as structured JSON for comparison

This is a minimal demonstration of how one might begin to test whether an agent's reasoning chain is sound — not just whether the agent "got the answer right."

It aligns with Imbue's focus on developing agents that reason deliberately, verify their own steps, and behave predictably.

---

## How it works

1. A task definition (e.g., "Sort these numbers") is loaded from `tasks/`.
2. A sample agent reasoning trace is loaded from `examples/`.
3. The evaluator parses reasoning into discrete steps — analogous to breaking an argument into claims.
4. Each step is evaluated with simple rules:
   - **Relevance** (Is this step actually advancing the solution?)
   - **Continuity** (Does it follow logically from the previous step?)
   - **Constraint adherence** (Does it violate instructions?)
   - **Contradiction detection**
5. The final answer is checked against the expected output.
6. The system computes:
   - reasoning score
   - correctness score
   - overall score
7. The full evaluation is logged in JSON under `logs/`.

---

## Usage

```bash
pip install -r requirements.txt
python -m src.main
```

---

## Why this exists

Current LLMs often generate answers that sound right without demonstrating actual reasoning.
This prototype focuses on the structure of reasoning itself — examining the logic between input and output.

It serves as a conceptual and technical demonstration of how one might evaluate an agent's reasoning process using simple, interpretable rules.
