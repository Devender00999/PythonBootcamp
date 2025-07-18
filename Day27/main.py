import tkinter

# creating window
window = tkinter.Tk()

# setting up window
window.title("First window")
window.minsize(width=500, height=300)

# padding
window.config(padx=20, pady=20)

# creating label in tkinter
# adding label to window
my_label = tkinter.Label(text='I am Label', font=("Times", 34,'bold'))
# my_label.pack(side='left')
my_label.grid(row=0, column=0)


# changing text in label
my_label['text'] = "Hello World!"
my_label.config(text="Hello World!")

# input using Entry
entry = tkinter.Entry()
# entry.pack(side="left")
entry.grid(row=3,column=3)


def replace_text():
   my_label.config(text=entry.get())
   
# button
button = tkinter.Button(text="Click Me!", command=replace_text)
button.grid(row=1, column=1)

# button
new_button = tkinter.Button(text="New Button!", command=replace_text)
new_button.grid(row=0, column=2)



# stopping window from auto closing
window.mainloop()

