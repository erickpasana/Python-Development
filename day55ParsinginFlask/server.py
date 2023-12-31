from flask import Flask, request, session
import random
import os

random_number = random.randint(0, 9)
total_guesses = 0
app = Flask(__name__)
app.secret_key = os.urandom(6)
print(random_number)
print(app.secret_key)
app = Flask(__name__)

# x----------------------- Solution -----------------------x

@app.route('/')
def home():
    # store the random number in the session
    session["random_number"] = random.randint(0, 9)
    # store the number of guesses in the session
    session["total_guesses"] = 0
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if session["total_guesses"] < 2:
        if guess > session["random_number"]:
            session["total_guesses"] += 1
            return "<h1 style='color: purple'>Too high, try again!</h1>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"\
                f'<h3>Number: {session["random_number"]}  Tries: {session["total_guesses"]}</h3>'
            
        elif guess < session["random_number"]:
            session["total_guesses"] + 1
            return "<h1 style='color: red'>Too low, try again!</h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"\
                f'<h3>Number: {session["random_number"]}  Tries: {session["total_guesses"]}</h3>'
        else:
            return "<h1 style='color: green'>You found me!</h1>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    # else:

    
# x------------------------- Bing -------------------------x

# @app.route('/')
# def head():
#     return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
#     "<img style='text-align: center' src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"\
#     "<form action='/guess' method='post'>" \
#         "<input type='number' name='number' min='0' max='9'>" \
#         "<button type='submit'>Submit</button>" \
#     "</form>"

# @app.route('/guess', methods=['POST'])
# def guess():
#     number = int(request.form['number']) # Get the user's input
#     answer = random.randint(0, 9) # Generate a random number
#     if number == answer: # Compare the user's input with the random number
#         return "<h1 style='text-align: center'>You guessed right!</h1>" \
#         "<img style='text-align: center' src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"
#     else:
#         return f"<h1 style='text-align: center'>You guessed wrong. The answer was {answer}.</h1>" \
#         "<img style='text-align: center' src=https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif>"


if __name__ == '__main__':
    app.run(debug=True)