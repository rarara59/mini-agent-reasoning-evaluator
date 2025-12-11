import json
from .models import EvaluationResult


def format_human(result: EvaluationResult) -> str:
    """
    Convert an EvaluationResult into a human-readable string for console output.
    """
    lines = [
        "=" * 50,
        f"Task: {result.task_id}",
        "=" * 50,
        "",
        "Scores:",
        f"  Reasoning Score:   {result.reasoning_score:.1f}",
        f"  Correctness Score: {result.correctness_score:.1f}",
        f"  Overall Score:     {result.overall_score:.1f}",
        "",
        f"Final Answer Correct: {result.final_answer_correct}",
        "",
    ]

    # Add failure summary
    invalid_indices = result.failure_summary.get("invalid_step_indices", [])
    error_types = result.failure_summary.get("error_types", [])
    status = result.failure_summary.get("status", "unknown")

    lines.append(f"Status: {status}")
    lines.append("")

    if invalid_indices:
        lines.append(f"Invalid Steps: {invalid_indices}")
        if error_types:
            lines.append("Sample Errors:")
            for error in error_types[:2]:  # Show up to 2 sample errors
                lines.append(f"  - {error}")
    else:
        lines.append("All reasoning steps valid.")

    lines.append("")
    lines.append("=" * 50)

    return "\n".join(lines)


def format_json(result: EvaluationResult, indent: int = 2) -> str:
    """
    Convert an EvaluationResult into a pretty JSON string for debugging.
    """
    payload = {
        "task_id": result.task_id,
        "reasoning_score": result.reasoning_score,
        "correctness_score": result.correctness_score,
        "overall_score": result.overall_score,
        "final_answer_correct": result.final_answer_correct,
        "failure_summary": result.failure_summary,
        "evaluated_steps": [
            {
                "index": e.step.index,
                "text": e.step.text,
                "valid": e.valid,
                "errors": e.errors,
            }
            for e in result.evaluated_steps
        ],
    }
    return json.dumps(payload, indent=indent)
