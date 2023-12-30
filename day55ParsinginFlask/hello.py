from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
    '<p>Paragraph 1</p>' \
    '<p>Paragraph 2</p>'\
    '<img src=https://media.giphy.com/media/YRVP7mapl24G6RNkwJ/giphy.gif>'

def bold(function):
    def wrapper(name):
        return f'<b><p>{function(name)}</p></b>'
    return wrapper

def italic(function):
    def wrapper(name):
        # return f'<em><b><p>{function(name)}</p></b></em>'
        return f'<em><p>{function(name)}</p></em>'
    return wrapper

def underline(function):
    def wrapper(name):
        # return f'<em><b><p>{function(name)}</p></b></em>'
        return f'<u><h2>{function(name)}</h2></u>'
    return wrapper

@app.route("/<name>")
@underline
@bold
@italic
def hello_name(name):
    return f'Hello, {name}!'

if __name__ == "__main__":
    app.run(debug=True)