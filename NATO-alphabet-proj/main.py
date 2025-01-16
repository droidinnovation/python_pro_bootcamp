import pandas as pd

#TODO 1. Create a dictionary in this format:
df_phonetic = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in df_phonetic.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name_input = input("Input a word :").strip().upper()
if len(name_input)>0:
    # alphabet_list = list(name_input.strip())
    # result = [value for (key, value) in alphabet_dict.items() if key in alphabet_list]
    result = [alphabet_dict[letter] for letter in name_input]

    print(result)
