import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

# makes printing simpler
images = [rock, paper, scissors]
words = ["rock", "paper", "scissors"]

choice = input("What do you choose? Type '0' for rock, '1' for paper, or '2' for scissors.\n")

# if input is numeric, proceed
if choice.isnumeric():
    # convert to int for comparisons
    choice = int(choice)

    # must be between from 0 to 2, inclusive
    if choice < 0 or choice > 2:
        print("Invalid input. You lose!")
    else:
        print(f"You chose {words[choice]}{images[choice]}")

        comp_choice = random.randint(0,2)
        print(f"\nComputer chose {words[comp_choice]}{images[comp_choice]}")

        # adding a blank newline for aesthetics
        print()
        # draw
        if comp_choice == choice:
            print("Tie!")
        # comp winning
        elif comp_choice == 0 and choice == 2:
            print("Computer wins!")
        elif comp_choice == 1 and choice == 0:
            print("Computer wins!")
        elif comp_choice == 2 and choice == 1:
            print("Computer wins!")
        # player winning
        elif choice == 0 and comp_choice == 2:
            print("You win!")
        elif choice == 1 and comp_choice == 0:
            print("You win!")
        elif choice == 2 and comp_choice == 1:
            print("You win!")
else:
    print("Invalid input. You lose!")
