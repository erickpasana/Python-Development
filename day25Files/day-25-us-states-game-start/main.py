import turtle
import pandas as pd

map = turtle.Turtle()
screen = turtle.Screen()
screen.title('U.S. States Game')
img = "blank_states_img.gif"
screen.addshape(img)
map = turtle.Turtle()
map.shape(img)

df = pd.read_csv('50_states.csv')
states = df.state.to_list()
guessed_states = []

while len(guessed_states) < len(states):

    # print("Wrong spelling, Wrong Answer!")
    user_answer = turtle.textinput(title=f"{len(guessed_states)}/50.", prompt="Name a State. Remember, Wrong spelling, Wrong Answer!").title()
    if user_answer == 'Exit':
        to_study = df[~df['state'].isin(guessed_states)]
        to_study.to_csv('to_study.txt')
        break

    if user_answer in states:
        guessed_states.append(user_answer)
        x_coord = int(df[df.state == user_answer]['x'])
        y_coord = int(df[df.state == user_answer]['y'])
        write_state = turtle.Turtle()
        write_state.hideturtle()
        write_state.penup()
        write_state.goto(x_coord, y_coord)
        write_state.hideturtle()
        write_state.penup()
        write_state.goto(x_coord, y_coord)
        write_state.write(user_answer)
        Score = len(guessed_states)
    else:
        print("It's not.")

    # in_game = False




turtle.mainloop()




# screen.listen()
# screen.exitonclick()
# def coords(x, y):
#     print(x, y)

# turtle.onscreenclick(coords)