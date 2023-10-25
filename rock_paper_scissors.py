rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
from random import randint as rndint
import time
from click import clear

print("Welcome to play Rock, Paper, Scissors. It's fun!")
choice = ['r', 'p', 's']
continue_playing = True

while continue_playing:
    player_input = input("What's you sign? r-Rock, p-Paper, S-scissors\n")
    player = player_input.lower()
    if player not in choice:
        print("Your choice is invalid. YOU LOOSE!")
        exit()
    if player == 'r':
        print(f"{rock}\nYou chose Rock!")
        player = rock
    if player == 'p':
        print(f"{paper}\nYou chose Paper!")
        player = paper
    if player == 's':
        print(f"{scissors}\nYou chose Scissors!")
        player = scissors
    comp1 = ['rock', 'paper', 'scissors']
    comp = [rock, paper, scissors]
    computer = random.choice(comp)
    sign_word = comp.index(computer)
    # print(sign_word)
    print(f"{computer}\nComputer choose {comp1[sign_word]}")
    time.sleep(2)
    if player == rock and computer == paper:
        print("Sorry You loose!")
    if player == rock and computer == scissors:
        print("You Win!!!")
    if player == paper and computer == rock:
        print("You Win!!!")
    if player == paper and computer == scissors:
        print("Sorry You loose!")
    if player == scissors and computer == rock:
        print("Sorry You loose!")
    if player == scissors and computer == paper:
        print("You Win!!!")
    if player == computer:
        print("It's a Draw!")
    continue_message = input("Do you want to continue playing?: y/n\n")
    if continue_message == "n":
        continue_playing = False
    clear()
    
print("Goodbye")
