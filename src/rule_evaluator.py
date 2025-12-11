from typing import List, Optional
from .models import Step, EvaluatedStep


# Phrases that indicate a step is referencing previous reasoning
CONTINUATION_PHRASES = [
    "next i will",
    "now i",
    "then i",
    "after that",
    "following this",
    "continuing",
    "based on this",
    "from the previous",
]

# Phrases that indicate proper backward reference
REFERENCE_PHRASES = [
    "from step",
    "as shown",
    "as calculated",
    "this gives",
    "this means",
    "therefore",
    "thus",
    "so",
    "which",
    "the result",
    "the answer",
    "we have",
    "i have",
    "remaining",
    "now",
]


def check_continuity(current_step: Step, previous_step: Optional[Step]) -> Optional[str]:
    """
    Check if a step that uses continuation language properly references previous content.

    Returns an error message if there's a potential missing link, None otherwise.
    """
    text_lower = current_step.text.lower()

    # Check if this step uses continuation language
    uses_continuation = any(phrase in text_lower for phrase in CONTINUATION_PHRASES)

    if not uses_continuation:
        return None

    # If it uses continuation language, check for backward references
    has_reference = any(phrase in text_lower for phrase in REFERENCE_PHRASES)

    # Also check if it references content from the previous step
    if previous_step:
        # Extract key terms from previous step (words > 3 chars)
        prev_terms = [
            word for word in previous_step.text.lower().split()
            if len(word) > 3 and word.isalpha()
        ]
        references_previous = any(term in text_lower for term in prev_terms)
    else:
        references_previous = False

    if not has_reference and not references_previous:
        return "Possible missing link in reasoning: continuation without clear reference to previous step"

    return None


def evaluate_steps(
    steps: List[Step],
    task_description: str,
    constraints: Optional[List[str]] = None,
) -> List[EvaluatedStep]:
    """
    Apply simple rules to each step.

    Rules (very minimal for this prototype):
    - Relevance: step text should mention something related to the task.
    - Constraint: step should not explicitly violate any constraints (if provided).
    - Continuity: steps using continuation language should reference previous content.
    Note: In a real system, these would be much richer and possibly LLM-assisted.
    """
    if constraints is None:
        constraints = []

    evaluated: List[EvaluatedStep] = []
    task_lower = task_description.lower()

    for i, step in enumerate(steps):
        errors: List[str] = []
        text_lower = step.text.lower()

        # Relevance rule
        if not any(token in text_lower for token in task_lower.split()[:3]):
            # extremely naive relevance heuristic
            errors.append("Possibly irrelevant to the task")

        # Constraint rule
        for constraint in constraints:
            if constraint.lower() in text_lower:
                errors.append(f"Potential constraint violation: '{constraint}'")

        # Continuity rule
        previous_step = steps[i - 1] if i > 0 else None
        continuity_error = check_continuity(step, previous_step)
        if continuity_error:
            errors.append(continuity_error)

        evaluated.append(
            EvaluatedStep(
                step=step,
                valid=len(errors) == 0,
                errors=errors,
            )
        )

    return evaluated
