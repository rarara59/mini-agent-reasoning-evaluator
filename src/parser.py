from typing import List
from .models import Step


def parse_reasoning(raw_text: str) -> List[Step]:
    """
    Very simple parser that splits on 'Step' or newlines.

    Example input:
        "Step 1: Identify the list.\nStep 2: Compare the first two items.\n..."

    This deliberately stays simple for clarity.
    """
    steps: List[Step] = []
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

    index = 1
    for line in lines:
        # If it contains 'Step', try to strip the prefix:
        lowered = line.lower()
        if "step" in lowered:
            # naive split on colon
            parts = line.split(":", 1)
            if len(parts) == 2:
                text = parts[1].strip()
            else:
                text = line
        else:
            text = line

        steps.append(Step(index=index, text=text))
        index += 1

    return steps
