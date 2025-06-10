# Caesar Cipher

alphabets = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
]


def encrypt(original_text: str, shift_amount: int):
   encrypted_text = ""
   for i in range(len(original_text)):
      char = original_text[i]
      if (char in alphabets):
         idx = alphabets.index(char)
         encrypted_text += alphabets[(idx + shift_amount) % 26]
      else:
         encrypted_text += char
   print(encrypted_text)
# encrypt(text, shift)

def descrypt(cipher_text: str, shift_amount: int):
   original_text = ""
   for i in range(len(cipher_text)):
      char = cipher_text[i]
      if (char in alphabets):
         idx = alphabets.index(char)
         original_text += alphabets[(idx - shift_amount) % 26]
      else:
         original_text += char
   print(original_text)
# descrypt(text, shift)

def caesar(direction, input_text, shift_amount):
   original_text = ""
   if direction == 'decode':
      shift_amount *= -1
   for i in range(len(input_text)):
      char = input_text[i]
      if (char in alphabets):
         idx = alphabets.index(char)
         original_text += alphabets[(idx + shift_amount) % 26]
      else:
         original_text += char
   print(f"Here's the {direction}d result: {original_text}")

print("""

        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
 
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88                 
""")

while True:
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   if direction not in ['encode', 'decode']:
      print("Please choose 'encode' or 'decode'.")
      continue
   text = input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))
   caesar(direction, text, shift)
   repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

   if repeat != 'yes':
      print("Goodbye :)")
      break
   
