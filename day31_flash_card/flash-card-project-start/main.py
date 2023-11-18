from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd
import random
import pathlib

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
WIDTH = 800
HEIGHT = 526
path = pathlib.Path(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\data\french_words.csv")
data = pd.read_csv(path)
data_dict_list2 = data.to_dict('records')


# ---------------------------- Functions ------------------------------- #
# Read the data file with pandas. Function to read and display the words...
def index():
    return random.randint(0, len(data_dict_list2)-1)

def create_flash_card():
    to_be_translated()

def to_be_translated():
    data_dict_list = data.to_dict()
    base_words = data_dict_list['French']
    base_word = data_dict_list2[index()]['French']
    flash_card.itemconfig(canvas_txt_word, text=base_word)
    print(index())
    print(data_dict_list2[index()])
    print(translation())

def translation():
    # data = pd.read_csv(path)
    # data_dict = {row.French: row.English for (index, row) in data.iterrows()}
    translation = data_dict_list2[index()]['English']
    print(translation)
    # print(index())
    # print(data_dict_list2[index()])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
# window.geometry(f"{WIDTH}x{HEIGHT}")
# window.minsize(WIDTH, HEIGHT)
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)#

flash_card = Canvas(width=WIDTH, height=HEIGHT, ) #bg='red',  #, width=WIDTH-100, height=HEIGHT-100, , HEIGHT-100,
card_front_img = PhotoImage(file=r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\card_front.png")
flash_card.create_image(400, 263, image=card_front_img)#350, 200
canvas_txt_country = flash_card.create_text(400, 150, font=(FONT_NAME, 40, 'italic'), fill='black', text='French')#'bold'
canvas_txt_word = flash_card.create_text(400, 263, font=(FONT_NAME, 60, 'bold'), fill='black', text='Word')#canvas_txt_word
flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.grid(column=0, row= 0, columnspan=2)#,  sticky="nsew" 

#Buttoms
# cross = Button()
cross_img = ImageTk.PhotoImage(Image.open(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\wrong.png"))
cross = Button(width=50, height=50, image=cross_img, command=create_flash_card)#window
cross.grid(column=0, row=1)

# check = Button()
check_img = ImageTk.PhotoImage(Image.open(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\right.png"))
check = Button(width=50, height=50, image=check_img, command=create_flash_card)#window
check.grid(column=1, row=1)





window.mainloop()