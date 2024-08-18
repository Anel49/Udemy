line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# changing case for easier comparison
position = list(position.upper())
invalid_input = "Invalid input. Please enter a letter and number without any spaces."

# must have 2 entries only
if len(position) != 2:
    print(invalid_input)
else:
    # index 0 must be a letter and index 1 must be a number
    if position[0].isalpha() and position[1].isnumeric:
        # line1 (row)
        if position[1] == '1':
            # columns
            if position[0] == 'A':
                line1[0] = "X"
            elif position[0] == 'B':
                line1[1] = "X"
            elif position[0] == 'C':
                line1[2] = "X"
            # entered something other than A, B, or C
            else:
               print(invalid_input)
        # line2 (row)
        elif position[1] == '2':
            # columns
            if position[0] == 'A':
                line2[0] = "X"
            elif position[0] == 'B':
                line2[1] = "X"
            elif position[0] == 'C':
                line2[2] = "X"
            # entered something other than A, B, or C
            else:
               print(invalid_input)
        # line3 (row)
        elif position[1] == '3':
            # columns
            if position[0] == 'A':
                line3[0] = "X"
            elif position[0] == 'B':
                line3[1] = "X"
            elif position[0] == 'C':
                line3[2] = "X"
            # entered something other than A, B, or C
            else:
               print(invalid_input)
        # entered something other than 1, 2, or 3
        else:
            print(invalid_input)
    # not alphanumeric, invalid input
    else:
        print(invalid_input)

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
