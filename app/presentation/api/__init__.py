from flask import Blueprint

api = Blueprint('api', __name__)

from app.presentation.api import errors, news
