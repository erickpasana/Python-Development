from tkinter import *
from tkinter import messagebox
import string
import random
import csv


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
        # Get the data from the Entry widgets
    website = website_entry.get()
    user = user_entry.get()
    pwd = pwd_entry.get()

    # Check if any of the Entry widgets are empty
    if not website or not user or len(pwd) < 16:
        messagebox.showwarning("Missing Information", "Please fill all fields and password should be not less than 16 characters.")
        return
    # Ask for confirmation
    result = messagebox.askokcancel(title='Ok to Save', message="Save changes?")
    # If the user clicked "Cancel", stop execution of the function
    if not result:
        return
    data = [website_entry.get(), user_entry.get(), pwd_entry.get()]
# Open the CSV file
    with open("data.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the text to a new row in the CSV file
        writer.writerow(data)
        website_entry.delete(0, END)
        # user_entry.delete(0, END)
        pwd_entry.delete(0, END)
        print(data)

def copy_to_clipboard():
    # Get the text from the Entry widget
    text = pwd_entry.get()
    # Clear the clipboard
    window.clipboard_clear()
    # Copy the text to the clipboard
    window.clipboard_append(text)

#Functions
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    pwd_entry.delete(0, 'end')
    char_list = [i for i in string.ascii_letters + string.digits + string.punctuation]
    pwd_list = [random.choice(char_list) for n in range(16)]
    pwd_list_str = "".join(pwd_list)
    pwd_entry.insert(0, string=pwd_list_str)#END, 
    return pwd_list_str
# ---------------------------- UI SETUP ------------------------------- #
width = 200
height = 200

window = Tk()
window.title("My Password Manager")
# window.geometry(f'{width}x{height}')
window.minsize(width, height)
window.config(padx=20, pady= 20,) #bg=YELLOW

canvas = Canvas(width=width, height=height)   #bg=YELLOW, highlightthickness=0
img = PhotoImage(file='logo.png')
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
website_entry = Entry(width=50)
website_entry.focus()
# website_entry.insert(0, 'Required')
# website_entry.bind('<FocusIn>', lambda event: clear_entry(event, entry))
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')

user_entry = Entry(width=50)
user_entry.insert(0, string='flpasana@outlook.com')
user_entry.grid(column=1, row=2, columnspan=2, sticky='w')

pwd_entry = Entry(width=30)
# pwd_entry.insert(0, 'Required')
pwd_entry.grid(column=1, row=3, columnspan=2, sticky='w')

#Button
pwd_button = Button(text="Generate Password", fg='black', bg='orange', width=15,command=generate_pwd)
pwd_button.grid(column=2, row=3, sticky='w')

add_button = Button(text="Add", fg='black', bg='green',width=20, command=add_data)   #button_click
add_button.grid(column=1, row=4)

copy_button = Button(text="Copy", fg='black', bg='yellow', width=15, command=copy_to_clipboard)   #button_click
copy_button.grid(column=2, row=4, sticky='w')



window.mainloop()
