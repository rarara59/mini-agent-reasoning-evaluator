from typing import List
from .models import EvaluatedStep


def compute_scores(
    evaluated_steps: List[EvaluatedStep],
    final_answer_correct: bool,
    reasoning_weight: float = 0.7,
    correctness_weight: float = 0.3,
) -> tuple[float, float, float]:
    """
    Compute reasoning_score, correctness_score, overall_score.
    """
    total_steps = len(evaluated_steps)
    if total_steps == 0:
        reasoning_score = 0.0
    else:
        valid_steps = sum(1 for e in evaluated_steps if e.valid)
        reasoning_score = (valid_steps / total_steps) * 100.0

    correctness_score = 100.0 if final_answer_correct else 0.0
    overall_score = reasoning_weight * reasoning_score + correctness_weight * correctness_score

    return reasoning_score, correctness_score, overall_score
