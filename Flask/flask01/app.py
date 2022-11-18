from flask import Flask
from flask import render_template
from markupsafe import escape
import time

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

@app.route("/date")
def date():
    return time.strftime("%Y-%m-%d %H:%M:%S")

@app.route("/say/<word>")
def sayWord(word):
    # return "<p>say " + word + " </p>"
    return f"<p>say {escape(word)} </p>"


if __name__ == "__main__":
    app.run()