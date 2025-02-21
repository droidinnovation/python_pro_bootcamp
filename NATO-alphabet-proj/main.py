import pandas as pd

#TODO 1. Create a dictionary in this format:
df_phonetic = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in df_phonetic.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    name_input = input("Input a word: ").strip().upper()
    if len(name_input) > 0:
        try:
            output = [alphabet_dict[letter] for letter in name_input]
        except KeyError:
            print("Sorry only input alphabet please")
            generate_phonetic()
        else:
            print(output)

generate_phonetic()