import logging
import os
from Answer import Answer
from Question import Question


class Quiz:
    def __init__(self):
        self._questions: list[Question] = list()
        self._answers: list[Answer] = list()
        self._logger = logging.getLogger(__name__)

    def load(self):
        print(os.getcwd())

        file="F:\\repos\LearningWorld\Training\Quizzer\Data\Strings.csv"
        with open(file, "r") as csv_file:
            # csv_reader = csv.reader(csv_file)
            # Has a header, will skip
            header = True
            for line in csv_file.readlines():
                line: str
                if header:
                    header=False
                    continue

                responses = line.split(", ")
                cur_question = Question()
                cur_question.load(responses)
                self.set_question(cur_question)

    def set_answer(self, answer: Answer) -> None:
        """Add a response from a quiz."""
        self._answers.append(answer)

    def get_answer(self, question: int) -> Answer:
        return self.answers.get(question)

    def set_question(self, question: Question) -> None:
        """Add a question to the quiz."""
        self._questions.append(question)

    def print_questions(self) -> None:
        """Print all the questions."""
        for question in self._questions:
            print(question)

quiz = Quiz()
quiz.load()
quiz.print_questions()