from flask import Blueprint

api = Blueprint('endpoint',__name__,template_folder='templates')

from . import endpoint 