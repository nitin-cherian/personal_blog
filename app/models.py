"""
models.py - The structure of all database tables are defined here.

"""
from datetime import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    bookmarks = db.relationship('Bookmark', backref='author', lazy='dynamic')

    def __repr__(self):
        return "<User {}>".format(self.username)


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_url = db.Column(db.String(256), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Bookmark {}>".format(self.post_url)
