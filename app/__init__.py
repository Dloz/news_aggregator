from flask import Flask
from app.PL.api import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    #config.init_app(app)

    from app.PL.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
