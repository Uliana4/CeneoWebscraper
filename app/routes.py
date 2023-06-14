from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('strona_glowna.html')

@app.route('/ekstrakcja')
def index1():
    return render_template("ekstrakcja.html")

@app.route('/products')
def index2():
    return render_template("lista_produktow.html")

@app.route('/O_AUTORZE')
def index3():
    return render_template("autor.html")