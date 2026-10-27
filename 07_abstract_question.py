from abc import ABC, abstractmethod
class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer): pass
class MCQQuestion(Question):
    def __init__(self, correct): self.correct = correct
    def evaluate_answer(self, answer): return answer.strip().lower() == self.correct.lower()
class TrueFalseQuestion(Question):
    def __init__(self, correct): self.correct = correct
    def evaluate_answer(self, answer): return answer.strip().lower() == self.correct.lower()
class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer): return len(answer.strip()) >= 20
questions = [MCQQuestion("b"), TrueFalseQuestion("true"), DescriptiveQuestion()]
for q, answer in zip(questions, ["b", "true", "Python supports reusable code through classes."]):
    print(type(q).__name__, "Correct/acceptable:", q.evaluate_answer(answer))
