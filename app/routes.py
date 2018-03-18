"""
routes.py - All the view functions are defined here.

"""
from flask import render_template

from app import app


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

