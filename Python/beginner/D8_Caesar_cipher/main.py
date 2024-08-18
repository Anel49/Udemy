alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the Caesar Cipher. Non-alphabetical characters will remain the same.")

# rerun is true on first run
rerun = True

# keep the program running
while rerun:
    cipher = input("Type \"encode\" to encrypt or type \"decode\" to decrypt: ").lower()

    if cipher in ("encode", "decode"):
        msg = input("\nType your message:\n").lower()
        shift = input("\nType the shift number:\n")
        
        # gotta be numeric, folks
        if shift.isnumeric():
            shift = int(shift)
            new_text = ""

            # decrements index if decoding
            if cipher == "decode":
                shift *= -1
            
            # looping through the message using the letter
            for i in msg:
                # accounting for spaces and numbers
                if not i.isalpha():
                    new_text += i
                else:
                    # add the shift
                    shifted_position = alphabet.index(i) + shift
                    # loops back to front if over 25 length, avoiding an index out of range error
                    shifted_position %= len(alphabet)
                    new_text += alphabet[shifted_position]

            print(f"\nHere is your {cipher}d message: \"{new_text}\"")

            # reruning program
            reruninp = input("\nWould you like to run again? Type \"yes\" or \"no\": ").lower()
            # spacing
            print()
            
            if reruninp not in ('yes', 'no'):
                # first example of invalid input; runs if input does not meet the specified criteria
                print("Invalid input. Ending session.")
                rerun = False
            elif reruninp == 'no':
                print("Ending session.")
                rerun = False
        else:
            print("\nInvalid input. Ending session.")
            rerun = False
    else:
        print("\nInvalid input. Ending session.")
        rerun = False
