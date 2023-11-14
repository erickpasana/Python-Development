from tkinter import *
from tkinter import messagebox
from time import sleep
import sys
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW_GREEN = "#9FBB73"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✅"
limit = 0
count_5 = 5
REPS = 0
min_W = 7
short_B = 3
long_B = 5
current_timed = 'Work'
count = min_W
stop = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    # if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #     window.destroy()  # replace 'window' with the name of your Tkinter root window
    #     sys.exit()
    global REPS, count, short_B, long_B, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, current_timed
    REPS = 0
    counter_label.config(text=f"Work Reps= {REPS}/4")
    current_timed = 'W'
    WSL_label.config(text=f"Current Timed= {current_timed}")
    count = min_W
    stop = FALSE
    canvas.itemconfig(canvas_txt, text="00:00")
    # update(count)

def stop_countdown():
    global stop
    # window.after_cancel(id)
    stop = True

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global count
    # update(count*60)
    update(count)
def add_REPS():
    global REPS, count, short_B, long_B, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, current_timed
    # REPS += 1
    if not stop:
        if REPS < 3:
            if current_timed == 'Work':
                # if REPS < 4:
                current_timed = 'Short Break'
                count = short_B
                # elif REPS == 4:
                #     current_timed = 'L'
                #     count = short_B
                REPS += 1
                # window.after(1000, add_REPS)
            elif current_timed == 'Short Break':
                current_timed = 'Work'
                count = min_W
                # window.after(1000, add_REPS)
            elif current_timed == 'Long Break':
                current_timed = 'Work'
                count = min_W
        if REPS == 3:
            REPS = 0
            current_timed = 'Long Break'
            count = long_B
            # window.after(1000, add_REPS)
        counter_label.config(text=f"Work Reps= {REPS}/4")
        WSL_label.config(text=f"Current Timed= {current_timed}")
        update(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def update(count):
    global REPS, short_B, long_B, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, current_timed, stop
    count_min = math.floor(count/60)
    count_sec = count % 60
    if not stop:
        if len(str(count_min)) < 2:
            count_min = f"0{count_min}"
        if len(str(count_sec)) < 2:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(canvas_txt, text=f"{count_min}:{count_sec}")
        if count > limit:
            window.after(1000, update, count - 1)
        elif count == limit:
            canvas.itemconfig(canvas_txt, text=f"{count_min}:{count_sec}")
            window.after(1000, add_REPS)
    else:
        stop = False


# ---------------------------- UI SETUP ------------------------------- #

width= 400
height= 300

window = Tk()
window.title("Pomodoro")
window.minsize(width, height)
window.config(padx=80, pady= 20, bg=YELLOW)
# window.after(1000, update)  # start the update 1 second later
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

canvas = Canvas(width=width/2, height=250, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100, 130, image=img)
canvas_txt = canvas.create_text(100, 150, font=(FONT_NAME, 30, 'bold'), fill='white', text='00:00')
canvas.grid(column=1, row= 1)

# update()

start_button = Button(text="Start", fg='black', command=start_timer)
# start_button.place(x=60, y=200)
start_button.grid(column=0, row= 2)

stop_button = Button(window, text="Stop", fg='black', command=stop_countdown) #   bg='orange'
stop_button.grid(column=1, row= 2)

reset_button = Button(window, text="Reset", fg='black', command=reset) #   bg='orange'
reset_button.grid(column=2, row= 2)

timer_label = Label(text="Pomodoro Timer", font=('Arial', 50), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row= 0)

counter_label = Label(text=f"Work Reps= {REPS}/4", font=(20), fg='black', bg=YELLOW)
counter_label.grid(column=0, row= 1)

WSL_label = Label(text=f"Current Timed= {current_timed}", font=(20), fg='black', bg=YELLOW)
WSL_label.grid(column=2, row= 1)






window.mainloop()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# def update(count):
#     # count_time = count*60
#     count_min = math.floor(count/60)
#     count_sec = count % 60
#     if len(str(count_min)) < 2:
#         count_min = f"0{count_min}"
#     if len(str(count_sec)) < 2:
#         count_sec = f"0{count_sec}"
#     canvas.itemconfig(canvas_txt, text=f"{count_min}:{count_sec}")
#     if count > limit:
#         window.after(1000, update, count - 1)