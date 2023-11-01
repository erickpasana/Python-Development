# from data import question_data as qdata
# import random

class Question:
    # question = random.choice(qdata)
    # q_text = question['question']
    # q_answer = question['correct_answer']

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


