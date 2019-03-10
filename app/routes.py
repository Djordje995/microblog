from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Djordje'}
    posts = [
        {
            'author': {'username': 'Nikola'},
            'body': 'Lep dan danas!'
        },
        {
            'author': {'username': 'Andjela '},
            'body': 'Ljubavi nema te ceo dan! ' 
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
