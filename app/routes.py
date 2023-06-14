from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('strona_glowna.html')

@app.route('/ekstrakcja')
def extract():
    return render_template("ekstrakcja.html")

@app.route('/products')
def products():
    return render_template("lista_produktow.html")

@app.route('/product')
def product():
    return render_template("96685108.html")

@app.route('/O_AUTORZE')
def autor():
    return render_template("autor.html")