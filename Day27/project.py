import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")


# 
window.config(padx=20, pady=20)
label = tkinter.Label(text='is equal to')
label.grid(row=1, column=0)


entry = tkinter.Entry()

entry.grid(row=0, column=1)


label_miles = tkinter.Label(text="miles")
label_miles.grid(row=0, column = 2)

label_km = tkinter.Label(text="km")
label_km.grid(row=1, column = 2)

label_value = tkinter.Label(text=0)
label_value.grid(row=1, column=1)

def calculate_km():
   value = float(entry.get())
   label_value.config(text=value * 1.6)

button = tkinter.Button(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)



window.mainloop()