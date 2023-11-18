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
PATH = pathlib.Path(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\data\french_words.csv")
DATA = pd.read_csv(PATH)
data_dict_list2 = DATA.to_dict('records')
the_word_dict = random.choice(data_dict_list2)
to_be_translated_country = DATA.columns[0]
translation_country = DATA.columns[1]
canvas_flash_card = True

# ---------------------------- Functions ------------------------------- #
# Read the data file with pandas. Function to read and display the words...

def create_flash_card():
    global data_dict_list2, the_word_dict, canvas_flash_card, timer
    window.after_cancel(timer)
    flash_card.itemconfig(canvas_image, image=card_front_img)
    flash_card.itemconfig(canvas_txt_country, text=to_be_translated_country, fill='black')
    flash_card.itemconfig(canvas_txt_word, font=(FONT_NAME, 60, 'bold'), fill='black')
    the_word_dict = random.choice(data_dict_list2)
    to_be_translated()
    timer = window.after(3000, switch_canvas)

def to_be_translated():
    base_word = the_word_dict[to_be_translated_country]
    flash_card.itemconfig(canvas_txt_word, text=base_word)
    print(the_word_dict)
    

def switch_canvas():
    translation = the_word_dict[translation_country]
    flash_card.itemconfig(canvas_image, image=card_back_img)
    flash_card.itemconfig(canvas_txt_country, text=translation_country, fill='white')
    flash_card.itemconfig(canvas_txt_word, text=translation, fill='white')
    print(the_word_dict)
    print(translation)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)#

timer = window.after(3000, switch_canvas)

flash_card = Canvas(width=WIDTH, height=HEIGHT, ) 
card_front_img = PhotoImage(file=r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\card_front.png")
card_back_img = PhotoImage(file=r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\card_back.png")
canvas_image = flash_card.create_image(400, 263, image=card_front_img)
canvas_txt_country = flash_card.create_text(400, 150, font=(FONT_NAME, 40, 'italic'), fill='black', text=f"Today's words are {to_be_translated_country}")
canvas_txt_word = flash_card.create_text(400, 263, font=(FONT_NAME, 30, ), fill='black', text="Click any button to start")
flash_card.grid(column=0, row=0, columnspan=2)
flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#Buttoms
# cross = Button()
cross_img = ImageTk.PhotoImage(Image.open(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\wrong.png"))
cross = Button(width=50, height=50, image=cross_img, command=create_flash_card)#window
cross.grid(column=0, row=1)

# check = Button()
check_img = ImageTk.PhotoImage(Image.open(r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\right.png"))
check = Button(width=50, height=50, image=check_img, command=create_flash_card)#window
check.grid(column=1, row=1)

# job_id = window.after(3000, switch_canvas)
# window.after(1000, switch_canvas)


window.mainloop()






# def switch_canvas():
    # flash_card.pack_forget()  # Hide canvas1
    # back_card.grid(column=0, row=0, columnspan=2)  # Show canvas2
    # print(canvas_flash_card)
    # window.after(3000, switch_back)
    # flash_card.itemconfig(canvas_image, image=card_back_img)
    # flash_card.itemconfig(canvas_txt_country, text=translation_country)
    # translation()
    # flash_card.create_image(400, 263, image=card_back_img)
    # flash_card.itemconfig(canvas_txt_country,

# def switch_back():
#     back_card.pack_forget()  # Hide canvas2
#     flash_card.grid(column=0, row=0, columnspan=2)  # Show canvas1 again
    # print(canvas_flash_card)

# back_card = Canvas(width=WIDTH, height=HEIGHT, )
# card_back_img = PhotoImage(file=r"C:\Users\flpas\OneDrive - Connection Systems Development\Python-Development\day31_flash_card\flash-card-project-start\images\card_back.png")
# back_card.create_image(400, 263, image=card_back_img)
# back_card_txt_country = back_card.create_text(400, 150, font=(FONT_NAME, 40, 'italic'), fill='white', text=translation_country)
# back_card_txt_word = back_card.create_text(400, 263, font=(FONT_NAME, 30, ), fill='white', text="Click any button to start")
# # back_card.grid(column=0, row=0, columnspan=2)
# back_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)