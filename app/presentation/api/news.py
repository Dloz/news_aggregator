import dateutil.parser
from flask import jsonify, request

from app.data_access import article_storage
from app.presentation.api import api as api_bp
from app.presentation.api.errors import bad_request


@api_bp.route('/news')
@api_bp.route('/news/<string:site>')
def get_news(site=None):
    from api import app
    page_size = app.config["NEWS_PER_PAGE"]
    from_param = request.args.get('from')
    to_param = request.args.get('to')
    page = request.args.get('p')
    if page:
        try:
            page = int(page)
        except ValueError:
            return bad_request("Page parameter is in wrong format. Check if it is a number.")
    from_date = None
    to_date = None
    if from_param:
        from_date = dateutil.parser.parse(from_param)
        if to_param:
            to_date = dateutil.parser.parse(to_param)
    data = article_storage.read(from_date=from_date, to_date=to_date, page=page, page_size=page_size, site=site)
    if not data:
        return list()
    return jsonify(data)
