from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator(nr_letters, nr_symbols, nr_numbers ):
   letters = [
      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
   ]

   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

   symbols = [
   '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
   '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<',
   '.', '>', '/', '?', '`', '~'
   ]
   password_list = []
   random_letters = [random.choice(letters) for _ in range(nr_letters)]
   random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
   random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

   password_list = random_letters + random_symbols + random_numbers
   random.shuffle(password_list)

   password = "".join(password_list)
   return password

def generate_password():
   password = password_generator(8, 5, 1)
   password_input.delete(0, END)
   password_input.insert(0, password)
   pyperclip.copy(password)
   
   
# ---------------------------- Search ------------------------------- #
def search():
   website = website_input.get()
   if len(website) == 0:
      messagebox.showerror(title='Oops', message="Please enter website name for search.")
   try:
      with open('passwords.json', 'r') as file:
         data = json.load(file)
         print(data.get(website))
         if data.get(website) is not None:
            details = data[website]
            messagebox.showinfo(title=website, message=f"There are the details entered: \nEmail: {details.get('email')}"
                                  f"\nPassword: {details.get('password')}\n",)
         else:
            messagebox.showwarning(title='Oops', message=f"There are no passwords saved for {website}.")
   except FileNotFoundError: 
      messagebox.showwarning(title='Oops', message="There are no passwords saved.")


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
      try: 
         password = {
            website: {
               "email": email,
               "password": password
            }
         }
         file = open('passwords.json', 'r')
         data = json.load(file)
      
      except:
         file = open('passwords.json', 'w')
         json.dump(password, file, indent=4)
      else:
         file = open('passwords.json', 'w')
         data.update(password)
         json.dump(data, file, indent=4)
      finally:
         file.close()
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

website_input = Entry(width=22)
website_input.grid(row=1, column=1)
website_input.focus()

search_btn = Button(text="Search", width=12, command=search)
search_btn.grid(row=1, column=2)

# username
username_label = Label(text='Email/Username: ')
username_label.grid(row=2, column=0)

username_input = Entry(width=38)
username_input.insert(0, "devender@gmail.com")
username_input.grid(row=2, column=1, columnspan=2)

# password
password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

# add button
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)









window.mainloop()

