from flask import Flask
from flask import render_template

app = Flask(__name__)

# templates/index.html      By default, find the index.html file in the templates folder.
@app.route("/")
def root():
    return render_template("index.html")       

@app.route("/welcome")
def welcome():
    return "<p>You are welcome.</p>"

@app.route("/hello")
def hello():
    return "<p>hello world.</p>"

@app.route("/say/<word>")
def sayWord(word):
    return "<p>say " + word + " </p>"


if __name__ == "__main__":
    app.run()