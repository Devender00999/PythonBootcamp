import json
# exception handling in python
def exception_handling():
   try:
      # trying to run a code that can throw exception
      file = open('a.txt')
   # handling generic exception
   except: 
      print('Unable to open file.')
   else: 
      # will run after try block run successfully.
      file = open('a.txt')
      print(file.readlines())
   finally:
      # will run anyway.
      print('Ran after everything.')
   

def working_with_json():
   # reading json 
   with open('data.json', 'r') as file:
      data = json.load(file)
      print(data, type(data))
      
   # updating json file
   data.update({
      "Amazon": {
         "email": "devender@gmail.com",
         "password": "Pass@123"
      }
   })
   
   # saving to local file
   with open('data.json', 'w') as file:
      json.dump(data, file, indent=4)
      
      
      
working_with_json()