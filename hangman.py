import random
# import mywords
from resources import logo
from resources import stages
from resources import mywords


# print(mywords)
# word_list = ["aardvark", "baboon", "camel"]
word_list = mywords

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word_list.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word_list.

chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)

word_length = len(chosen_word_list)
total_chances = 0
missed_guess = 0
# print(chosen_word_list)
# print(word_length)
display = ["_" for i in range(word_length)]
guessed_letters = 0
guessed_letters_list = []
# for i in range(len(chosen_word_list)):
#     display += "_"
print(display)
print(word_length)

while missed_guess < 6 and "_" in display:
    user_guess = input("Guess a letter: ").lower()
    guessed_letters_list += user_guess
    # if user_guess in display:

    if user_guess in display:
        print("You already guessed it. You missed!")
        missed_guess += 1
        print(f"Your current status: {display}")
        print(f"Miss: {missed_guess} Chances Left: {10 - missed_guess}")
        continue
        # break
    if user_guess in chosen_word:
        for n in range(word_length):
            if user_guess == chosen_word_list[n]:
                display[n] = user_guess
                # guessed_letters += 1
                print("correct")
                # continue
                # break
            else:
                # missed_guess += 1
                # print("Wrong")
                # print(display)
                continue
                # break
    else:
        missed_guess += 1
        print("You got it wrong this time.")
    print(mywords[6-missed_guess])
    print(f"Your current status: {' '.join(display)}")
    print(f"Your Guessed list: {guessed_letters_list}")
    print(f"Miss: {missed_guess} Chances Left: {6 - missed_guess}")
if "_" not in display:
    print(display)
    print(f"The hidden word is {chosen_word}. You Won!!!")
else:
    print(f"The hidden word is {chosen_word}. You Lost!!!")
print("Game Over!!!")
    # print(input("What's your first guess?"))




