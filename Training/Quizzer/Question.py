from dataclasses import dataclass, field
import logging
from typing import List


@dataclass
class Question():
    """Question model."""
    question: str = "Undefined"
    options: dict = field(default_factory=dict) 
    answer: int = None

    def __str__(self) -> str:
        """String representation."""
        question = f"Question: {self.question}"
        answer = f"Answer: {self.answer}"
        option = f"Options: {self.options}"

        return f"{question}, {answer}, {option}"

    def load(self, responses: List[str]):
        """Loads a question from a response."""
        if not responses:
            logging.debug("Empty line detected. Skipping")

        if len(responses) <= 3:
            logging.warning(f"Invalid data row. {responses}")
            return

        # Load Question
        self.question = responses[0]
        # Load Answer
        self.answer = responses[1]
        # Load Options
        index = 0
        for i in range(2, len(responses)):
            if i == len(responses) - 1:
                responses[i] = responses[i].strip()

            self.options[index] = responses[i]
            index += 1

    def get_answer(self) -> int:
        """Gets the correct answer."""
        return self.answer

    def get_options(self)-> List[str]:
        """Returns the answer options."""
        return self.options
