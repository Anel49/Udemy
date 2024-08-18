# Family-friendly "Hangman"
import random

# short word list
wordList = ["cantaloupe", "bad", "dare", "loop", "track", "wash", "bullet", "articulate", "cylinder", "build", "popular", "forecast", "sweep", "clay", "dividend", "unlike", "area", "export", "ruin", "facility", "inflate", "splurge", "cell", "question", "revive", "cellar", "move", "fit", "apple", "copy", "flush", "immune", "abundant", "gloom", "state", "reserve", "sphere", "translate", "broken", "clean", "technology", "frighten", "emotion", "die", "coffin", "dribble", "domination", "exaggerate", "live", "flour"]
# chooses one
word = random.choice(wordList)
# empty list to compare and play with
wordDisplay = []
# player's number of guesses left
chances = 6

# making the displayed form of the word
for x in word:
    wordDisplay += "_"

# welcome message, first blanks of the word
print("\nWelcome to a family-friendly version of Hangman! Begin guessing!")
# converting to a string and adding spacing for ease of reading, as well as an
# initial newline for additional legibility
print("\n" + " ".join(wordDisplay))

# while the player still has at least 1 chace and there is still a letter to
# be guessed
while (chances > 0) and ("_" in wordDisplay):

    # reset count for next guess
    count = 0
    # chances visual
    print(f"\nChances: {chances}")

    # guess input and lowers for comparison
    guess = input("\nGuess a letter: ").lower()

    # range using length of word
    for x in range(len(word)):
        # grabs the letter to compare guess with
        letter = word[x]
        # if true, replace letter in display and add to counter for following
        # if block
        if guess == letter:
            wordDisplay[x] = guess
            count += 1
    # if the count is 0, that means the player did not correctly guess,
    # deducting a chance
    if count == 0:
        chances -= 1
    # spacing
    print()
    # converting to a string and adding spacing for ease of reading
    print(" ".join(wordDisplay))

# while loop ended, meaning the player hit 0 chances or correctly guessed
# the word

# if the chances are zero, they lost
if chances == 0:
    print(f"\nThe word was {word}. Game over.")
# else if they still have chances, they won
else:
    print(f"\nCongratulations! You won!")
