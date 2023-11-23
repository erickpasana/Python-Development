from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

THEME_COLOR = "#375362"
WIDTH = 200
HEIGHT = 400


class QuizInterface:

    def __init__(self):
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

        self.q_card = Canvas(width=WIDTH, height=HEIGHT, )
        q_in_qcard = self.q_card.create_text(100, 200, font=('Arial', 20, ), fill='black', text=self.quiz.next_question())
        self.q_card.grid(column=0, row=2, columnspan=2)

        #Buttoms
        # cross = Button()
        # cross_img = ImageTk.PhotoImage(Image.open(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\wrong.png"))
        # cross = Button(width=50, height=50, image=cross_img, command=create_flash_card)#window
        # cross.grid(column=0, row=1)

        # # check = Button()
        # check_img = ImageTk.PhotoImage(Image.open(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\right.png"))
        # check = Button(width=50, height=50, image=check_img, command=words_to_learn)#window
        # check.grid(column=1, row=1)




        self.window.mainloop()

