from flask import Blueprint

rsc = Blueprint('rsc', __name__)
from . import views, errors
