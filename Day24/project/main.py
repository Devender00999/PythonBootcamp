#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('Input/Letters/starting_letter.txt') as letter_file:
   letter = letter_file.read()
   
   with open('Input/Names/invited_names.txt') as name_list:
      names = name_list.readlines()
      
      for name in names:
         with open(f"Output/ReadyToSend/letter_to_{name.strip()}.txt", mode = 'w') as final_letter:
            final_letter.write(letter.replace('[name]', name.strip()))
            
            
      