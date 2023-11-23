from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

THEME_COLOR = "#375362"
WIDTH = 200
HEIGHT = 400


class QuizInterface:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        # self.question_list = q_list
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.question_bank.append(new_question)
        self.quiz = QuizBrain(self.question_bank)

        self.q_card = Canvas(self.window, width=WIDTH, height=HEIGHT/2, )#
        q_in_qcard = self.q_card.create_text(100, 100, font=('Arial', 20, ), fill='black', text='Hello')#self.quiz.next_question()
        self.q_card.grid(column=0, row=1, columnspan=2)

        #Buttoms
        # self.cross = Button()
        cross_img = PhotoImage(file=(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day17\quiz-game-final\images\false.png"))
        self.cross = Button(width=50, height=50, image=cross_img, )#command=create_flash_card
        self.cross.grid(column=0, row=2)

        # # check = Button()
        check_img = PhotoImage(file=(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day17\quiz-game-final\images\true.png"))
        self.check = Button(width=50, height=50, image=check_img, )#command=words_to_learn
        self.check.grid(column=1, row=2)

        #Labels
        self.score = Label(text="Score: 0", font=("Arial", 10, ), bg=THEME_COLOR)
        self.score.grid(column=1, row=0, sticky=NE)#"bold"




        self.window.mainloop()

