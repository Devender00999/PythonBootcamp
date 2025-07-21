from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
   website = website_input.get()
   email = username_input.get()
   password = password_input.get()
   
   if len(website) == 0 or len(email) == 0 or len(password) == 0:
      messagebox.showwarning(title='Oops', message="Please don't leave any fields empty!")
      return
   is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}"
                                  f"\nPassword: {password} \nIs it ok to save?",)
   if is_ok:
      with open('password.csv', 'a+') as file:
         file.seek(0)
         if len(file.readline()) == 0: 
            file.write('Website, Email, Password\n')
         file.write(f"{website},{email},{password}\n")
         website_input.delete(0, END)
         password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
myimage = PhotoImage(file='logo.png')

canvas.create_image(125, 100, image=myimage)
canvas.grid(row=0, column=1)

# website
website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)

website_input = Entry(width=38, )
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# username
username_label = Label(text='Email/Username: ')
username_label.grid(row=2, column=0)

username_input = Entry(width=38)
username_input.insert(0, "devender00999@gmail.com")
username_input.grid(row=2, column=1, columnspan=2)

# password
password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_btn = Button(text="Generate Password")
generate_btn.grid(row=3, column=2)

# add button
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)









window.mainloop()

