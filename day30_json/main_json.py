from tkinter import *
from tkinter import messagebox
import string
import random
import csv
import pyperclip
import json
from pathlib import Path

width = 200
height = 200
data_json = Path(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day29\password-manager-start\data.json")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    # Get the data from the Entry widgets
    website = website_entry.get().title()
    user = user_entry.get()
    pwd = pwd_entry.get()
    new_data = {
        website: {
            'email': user,
            'password': pwd, 
        }
    }

    # Check if any of the Entry widgets are empty
    if not website or not user or len(pwd) < 16:
        messagebox.showwarning("Missing Information", "Please fill all fields and password should not be less than 16 characters.")
        return
    # Ask for confirmation
    result = messagebox.askokcancel(title='Ok to Save', message="Save changes?")
    # If the user clicked "Cancel", stop execution of the function
    if not result:
        return
    data = [website_entry.get(), user_entry.get(), pwd_entry.get()]
# Open/Create the json file
    try:
        with open(data_json, 'r') as file:
            # json.dump(new_data, file, indent=4)
            data = json.load(file)
    except FileNotFoundError:
        with open(data_json, 'w') as file:
            # data = json.load(file)
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open(data_json, 'w') as file:
            json.dump(data, file, indent=4)
    finally:
            website_entry.delete(0, END)
            # user_entry.delete(0, END)
            pwd_entry.delete(0, END)
            print(data)

#Functions
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    pwd_entry.delete(0, 'end')
    char_list = [i for i in string.ascii_letters + string.digits + string.punctuation]
    pwd_list = [random.choice(char_list) for n in range(16)]
    pwd_list_str = "".join(pwd_list)
    pwd_entry.insert(0, string=pwd_list_str)#END, 
    return pwd_list_str

def copy_to_clipboard():
    return pyperclip.copy(pwd_entry.get())

def search_keyword():
    keyword = website_entry.get().title()
    try:
        with open(data_json) as f:
            data = json.load(f)
            result = data[keyword]
    except FileNotFoundError:
        messagebox.showinfo(keyword, "You have no saved data file yet. Start saving your data now.")
    except KeyError:
        messagebox.showinfo(keyword, "Keyword not found.")
    else:
        messagebox.showinfo(keyword, f"email: {result['email']}\npassword: {result['password']}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.minsize(width, height)
window.config(padx=20, pady= 20,) #bg=YELLOW

canvas = Canvas(width=width, height=height)   #bg=YELLOW, highlightthickness=0
img = PhotoImage(file=r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day29\password-manager-start\logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row= 0)

#Labels
website = Label(text='Website: ')
website.grid(column=0, row=1, sticky='e')

user = Label(text='Email/Username',)
user.grid(column=0, row=2, sticky='e')

pwd = Label(text='Password',)
pwd.grid(column=0, row=3, sticky='e')

#Entries
website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')

user_entry = Entry(width=30)
user_entry.insert(0, string='flpasana@outlook.com')
user_entry.grid(column=1, row=2, columnspan=2, sticky='w')

pwd_entry = Entry(width=30)
# pwd_entry.insert(0, 'Required')
pwd_entry.grid(column=1, row=3, columnspan=2, sticky='w')

#Button
pwd_button = Button(text="Generate Password", fg='black', bg='orange', width=15,command=generate_pwd)
pwd_button.grid(column=2, row=3, sticky='w')

add_button = Button(text="Add", fg='black', bg='green',width=20, command=add_data)
add_button.grid(column=1, row=4)

search_button = Button(text="Search", fg='black',width=15, command=search_keyword)#, bg='green'
search_button.grid(column=2, row=1, sticky='w')

copy_button = Button(text="Copy", fg='black', width=15, command=copy_to_clipboard)   #button_click, bg='yellow'
copy_button.grid(column=2, row=4, sticky='w')



window.mainloop()
