from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
width = 200
height = 200

window = Tk()
window.title("My Password Manager")
# window.geometry(f'{width}x{height}')
window.minsize(width, height)
window.config(padx = 20, pady = 20)
window.config(padx=20, pady= 20,) #bg=YELLOW

# canvas = Canvas(window)
# canvas.create_image(img)
canvas = Canvas(width=width, height=height)   #bg=YELLOW, highlightthickness=0
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
# canvas_txt = canvas.create_text(100, 150, font=(FONT_NAME, 30, 'bold'), fill='white', text='00:00')
canvas.pack()
# canvas.grid(column=0, row= 1)




window.mainloop()
