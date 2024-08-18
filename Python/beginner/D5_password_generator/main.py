import random

# lists of characters to use
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# input
numLetters = int(input("How many letters would you like in your password?\n"))
numNums = int(input("\nHow many numbers?\n"))
numSymb = int(input("\nHow many symbols?\n"))

# empty password type list to add to
passwordList = []

# randomly selecting and appending to passwordList
for x in range(1, numLetters + 1):
    randLetter = random.choice(letters)
    passwordList.append(randLetter)

for x in range(1, numNums + 1):
    randNum = random.choice(numbers)
    passwordList.append(randNum)

for x in range(1, numSymb + 1):
    randChar = random.choice(symbols)
    passwordList.append(randChar)

# shuffle the list for character index randomization
random.shuffle(passwordList)

# convert passwordList to string using join() function
password = "".join(passwordList)

# output
print(f"\nYour password is: {password}")
