import json
from datetime import datetime
from pathlib import Path
from .models import EvaluationResult


LOG_DIR = Path("logs")


def log_evaluation(result: EvaluationResult) -> Path:
    LOG_DIR.mkdir(exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = LOG_DIR / f"{result.task_id}_{timestamp}.json"

    payload = {
        "task_id": result.task_id,
        "reasoning_score": result.reasoning_score,
        "correctness_score": result.correctness_score,
        "overall_score": result.overall_score,
        "final_answer_correct": result.final_answer_correct,
        "failure_summary": result.failure_summary,
        "steps": [
            {
                "index": e.step.index,
                "text": e.step.text,
                "valid": e.valid,
                "errors": e.errors,
            }
            for e in result.evaluated_steps
        ],
    }

    with filename.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    return filename
