############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
from time import sleep
from mywords import black_jack_logo
from click import clear

print("Welcome to Black Jack game")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal(player):
    for card in range(2):
        player.append(random.choice(cards))
def hit(player):
    player.append(random.choice(cards))

def compare1(player1, dealer):
    player1_score = sum(player1)
    dealer_1stcard = dealer[0]
    return print(f"Your score: {player1_score}\nDealer 1st card: {dealer_1stcard}")
def compare_final(player1, dealer):
    player1_score = sum(player1)
    dealer_score = sum(dealer)
    if player1_score > dealer_score:
        return print(f"Your Score is: {player1_score}\nDealer Score is: {dealer_score}\n You Win!")
    if player1_score < dealer_score:
        return print(f"Your Score is: {player1_score}\nDealer Score is: {dealer_score}\n You Loose!")
    if player1_score == dealer_score:
        return print(f"Your Score is: {player1_score}\nDealer Score is: {dealer_score}\n It's a draw!")


def game():

    clear()
    print(black_jack_logo)
    player1 = []
    dealer = []
    print('x' * 40)
    deal(player1)
    deal(dealer)
    print(player1)
    print(dealer)
    player1_score = sum(player1)
    dealer_score = sum(dealer)
    print('x' * 40)
    compare1(player1, dealer)

    stay_process = True
    while stay_process:
        if player1_score == 21:
            break
        if player1_score > 21:
            if 11 in player1:
                player1[player1.index(11)] = 1
                player1_score = sum(player1)
            else:
                print(f"Your score is {player1_score} and over 21. You loose!")
                if input("Press 'y' if you want to play again.") == 'y':
                    game()
                else:
                    print("Thank you and Goodbye!")
                    exit()
                # player1_score = 0
                # stay_process = False
                # break
        print(f"{player1} = {player1_score}")
        hit_stay = input("Hit: h or Stay: s\n")
        # sleep(2)
        if hit_stay == 'h':
            hit(player1)
            player1_score = sum(player1)
            print(f"{player1} = {player1_score}")
        elif hit_stay == 's':
            stay_process = False
            break
    print("Dealer Turn")
    # sleep(3)
    # print(dealer)
    print(f"Your score: {player1_score}\nDealer: {dealer_score}")
    # sleep(1)
    dealer_stay = False
    while not dealer_stay:
        if dealer_score == 21:
            break
        if dealer_score > 21:
            if 11 in dealer:
                dealer[dealer.index(11)] = 1
                dealer_score = sum(dealer)
                # if dealer_score < player1_score:
                #     hit(dealer)
                #     dealer_score = sum(dealer)
            else:
                print(f"Dealer Score is: {dealer_score} and over 21.\nYou Win!")
                if input("Press 'y' if you want to play again.") == 'y':
                    game()
                else:
                    print("Thank you and Goodbye!")
                    exit()
                # dealer_score = 0
                # dealer_stay = False
                # break
        print(dealer)
        print(dealer_score)
        if dealer_score < 17:
            hit(dealer)
            dealer_score = sum(dealer)
            print(f"{dealer} = {dealer_score}")
            # sleep(1)
        # elif dealer_score > 21:
        #     if 11 in dealer:
        #         dealer[dealer.index(11)] = 1
        #         dealer_score = sum(dealer)
        #         hit(dealer)
        #     print("Dealer Score is: {dealer_score} and over 21.\nYou Win!")
        #     dealer_stay = False
        #     break
        elif dealer_score < 21:
            print(f"{dealer} = {dealer_score}")
            if player1_score > dealer_score:
                if 11 in dealer:
                    dealer[dealer.index(11)] = 1
                    dealer_score = sum(dealer)
                    hit(dealer)
                    dealer_score = sum(dealer)
                else:
                    hit(dealer)
                    dealer_score = sum(dealer)
                    print(f"{dealer} = {dealer_score}")
                    # dealer_stay = False
                    # break
            else:
                dealer_stay = False
                break

    
    compare_final(player1, dealer)
    if input("Press 'y' if you want to play again.") == 'y':
        # player1 = []
        # dealer = []
        game()
    else:
        print("Thank you and Goodbye!")
        exit()
    
game()

