from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_list.append(question)

quiz = QuizBrain(question_list)
choice = input("Hello! How woud you like to play? (order/random)\n")
if choice == "random":
    quiz.go_randomly()
else:
    quiz.go_in_order()