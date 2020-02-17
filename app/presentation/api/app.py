from flask_swagger import swagger
from app.presentation.api import SWAGGER_CONFIG_URL, SWAGGER_UI_URL
from api import app


@app.route(SWAGGER_UI_URL)
def docs():
    config = swagger(app)
    config['info']['description'] = "REST API Service to extract news data"
    config['info']['version'] = "2.0"
    config['info']['title'] = "News aggregator API"
    return config
