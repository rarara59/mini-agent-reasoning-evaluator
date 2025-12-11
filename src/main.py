import json
import sys
from pathlib import Path

from .parser import parse_reasoning
from .rule_evaluator import evaluate_steps
from .answer_checker import check_final_answer
from .aggregator import aggregate_failures
from .scorer import compute_scores
from .formatter import format_human
from .logger import log_evaluation
from .models import EvaluationResult


# Available tasks and their corresponding example files
TASKS = {
    "sort": ("tasks/task_sort_numbers.json", "examples/sample_agent_output_sort.txt"),
    "word": ("tasks/task_word_problem.json", "examples/sample_agent_output_word_problem.txt"),
    "constraints": ("tasks/task_constraints.json", "examples/sample_agent_output_constraints.txt"),
}


def load_task(task_path: str) -> dict:
    p = Path(task_path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_agent_output(path: str) -> str:
    p = Path(path)
    return p.read_text(encoding="utf-8")


def main() -> None:
    # Simple CLI: python -m src.main [task_name]
    # task_name can be: sort, word, constraints (default: sort)
    task_name = sys.argv[1] if len(sys.argv) > 1 else "sort"

    if task_name not in TASKS:
        print(f"Unknown task: {task_name}")
        print(f"Available tasks: {', '.join(TASKS.keys())}")
        sys.exit(1)

    task_path, example_path = TASKS[task_name]
    task = load_task(task_path)
    raw_reasoning = load_agent_output(example_path)

    steps = parse_reasoning(raw_reasoning)
    evaluated_steps = evaluate_steps(
        steps,
        task_description=task["prompt"],
        constraints=task.get("constraints", []),
    )

    # Check final answer using answer_checker
    final_answer_correct = check_final_answer(raw_reasoning, task["expected_answer"])

    reasoning_score, correctness_score, overall_score = compute_scores(
        evaluated_steps,
        final_answer_correct=final_answer_correct,
    )

    failure_summary = aggregate_failures(evaluated_steps, final_answer_correct)

    result = EvaluationResult(
        task_id=task["id"],
        reasoning_score=reasoning_score,
        correctness_score=correctness_score,
        overall_score=overall_score,
        evaluated_steps=evaluated_steps,
        final_answer_correct=final_answer_correct,
        failure_summary=failure_summary,
    )

    log_file = log_evaluation(result)

    print(format_human(result))
    print(f"Log written to: {log_file}")


if __name__ == "__main__":
    main()
