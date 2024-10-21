from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# taking data from data.py and turning them into Question classes
for x in question_data:
    question_bank.append(Question(x.get("text"), x.get("answer")))

# creating QuizBrain class for use
quiz = QuizBrain(question_bank)

quiz.next_question()
print(f"Your final score is {quiz.score}/{quiz.question_num}.")