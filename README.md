# Mini-Agent Reasoning Evaluator

This project is a small prototype that evaluates how an agent *reasons* through a task — not just whether it arrives at the right answer.

The central idea is borrowed from legal reasoning:
**a conclusion is only as strong as the chain of logic that supports it.**

Just as a court examines an argument by evaluating each claim for relevance, continuity, constraint adherence, and internal consistency, this tool examines an agent's reasoning step-by-step.

Instead of assuming that a confident answer reflects sound logic, the evaluator:

- parses the agent's reasoning into discrete steps
- treats each step like a claim in a legal argument
- tests those steps against simple, interpretable rules
- checks the final answer for correctness
- computes reasoning and correctness scores
- logs each evaluation run as structured JSON

This prototype does not attempt to solve reasoning in the general case.
It simply demonstrates how one might begin to evaluate *whether* an agent's reasoning chain is valid, coherent, and grounded — the core of Imbue's mission to develop agents that truly reason.

---

## How it works

1. A task definition (e.g., "Sort these numbers") is loaded from `tasks/`.
2. A reasoning trace is loaded from `examples/`.
3. The evaluator breaks the reasoning into discrete steps.
4. Each step is evaluated with simple rules:
   - **Relevance** (Does this step actually relate to the task?)
   - **Continuity** (Does it plausibly follow from the prior step?)
   - **Constraint adherence** (Does it violate the instructions?)
   - **Contradiction detection** (Does it contradict earlier steps?)
5. The final answer is checked against the expected output.
6. Scores are computed for reasoning, correctness, and overall quality.
7. The run is logged as structured JSON in `logs/`.

This creates a small, inspectable evaluation pipeline that mirrors — in miniature — the kinds of reasoning-verification systems required for safer and more reliable agents.

---

## Usage

```bash
pip install -r requirements.txt
python -m src.main
```

The output includes:
- a reasoning score
- a correctness score
- an aggregated explanation of step-level issues
- a JSON file with the full evaluation record

---

## What this project demonstrates

- A concrete way to evaluate an agent's reasoning process, not only its final answer.
- How simple, interpretable rules can surface failure modes in step-by-step logic.
- An approach to treating agent reasoning like a legal argument: breaking it into claims and evaluating continuity, relevance, and constraint adherence.
- A working implementation that can be extended with richer rules, benchmarks, and LLM-assisted grading.
- A minimal but principled foundation for agent evaluation — aligned with Imbue's mission to build agents whose reasoning can be inspected, tested, and improved.
