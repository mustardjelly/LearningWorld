from dataclasses import dataclass


@dataclass
class Answer():
    """Store a Quiz answer."""
    question: int = 0
    answer: str = None
    correct: bool = False
