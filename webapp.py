import flask
from flask import Flask, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    title = "Dokumentasi WebApp"
    return render_template("index.html", title = title)

app.run()
