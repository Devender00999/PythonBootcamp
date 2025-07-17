import tkinter

# creating window
window = tkinter.Tk()

# setting up window
window.title("First window")
window.minsize(width=500, height=300)

# creating label in tkinter
# adding label to window
my_label = tkinter.Label(text='I am Label', font=("Times", 34,'bold'))
my_label.pack()


# changing text in label
my_label['text'] = "Hello World!"
my_label.config(text="Hello World!")

text = tkinter.StringVar()

# input using Entry
entry = tkinter.Entry(textvariable=text)
entry.pack()


def replace_text():
   my_label.config(text=text.get())
   
# button
button = tkinter.Button(text="Click Me!", command=replace_text)
button.pack()



# stopping window from auto closing
window.mainloop()

