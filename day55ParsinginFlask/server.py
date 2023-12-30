from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def head():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
    "<img style='text-align: center' src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"\
    "<form action='/guess' method='post'>" \
    "<input type='number' name='number' min='0' max='9'>" \
    "<button type='submit'>Submit</button>" \
    "</form>"

@app.route('/guess', methods=['POST'])
def guess():
    number = int(request.form['number']) # Get the user's input
    answer = random.randint(0, 9) # Generate a random number
    if number == answer: # Compare the user's input with the random number
        return "<h1 style='text-align: center'>You guessed right!</h1>" \
        "<img style='text-align: center' src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"
    else:
        return f"<h1 style='text-align: center'>You guessed wrong. The answer was {answer}.</h1>" \
        "<img style='text-align: center' src=https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif>"


if __name__ == '__main__':
    app.run(debug=True)