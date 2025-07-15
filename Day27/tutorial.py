import tkinter

window = tkinter.Tk()

window.title('My First GUI Program')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text='I am Label')
my_label.pack()

window.mainloop()



# function with default values

def callMe(a, b = 2, c = 3):
   """a is mandatory\n
      b is 2 by default \n
      c is 3 by default\n
   """
   print(a, b, c)
   
callMe(1)