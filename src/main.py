from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
    
def generate_password(): 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        is_empty = messagebox.showinfo(title="Oops", message="Make sure there are no empty fields!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        
        if is_ok:   
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}  |  {email}  |  {password}\n")
                website_input.delete(0, END)
                email_username_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./src/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


#labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_input = Label(text="Password:")
password_input.grid(column=0, row=3)


#entries

website_input = Entry(width=44)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_input = Entry(width=44)
email_username_input.grid(column=1, row=2, columnspan=2)\

password_input = Entry(width=26)
password_input.grid(column=1, row=3)


#buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()