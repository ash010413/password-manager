from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
# import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    pass_entry.insert(0,password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    password = pass_entry.get()
    email = email_entry.get()
    new_data = {website:{
        "email": email,
        "password": password,
    }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Ayy, Do not leave any fields empty!!')
    else:
        try:
            with open('data.json','r') as data_file:
                # json.dump(new_data,data_file,indent=4)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
                # print(data)
        finally:
            web_entry.delete(0,END)
            pass_entry.delete(0,END)
            web_entry.focus()

# ---------------------------- UI SETUP -------------------------------
def find_password():
    try:
        with open('data.json','r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File found.")
    else:
        json_data_key = []
        for key in json_data:
            json_data_key.append(key)
        if web_entry.get() in json_data_key:
            messagebox.showinfo(title='Details',message=f'Website: {web_entry.get()}\nPassword: {json_data[web_entry.get()]["password"]}')
        else:
            messagebox.showinfo(title="Error",message=f"No details for {web_entry.get()} exists.")
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website = Label(text='Website:')
website.grid(row=1,column=0)

email_username = Label(text='Email/Username:')
email_username.grid(row=2,column=0)

password = Label(text='Password:')
password.grid(row=3,column=0)

web_entry = Entry(width=31)
web_entry.grid(row=1,column=1,columnspan=1)
web_entry.focus()

search = Button(text="Search",width=22,command=find_password)
search.grid(row=1,column=2,columnspan=1)

email_entry = Entry(width=54)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'ashwin@gmail.com')

pass_entry = Entry(width=32)
pass_entry.grid(row=3,column=1)

gen_pass = Button(text='Generate Password',command=generate_password,width=22)
gen_pass.grid(row=3,column=2)

add = Button(text='Add',width=36,command=save)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()