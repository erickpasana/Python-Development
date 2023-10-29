from higher_lower_game_data import data as dt
from resources import higher_lower_logo, vs_logo
from time import sleep
import random
from click import clear

clear()
print(higher_lower_logo)
print("Welcome to the celebrity game...")
sleep(2)
data = dt 

def assign_subject(subject):
    subj = random.choice(data)
    return subject.update(subj)

def compare(user_choice, a, b):
    x = a['follower_count']
    y = b['follower_count']
    if x > y:
        return user_choice == 'a'
    elif y > x:
        return user_choice == 'b'
    
def start(sub_a, sub_b, sub_a_details, sub_b_details):
    print(f"{higher_lower_logo}\n")
    print(f"Compare A: {sub_a_details}")
    print(f"{vs_logo}")
    print(f"Against B: {sub_b_details}")

sub_a = {}
sub_b = random.choice(data)
current_score = 0
game_proper = True
while game_proper:

    sub_a.update(sub_b)
    sub_b = random.choice(data)
    while sub_b == sub_a:
        sub_b = random.choice(data)
    sub_a_details = f"{sub_a['name']}, {sub_a['description']}, from {sub_a['country']}"
    sub_b_details = f"{sub_b['name']}, {sub_b['description']}, from {sub_b['country']}"
    print(f"Compare A: {sub_a_details}")
    print(f"{vs_logo}")
    print(f"Against B: {sub_b_details}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    print(f"{higher_lower_logo}\n")
    if_correct = compare(user_choice, sub_a, sub_b)
    if if_correct:
        current_score += 1
        print(f"You're correct! Current score is: {current_score}")
    else: 
        game_proper = False
        print(f"Sorry that's wrong. Your final score is: {current_score}")


