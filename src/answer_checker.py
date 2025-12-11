import ast
import re
from typing import Any, Optional


def extract_final_answer(raw_reasoning: str) -> Optional[str]:
    """
    Extract the final answer from the reasoning text.
    Looks for a line starting with 'Final Answer:' (case-insensitive).
    """
    for line in raw_reasoning.splitlines():
        line_stripped = line.strip()
        if line_stripped.lower().startswith("final answer:"):
            # Extract everything after the colon
            answer_part = line_stripped.split(":", 1)[1].strip()
            return answer_part
    return None


def parse_answer(answer_str: str) -> Any:
    """
    Attempt to parse the answer string into a Python object.
    Handles lists, numbers, and strings.
    """
    if answer_str is None:
        return None

    try:
        # Try to safely evaluate as a Python literal (list, int, etc.)
        return ast.literal_eval(answer_str)
    except (ValueError, SyntaxError):
        # If it fails, return as-is (string)
        return answer_str


def check_final_answer(raw_reasoning: str, expected_answer: Any) -> bool:
    """
    Check if the final answer in the reasoning matches the expected answer.

    Args:
        raw_reasoning: The full reasoning text from the agent.
        expected_answer: The expected answer from the task definition.

    Returns:
        True if the final answer matches expected_answer, False otherwise.
    """
    final_answer_str = extract_final_answer(raw_reasoning)

    if final_answer_str is None:
        return False

    parsed_answer = parse_answer(final_answer_str)

    # Compare parsed answer with expected
    return parsed_answer == expected_answer
