from resources import guessing_game_logo
from click import clear
import random


def guess_game():

    clear()
    logo = guessing_game_logo
    print("Welcome to the number guessing game.")
    levels = {
    'e': 100,
    'm': 200,
    'h': 500,
    }
    diff_level = 0
    # level_key = 
    print(f"{logo}\n")
    # guesses = []
    choose_level = input("Choose dificulty level from e-Easy(1-100) m-Medium(1-200) h-Hard(1-500): ")
    diff_level = levels.get(choose_level)
    # numberlist = [i for i in range(1, diff_level + 1)]
    number = random.randint(1, diff_level)
    # number = random.choice(numberlist)
    attempts_left = 3
    guess = True

    while guess:
        print(number)
        if attempts_left == 0:
            print("You're out of attempts. You loose!")
            # return
            # guess = False
            break
        print(f"Attempts left: {attempts_left}")
        guessed_num = int(input(f'Guess a number. You have {attempts_left} attempts: '))
        if guessed_num > number:
            attempts_left -= 1
            print("Guess lower.")
        elif guessed_num < number:
            attempts_left -= 1
            print("Guess higher.")
        elif guessed_num == number:
            print("You guessed it right! YOU WIN!!!")
            break
        
    if input("Would you like to play again? y/n\n") == "y":
        guess_game()
    else:
        print("Thank you. Goodbye...")
        return
        # exit()


# print(numberlist)
# print(choose_level)
# print(diff_level)


guess_game()
