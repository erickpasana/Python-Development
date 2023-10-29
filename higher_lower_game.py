from higher_lower_game_data import data
from resources import higher_lower_logo, vs_logo
from time import sleep
import random
from click import clear

clear()
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
        return a
    elif y > x:
        return b
def start(sub_a, sub_b, sub_a_details, sub_b_details):
    print(f"{higher_lower_logo}\n")
    print(f"Compare A: {sub_a_details}")
    print(f"{vs_logo}")
    print(f"Compare A: {sub_b_details}")
    # print(sub_a['follower_count'])
    # print(sub_b['follower_count'])


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
    start(sub_a, sub_b, sub_a_details, sub_b_details)
    current_score = 0
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    choice = f"sub_{user_choice}"
    if user_choice == "a":
        choice = sub_a
    elif user_choice == "b":
        choice = sub_b
    winner = compare(sub_a, sub_b)
    
    play_again = 'n'
    game_proper = True
    while game_proper:
        if choice == winner:
            current_score += 1
            print(f"You're correct! Current score is: {current_score}")
        else: 
            print(f"Sorry that's wrong. Your final score is: {current_score}")
            play_again = input("Would you like to play again? y/n: ")
            if play_again == 'y':
                game()
            if play_again == 'n':
                return
            elif play_again != 'n':
                print("Your response is invalid.")
                return
        sub_a.update(sub_b)
        assign_subject(sub_b)

        while sub_b == sub_a:
            sub_b.update(assign_subject(sub_b))

        sub_a_details = f"{sub_a['name']}, {sub_a['description']}, from {sub_a['country']}"
        sub_b_details = f"{sub_b['name']}, {sub_b['description']}, from {sub_b['country']}"
        clear()
        start(sub_a, sub_b, sub_a_details, sub_b_details)
        print(f"You're correct! Current score is: {current_score}")
        user_choice = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == "a":
            choice = sub_a
        elif user_choice == "b":
            choice = sub_b
        winner = compare(sub_a, sub_b)

    print(winner)
    return

game()