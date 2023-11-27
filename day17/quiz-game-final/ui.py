from tkinter import *
from quiz_brain import QuizBrain
# from data import question_data
# from question_model import Question

THEME_COLOR = "#375362"
WIDTH = 300
HEIGHT = 400


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        # self.correct_answer = self.quiz.current_correct_answer
        self.question_number = self.quiz.question_number
        self.scoring = self.quiz.score

# x---------------------------- Labels ------------------------x
        self.scoreboard = Label(text=f"Score: {self.scoring}", font=("Arial", 10), fg="white", bg=THEME_COLOR)
        self.scoreboard.grid(column=1, row=0, sticky=NE)#"bold"

# x--------------------------- CANVAS -------------------------x
        self.q_card = Canvas(width=300, height=250, bg='white')
        # self.q_card = Canvas(width=300, height=250, bg='yellow')
        self.q_in_qcard = self.q_card.create_text(150, 125, text='Welcome to QUIZZLER', font=('Arial', 20, 'italic'), width=280, fill=THEME_COLOR)
        self.q_card.grid(column=0, row=1, columnspan=2, pady=50)

# x--------------------------- Buttoms -----------------------x
        cross_img = PhotoImage(file=(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day17\quiz-game-final\images\false.png"))
        check_img = PhotoImage(file=(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day17\quiz-game-final\images\true.png"))

        self.cross = Button(width=50, height=50, image=cross_img, command=self.cross_button)#
        self.cross.grid(column=0, row=2)
        self.check = Button(width=50, height=50, image=check_img, command=self.check_button)#
        self.check.grid(column=1, row=2)
        

        self.window.after(2000, self.start)
        # self.start()

        self.window.mainloop()
        
    def start(self):
        self.q_card.config(bg='white')
        self.scoreboard.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.q_card.itemconfig(self.q_in_qcard, text=q_text)
        else:
            self.check.config(state='disabled')
            self.cross.config(state='disabled')
            self.q_card.itemconfig(self.q_in_qcard, text=f"Game over. Your final score is {self.quiz.score}")
            # timer = self.window.after(5000, exit)
            timer = self.window.after(5000, quit)

        # Define the check_true method
    def check_button(self):
        # Check if the user's answer is "True"
        self.user_feedback(self.quiz.check_answer('True'))
        # is_correct = self.quiz.check_answer('True')
        # self.user_feedback(is_correct)

    # Define the check_false method
    def cross_button(self):
        # Check if the user's answer is "False"
        is_correct = self.quiz.check_answer('False')
        self.user_feedback(is_correct)

    def user_feedback(self, is_correct):
        if is_correct:
            # self.q_card = self.q_card.config(bg='green')
            self.q_card.config(bg='green')
            # self.scoreboard = Label(text=f"Score: {self.scoring}", font=("Arial", 10), fg="white", bg=THEME_COLOR)
            self.q_card.itemconfig(self.q_in_qcard, text=f"You got it right!")
        elif not is_correct:
            # self.q_card = self.q_card.config(bg='red')
            self.q_card.config(bg='red')
            self.q_card.itemconfig(self.q_in_qcard, text=f"You got it wrong!\nThe correct answer is: {self.quiz.current_question_answr}.")

        self.window.after(1000, self.start)




    # if self.quiz.check_answer == True:
    #     self.q_card.config(bg="green")
    # else:
    #     self.q_card.config(bg="red")


    # def answer_false(self):
    #     self.quiz.check_false()
    #     self.q_in_qcard = self.q_card.itemconfig(self.q_in_qcard, text=self.quiz.current_correct_answer)
    #     if self.quiz.current_correct_answer == 'Correct':
    #         self.score += 1
    #         self.window.mainloop()
    #     else:
    #         self.window.mainloop()
    #         # pass

    # def answer_true(self):
    #     self.quiz.check_true()
    #     self.q_in_qcard = self.q_card.itemconfig(self.q_in_qcard, text=self.quiz.current_correct_answer)
    #     if self.quiz.current_correct_answer == 'Correct':
    #         self.score += 1
    #         self.window.mainloop()
    #     else:
    #         self.window.mainloop()
    #         # pass

        # self.question_bank = []
        # for question in question_data:
        #     question_text = question["question"]
        #     question_answer = question["correct_answer"]
        #     new_question = Question(question_text, question_answer)
        #     self.question_bank.append(new_question)
