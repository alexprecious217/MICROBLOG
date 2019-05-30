from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Allisona'}
    posts = [
        {
            'author': {'username': 'Alex'},
            'body': 'Why dya guys eat too much?'
        },
        {
            'author': {'username': 'Precious'},
            'body': 'I blah blah blah blah blah'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user{}, REMEMBER_ME'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

