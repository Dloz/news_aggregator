from flask import jsonify, request
import dateutil.parser
from app.DAL import article_storage
from app.PL.api import api as api_bp
from app.PL.api.errors import bad_request


@api_bp.route('/news')
@api_bp.route('/news/<int:page>')
def get_news(page=None):
    from_param = request.args.get('from')
    to_param = request.args.get('to')
    from_date = None
    to_date = None
    if from_param:
        from_date = dateutil.parser.parse(from_param)
        if to_param:
            to_date = dateutil.parser.parse(to_param)
        else:
            pass
    if page:
        data = article_storage.pagination(page)
    else:
        data = article_storage.read(from_date=from_date, to_date=to_date)
    if not data:
        return bad_request("No data")
    return jsonify(data)
