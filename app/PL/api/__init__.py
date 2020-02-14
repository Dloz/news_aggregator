from flask import Blueprint

api = Blueprint('api', __name__)

from app.PL.api import errors, news
