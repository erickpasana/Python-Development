from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
WIDTH = 800
HEIGHT = 526

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
# window.geometry(f"{WIDTH}x{HEIGHT}")
window.minsize(WIDTH, HEIGHT)
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)#

flash_card = Canvas(width=WIDTH-100, height=HEIGHT-100, bg='red', highlightthickness=0)   #bg=YELLOW, width=WIDTH-100, height=HEIGHT-100, , HEIGHT-100,
img = PhotoImage(file=r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\card_front.png")
# flash_card.create_image(100, 100, image=img)
flash_card.create_image(350, 200, image=img)#350, 200
canvas_txt_country = flash_card.create_text(350, 150, font=(FONT_NAME, 20, 'italic'), fill='black', text='French')#'bold'
canvas_txt_word = flash_card.create_text(350, 263, font=(FONT_NAME, 40, 'bold'), fill='black', text='Louvre')
flash_card.grid(column=0, row= 0, columnspan=2)#,  sticky="nsew"

#Buttoms
# cross = Button()
cross_img = ImageTk.PhotoImage(Image.open(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\wrong.png"))
cross = Button(width=50, height=50, image=cross_img)#window
cross.grid(column=0, row=1)

# check = Button()
check_img = ImageTk.PhotoImage(Image.open(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\right.png"))
check = Button(width=50, height=50, image=check_img)#window
check.grid(column=1, row=1)





window.mainloop()