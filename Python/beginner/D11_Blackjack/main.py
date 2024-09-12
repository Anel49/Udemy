import os, random

# clears the window so it's ✧･ﾟ: *✧･ﾟ:* cleaner *:･ﾟ✧*:･ﾟ✧
os.system('cls')

continuing, play = True, True
player_cards = []
nums = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = ["♥", "♦", "♣", "♠"]

def add_card():
    cont = True
    card = [random.choice(nums), random.choice(suits)]

    while cont:
        if card in player_cards:
            card = [random.choice(nums), random.choice(suits)]
        else:
            cont = False
    
    player_cards.append(card)

def card_graphic(num, suit):
    # if it's a 10, it has 2 characters, so the card graphic formation
    # has a one space difference
    if num == 10:
        print(" ___")
        print("|" + str(num) + " |")
        print("| " + suit + " |")
        print("|_" + str(num) + "|")
    # the card has a single character
    else:
        print(" ___")
        print("|" + str(num) + "  |")
        print("| " + suit + " |")
        print("|__" + str(num) + "|")

def dealer_cards(player_cards):
    dealers_total, players_total = 0, 0

    i = 0

    for card in player_cards:
        if card[0] in ("A", "J", "Q", "K"):
            if card[0] == "A":
                choice = int(input("You have an Ace. Would you like it to equal 1 or 10 points? Type \"1\" or \"10\". "))
                players_total += choice
            else:
                players_total += 10
        else:
            players_total += card[0]
        i += 1

    # 17 is a safe number to stop hitting at; also, too little time to make it
    # super realistic by also tracking the dealers's cards and making sure none
    # match the player's cards, though it can certainly be done.
    while dealers_total < 17:
        dealers_total += random.randint(1,10)
    
    print(f"\nYour total points is {players_total}.")
    print(f"The dealer's total points is {dealers_total}.")
    
    if players_total <= 21 and dealers_total <= 21:
        if dealers_total > players_total:
            print("The dealer won!")
        elif players_total > dealers_total:
            print("You won!")
        elif players_total == dealers_total:
            print("It's a tie! Neither wins!")
    elif players_total > 21 and dealers_total > 21:
        print("There is no winner!")
    elif players_total > 21:
        if dealers_total <= 21:
            print("The dealer won!")
    elif dealers_total > 21:
        if players_total <= 21:
            print("You won!")
        

# game starts with rules
print("Welcome to the game of Blackjack!")
print("The rules are simple: Try to get as close to 21 points without going over.")
print("Kings, Queens, and Jacks are worth 10 points.")
print("You can choose whether an Ace equals 1 or 10 points.")
inp = input("\nWould you like to start the game? Type \"y\" for yes or \"n\" for no. ")

# determining if the following while loop plays
if inp in ("y", "n"):
    if inp == "n":
        print("Ending program.")
        play = False
else:
    print("Invalid input. Ending program.")
    play = False

# while play is true, runs the program
while play:
    # clean window <3
    os.system('cls')
    add_card()
    add_card()

    print("\nYour first two cards are")
    
    # for loop for player's cards; also looped when requesting more cards
    card_i = 0
    for card in player_cards:
        card_graphic(player_cards[card_i][0], player_cards[card_i][1])
        card_i += 1

    # while loop so player can request another card
    while continuing:
        hit = input("\nWhat you like to draw another? Type \"y\" for yes or \"n\" for no. ")

        if hit in ("y", "n"):
            if hit == "y":
                add_card()
                
                card_i = 0
                print("Your cards are")
                for card in player_cards:
                    card_graphic(player_cards[card_i][0], player_cards[card_i][1])
                    card_i += 1
            else:
                dealer_cards(player_cards)
                continuing = False
        else:
            print("Invalid input. Ending game session.")
            continuing = False
        
    play_again = input("\nWould you like to play again? Type \"y\" for yes or \"n\" for no. ")

    # wanna play again?
    if play_again in ("y", "n"):
        # prevents while loop from running, ending the program
        if play_again == "n":
            play = False
        # set continuing to True so the while loop plays, and reset the player's cards
        else:
            continuing = True
            player_cards = []
    else:
        print("Invalid input. Ending program.")
        play = False