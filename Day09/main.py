import os
from art import logo
os.system('cls')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program. ")
bidding_finished = True
bids = {}

winner = ''
def finding_winner(bidding_recored):  
   
    for bidder in bidding_recored:
        highest_bid =0
        bid_amount = bidding_recored[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner =bidder
    print(f"the winner is { winner} with a bid of ${highest_bid}")
 

while bidding_finished:
    name =input("What's your name?: ") #key
    price = int(input("What's your bid?: "))
    bids[name] = price#always save the bidder
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if bidders == 'yes':    
        clear()

    else:
        bidding_finished= False  
        finding_winner(bids)


            



