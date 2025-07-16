import tkinter

# working with tkinter
window = tkinter.Tk()

window.title('My First GUI Program')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text='I am Label')
my_label.pack()

# window.mainloop()



# function with default values
def callMe(a, b = 2, c = 3):
   """a is mandatory\n
      b is 2 by default \n
      c is 3 by default\n
   """
   print(a, b, c)
   
# callMe(1)

# unlimited arguments(unlimited positional arguments) in a function
# converts given parameters to a tuple
def add(*args):
   print(sum(args))

# add(1,2,3,4,54)

# many keyword arguments
# converts given parameters to a dictionary
def add(**kwargs):
   print(kwargs)

# add(a=1, b=2, c=3 )

# class with many keyword arguments(kwargs)
# .get method in dictionary will return none if key does not exists
class Car():
   def __init__(self, **kw):
      self.model = kw.get('model')
      
car = Car(model="S3")
print(car.model)