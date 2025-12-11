from typing import List, Dict, Any
from .models import EvaluatedStep


def aggregate_failures(
    evaluated_steps: List[EvaluatedStep],
    final_answer_correct: bool,
) -> Dict[str, Any]:
    """
    Summarize failures from the evaluation.

    Args:
        evaluated_steps: List of evaluated steps from rule_evaluator.
        final_answer_correct: Whether the final answer was correct.

    Returns:
        Dictionary containing:
        - invalid_step_indices: List of step indices that failed validation
        - error_types: List of unique error messages across all steps
        - status: High-level label ("all_valid", "some_invalid", "incorrect_answer", "all_invalid")
    """
    invalid_step_indices: List[int] = []
    error_set: set = set()

    for evaluated_step in evaluated_steps:
        if not evaluated_step.valid:
            invalid_step_indices.append(evaluated_step.step.index)
            for error in evaluated_step.errors:
                error_set.add(error)

    # Determine high-level status
    total_steps = len(evaluated_steps)
    invalid_count = len(invalid_step_indices)

    if invalid_count == 0 and final_answer_correct:
        status = "all_valid"
    elif invalid_count == total_steps:
        status = "all_invalid"
    elif invalid_count > 0:
        status = "some_invalid"
    elif not final_answer_correct:
        status = "incorrect_answer"
    else:
        status = "all_valid"

    return {
        "invalid_step_indices": invalid_step_indices,
        "error_types": sorted(list(error_set)),
        "status": status,
        "invalid_count": invalid_count,
        "total_steps": total_steps,
        "final_answer_correct": final_answer_correct,
    }
