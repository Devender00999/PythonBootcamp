# exception handling in python

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