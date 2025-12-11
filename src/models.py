from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
class Step:
    index: int
    text: str


@dataclass
class EvaluatedStep:
    step: Step
    valid: bool
    errors: List[str]


@dataclass
class EvaluationResult:
    task_id: str
    reasoning_score: float
    correctness_score: float
    overall_score: float
    evaluated_steps: List[EvaluatedStep]
    final_answer_correct: bool
    failure_summary: Dict[str, Any]
