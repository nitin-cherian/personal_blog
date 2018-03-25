"""
routes.py - All the view functions are defined here.

"""
from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def home():
    posts = [
        {
            'header': 'First Blog Post',
            'body': 'This is my first blog post',
            'comments': [
                {
                    'author': 'John',
                    'body': 'Very good article!'
                },
                {
                    'author': 'Susan',
                    'body': 'Nicely written'
                }
            ]
        },
        {
            'header': 'Second Blog Post',
            'body': 'This is my second blog post',
            'comments': [
                {
                    'author': 'Alex',
                    'body': 'This is an excellent tutorial. Thanks'
                },
                {
                    'author': 'David',
                    'body': 'Short and Succinct.'
                }
            ]
        }
    ]

    return render_template('home.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)
