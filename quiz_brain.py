import random
from random import Random
randomizer = Random()
class QuizBrain():
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def go_in_order(self):
        if self.question_number == 12:
            print(f"You won! Your final score is {self.question_number}")
        else:
            current_question = self.question_list[self.question_number]
            choice = input(f"Q{self.question_number + 1}. {current_question.text} (True/False)\n")
            if choice == current_question.answer:
                self.question_number += 1
                self.go_in_order()
            else:
                print(f"Wrong. Your score is {self.question_number}")

    def go_randomly(self):
        if len(self.question_list) == 0:
            print(f"You won! Your final score is {self.question_number}")
        else:
            number = random.randint(0, len(self.question_list)-1)
            current_question = self.question_list[number]
            self.question_list.remove(current_question)
            choice = input(f"Q{self.question_number + 1}. {current_question.text} (True/False)\n")
            if choice == current_question.answer:
                self.question_number += 1
                self.go_randomly()
            else:
                    print(f"Wrong. Your score is {self.question_number}")