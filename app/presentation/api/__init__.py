from flask import Blueprint, Flask

api = Blueprint('api', __name__)

from app.presentation.api import errors, news
from app.presentation.api.config import Config

SWAGGER_UI_URL = '/docs'
SWAGGER_CONFIG_URL = '/static/swagger.json'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(api, url_prefix='/api')

    from flask_swagger_ui import get_swaggerui_blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_UI_URL, SWAGGER_CONFIG_URL)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_UI_URL)

    return app
