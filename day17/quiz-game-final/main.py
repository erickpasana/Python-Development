from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from click import clear
from ui import QuizInterface

quiz = QuizInterface()
# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     # clear()
#     quiz.next_question()
#     print(f"Your score is: {quiz.score}/{quiz.question_number}")
#     if input("Would you like to continue playing? y/n: ") == "y":
#         # quiz.still_has_questions = False
#         continue
#     else:
#         exit()

# print("You've completed the quiz")
# print(f"Your final score is: {quiz.score}/{quiz.question_number}")
# print(question_bank)
# print(question_data[5]["correct_answer"])
# print(question_data[5]["correct_answer"][0])