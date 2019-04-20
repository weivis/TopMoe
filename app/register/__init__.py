__author__ = 'Ran'

from flask import Blueprint
register = Blueprint('register', __name__)
from ..register import views