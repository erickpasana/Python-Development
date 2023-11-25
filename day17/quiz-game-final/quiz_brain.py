import html
# from ui import QuizInterface

# ui = QuizInterface()

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[self.question_number]
        self.current_question_answr = self.current_question.answer
        self.current_question = html.unescape(self.current_question.text)
        self.current_correct_answer = self.current_question_answr

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            print(f"{len(self.question_list)} - {self.question_number}")
            return True
        else:
            return False

    def next_question(self):
        # current_question derived from list from main.py Question Class
        # print(f"{quiz_question}")
        self.current_question = self.question_list[self.question_number]
        self.quiz_question = html.unescape(self.current_question.text)
        print(self.quiz_question)
        print(self.score)
        print(self.current_question_answr)
        return f"{self.question_number+1}: {self.quiz_question}"
        # user_answer = input(f"Q.{self.question_number}: {quiz_question} ((t)True/(f)False): ")
        # self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer):
        if user_answer == self.current_question_answr:
            self.score += 1
            self.question_number += 1
            return True
            # print(f"You got it right!")
        else:
            self.question_number += 1
            return False
            # print(f"That's wrong.\nThe correct answer is: {self.current_question_answr}.")
        # print(f"The correct answer was: {correct_answer}.")
        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")


    # # Define the check_answer method
    # def check_answer(self, user_answer):
    #     # Get the correct answer from the quiz brain object
    #     correct_answer = self.current_question_answr
    #     self.question_number += 1

    #     # Compare the user's answer with the correct answer
    #     if user_answer == correct_answer:
    #         self.score += 1
    #         self.current_correct_answer = 'Correct'
    #     else:
    #         self.current_correct_answer = 'Wrong'
            # return False
            # Check if there are more questions left
        # if self.quiz.is_end_of_quiz():
            # Display a message on the canvas
            # self.q_card.itemconfig(self.q_in_qcard, text=f"End of the quiz.\nYour final score is: {self.score_var.get()}/{self.quiz.question_number}")
        # else:
        #     # Call the start method after 1 second
        #     self.window.after(1000, self.start)