import flask
from flask import Flask, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    title = "Beranda WebApp"
    return render_template("index.html", title = title)

@app.route('/dokumentasi')
def dokumentasi():
    title = "Dokumentasi WebApp"
    return render_template("dokumentasi.html", title=title)

app.run()
