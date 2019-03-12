from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Djordje'}
    post = {'post': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'}
    return render_template('index.html', title='Home', user=user)



# Login
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# about
#
# @app.route('/about')
# def about():
#     # return redirect(url_for('about'))
#     return render_template('about.html', title='About', user='user', post='post')
