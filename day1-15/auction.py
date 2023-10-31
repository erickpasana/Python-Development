from click import clear
from mywords import auction_logo as aucl
from time import sleep

clear()
print(aucl)
print("Welcome to this Project Bidding")
project = "SEAWALL"
print(f"The Project Name is {project}.")
sleep(3)
print("May I request the bidders please and input your respective names and bid prices.")

add_bid = True
bids_list = {}
# winning_price = ""
def winner():
    winning_bidder = ""
    winning_bid = 0
    for key in bids_list:
        # winning_bid[key] = value
        amount = bids_list[key]
        if amount > winning_bid:
            winning_bidder = key
            winning_bid = amount
    print(f"The winning bidder is {winning_bidder} with a bid of ${winning_bid}.")
    

while add_bid:
    # bids = {}
    print(aucl)
    name = input("Name: ")
    bid_price = int(input("Bid: $"))
    bids_list[name] = bid_price

    # clear()
    print("Thank you.")
    more_bids = input("Are there anymore bids? y/n\n")
    if more_bids == 'n':
        add_bid = False
    clear()

winner()
print(bids_list)
# print(winning_bid)
