"""
__init__.py:  Exposes names that will be globally available to the application.

"""

from flask import Flask


app = Flask(__name__)


from app import routes