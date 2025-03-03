import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
output_list = []

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

while True:

    word = input("Enter a word: ").upper()

    if word == "EXIT":
        break

    output_list = [nato_dict[letter] for letter in word]
    print(output_list)
    

