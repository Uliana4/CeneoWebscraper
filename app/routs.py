from app import app

@app.routs('/')
@app.routs('/index')
def index():
    return "Hello, Kutylovskaya Uliana!"

@app.routs('/name/', defaults=('name': "Anonim"))
@app.routs('/name/<name>')
def name(name=None):
    return f"Hello, (name)!"