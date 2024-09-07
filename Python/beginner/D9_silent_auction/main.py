import os

print("Welcome to the silent auction program.")

continuing = True
bids = {}
winning_bidder = ""
winning_amount = 0

while continuing:
    bidder = input("What is your bidder number? ")
    bid = int(input("What is your bid? $"))

    bids[bidder] = bid

    continue_ans = input("Are there any other bidders? Type 'yes' or 'no'. ")

    # continue prompt?
    if continue_ans == 'no':
        continuing = False
    elif continue_ans == 'yes':
        # Stack Overflow comin' in clutch with this command
        os.system('cls')
    else:
        print("Invalid input. Ending program.")
        continuing = False

# comparing bids for highest bid
for i in bids:
    highest_bid = 0
    if bids.get(i) > highest_bid:
        winning_bidder = i
        winning_amount = bids.get(i)

# announcing winner
print(f"\nThe winning bidder is {winning_bidder} with a bid of ${winning_amount}!")