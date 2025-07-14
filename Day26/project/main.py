# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(df)
#TODO 1. Create a dictionary in this format:
codes = {row.letter: row.code for (index, row) in df.iterrows()}

input_text = input("Enter a word: ")
print([codes[word.upper()] for word in input_text if word.upper() in codes.keys()] )
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

