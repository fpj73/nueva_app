"""
[Aplicación básica del microframework Flask de Python]
Author: Fortinux
Date: []
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("base.html")

@app.route("/contactos")
def contactos():
    return '<H1> contactos </H1>'

@app.route("/admin")
def admin():
    return '<H1> admin </H1>'