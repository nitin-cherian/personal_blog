"""
personal_blog.py - Used to trigger the application
"""

from app import app, db
from app.models import User, Bookmark


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Bookmark': Bookmark
    }
