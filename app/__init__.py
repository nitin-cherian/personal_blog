"""
__init__.py:  Exposes names that will be globally available to the application.

"""

from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


from app import routes