from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
    '<p>Paragraph 1</p>' \
    '<p>Paragraph 2</p>'\
    '<img src=https://media.giphy.com/media/YRVP7mapl24G6RNkwJ/giphy.gif>'

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)