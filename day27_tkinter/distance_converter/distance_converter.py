from tkinter import *


width = 200
height = 200
window = Tk()
window.title("Distance Converter")
window.minsize(width, height)
window.config(padx=100, pady=100)

#Label
input_distance = Label(text="Miles", font=('Arial', 20, 'bold'), fg='black')
# input_distance = .config(text='CONFIG', fg='black', bg='red')
input_distance.grid(row=0, column=2)

txt1 = Label(text="is equal to", font=('Arial', 20, 'bold'), fg='black')
# my_label.config(text='CONFIG', fg='black', bg='red')
txt1.grid(row=1, column=0)
# txt1.config(padx=50, pady=50)

convert_unit = Label(text="Km", font=('Arial', 20, 'bold'), fg='black')
# my_label.config(text='CONFIG', fg='black', bg='red')
convert_unit.grid(row=1, column=2)
# convert_unit.config(padx=50, pady=50)

figure = Label(text="0", font=('Arial', 20, 'bold'), fg='black')
# my_label.config(text='CONFIG', fg='blue', bg='red')
figure.grid(row=1, column=1)
# figure.config(padx=50, pady=50)

#Button
def button_click():
    # my_label['text'] = 'Good to GO!!!'
    equals = float(search_box.get()) * 1.6
    figure.config(text=equals)
    print('Got clicked.')
my_button = Button(text="Calculate", fg='black', command=button_click)
# my_button.pack()
my_button.grid(row= 2, column=1)
# my_button.config(text='', font=('Arial', 50), fg='red', bg='green')

#Input

search_box = Entry(window)
# print(search_box.get())
search_box.grid(row= 0, column=1)









window.mainloop()