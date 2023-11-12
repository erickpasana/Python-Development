
from tkinter import *


width = 600
height = 400
window = Tk()
window.title("My First GUI!!!!!!!!")
window.minsize(width, height)

#Label
my_label = Label(text="I'm a Label", font=('Arial', 30, 'bold'))
my_label.pack()
my_label.config(text='CONFIG', fg='blue', bg='red')

#Button
def button_click():
    # my_label['text'] = 'Good to GO!!!'
    my_label.config(text=search_box.get(), bg='green')
    print('Got clicked.')
my_button = Button(text="Enter", fg='black', bg='yellow', command=button_click)
my_button.pack()
# my_button.config(text='', font=('Arial', 50), fg='red', bg='green')

#Input

search_box = Entry(window)
search_box.pack(expand=True)
print(search_box.get())









window.mainloop()