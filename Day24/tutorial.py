
# Reading file
with open('../../../../../Desktop/my_file.txt') as file:
   contents = file.read()
   print(contents)

# writing on a file (will create file if it does not exists)
# with open('my_file.txt', mode='w') as file:
#    file.write('New Content!!')
   
# appending on a file (will create file if it does not exists)
# with open('/Users/devender/Documents/my_file.txt', mode='a') as file:
#    file.write('\nNew Content!!')
   
# absolute path
# absolute file path starts from the root of computer storage system
# relative to root
# /Users/devender/Documents/Work/report.doc

# relative path
# location of file from current directory 
# relative to current path
# ./Work/report.doc
