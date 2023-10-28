from higher_lower_game_data import data
from resources import higher_lower_logo, vs_logo
from time import sleep
import random
from click import clear

print(higher_lower_logo)
print("Welcome to the celebrity game...")
sleep(2)

def assign_subject(subject):
    subj = random.choice(data)
    # name = subj['name']
    # follower_count = subj['follower_count']
    # description = subj['description']
    # country = subj['country']
    return subject.update(subj)

def compare(a, b):
    x = a['follower_count']
    y = b['follower_count']
    if x > y:
        # return a['name']
        return 'a'
    elif y > x:
        # return b['name']
        return 'b'


def game():
    clear()
    sub_a = {}
    sub_b = {}
    assign_subject(sub_a)
    assign_subject(sub_b)
    while sub_b == sub_a:
        assign_subject(sub_b)
    sub_a_details = f"{sub_a['name']}, {sub_a['description']}, from {sub_a['country']}"
    sub_b_details = f"{sub_b['name']}, {sub_b['description']}, from {sub_b['country']}"
    print(f"{higher_lower_logo}\n")
    print(f"{sub_a_details}")
    print(f"{vs_logo}")
    # print(sub_a_details)
    print(sub_b_details)
    print(sub_a['follower_count'])
    print(sub_b['follower_count'])
    sleep(2)
    current_score = 0
    choice = input(f"Who has more followers? Type 'A' or 'B': ").lower()
    winner = compare(sub_a, sub_b)
    
    game_proper = True
    while game_proper:

        if choice == winner:
            current_score += 1
            print(f"You're correct! Current score is: {current_score}")
        else: 
            print(f"Sorry that's wrong. Your final score is: {current_score}")
            if input("Would you like to play again? y/n: ") == "y":
                game()
            else:
                return
        sub_a.update(sub_b)
        assign_subject(sub_b)
        # while sub_b == sub_a:
        #     sub_b.update(assign_subject(sub_b))
        print(f"subj_a: {sub_a}   subj_b: {sub_b}")
        # assign_subject(sub_b)
        # print(f"subj_a: {sub_a}   subj_b: {sub_b}")
        sub_a_details = f"{sub_a['name']}, {sub_a['description']}, from {sub_a['country']}"
        sub_b_details = f"{sub_b['name']}, {sub_b['description']}, from {sub_b['country']}"
        print(sub_a_details)
        print(sub_b_details)
        print(sub_a['follower_count'])
        print(sub_b['follower_count'])
        choice = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        winner = compare(sub_a, sub_b)
    

    print('x' * 40)
    # print(sub_a_details)
    # print(sub_b_details)
    # print(sub_a['follower_count'])
    # print(sub_b['follower_count'])

    print(winner)
    return

game()