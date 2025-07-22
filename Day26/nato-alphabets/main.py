# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(df)
#TODO 1. Create a dictionary in this format:
codes = {row.letter: row.code for (index, row) in df.iterrows()}

is_invalid = True
while is_invalid:
   try:
      input_text = input("Enter a word: ")
      output = [codes[word.upper()] for word in input_text]
      is_invalid = False
   except KeyError:
      print("Sorry, only letters in the alphabet please.")   
   else:
      print(output)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

