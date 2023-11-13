
from tkinter import *


width = 600
height = 400
window = Tk()
window.title("My First GUI!!!!!!!!")
window.minsize(width, height)
window.config(padx=100, pady=100)

#Label
my_label = Label(text="I'm a Label", font=('Arial', 20, 'bold'), fg='blue', bg='red')
# my_label.config(text='CONFIG', fg='blue', bg='red')
my_label.grid(row=0, column=3)

my_labe2 = Label(text="New Label", font=('Arial', 20, 'bold'), fg='blue', bg='orange')
# my_label.config(text='CONFIG', fg='blue', bg='red')
my_labe2.grid(row=4, column=2)
my_labe2.config(padx=50, pady=50)

#Button
def button_click():
    # my_label['text'] = 'Good to GO!!!'
    my_label.config(text=search_box.get(), bg='green')
    print('Got clicked.')
my_button = Button(text="Enter", fg='black', bg='orange', command=button_click)
# my_button.pack()
my_button.grid(row= 1, column=3)
# my_button.config(text='', font=('Arial', 50), fg='red', bg='green')

#Input

search_box = Entry(window)
print(search_box.get())
search_box.grid(row= 2, column=3)









window.mainloop()