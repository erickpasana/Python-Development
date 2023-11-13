from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW_GREEN = "#d2de32"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✅"
limit = 0
count = 10

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # update(count*60)
    update(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def update(count):
    # count_time = count*60
    count_min = math.floor(count/60)
    count_sec = count % 60
    if len(str(count_min)) < 2:
        count_min = f"0{count_min}"
    if len(str(count_sec)) < 2:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_txt, text=f"{count_min}:{count_sec}")
    if count > limit:
        window.after(1000, update, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

width= 400
height= 300

window = Tk()
window.title("Pomodoro")
window.minsize(width, height)
window.config(padx=100, pady= 50, bg=YELLOW)
# window.after(1000, update)  # start the update 1 second later
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

canvas = Canvas(width=width/2, height=270, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100, 150, image=img)
canvas_txt = canvas.create_text(100, 170, font=(FONT_NAME, 30, 'bold'), fill='white', text='00:00')
canvas.grid(column=1, row= 1)

# update()

start_button = Button(text="Start", fg='black', command=start_timer)
# start_button.place(x=60, y=200)
start_button.grid(column=0, row= 2)

end_button = Button(text="Reset", fg='black',) #command=button_click   bg='orange'
end_button.grid(column=2, row= 2)

timer_label = Label(text="Pomodoro Timer", font=('Arial', 50), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row= 0)

counter_label = Label(text=checkmark, font=(20), fg=GREEN, bg=YELLOW)
counter_label.grid(column=1, row= 3)






window.mainloop()