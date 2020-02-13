import json

from bson import ObjectId
from bson.json_util import dumps
from flask import jsonify

from app.DAL import article_storage
from app.PL.api import api as api_bp


class JSONEncoder():
    def encode(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@api_bp.route('/news')
def get_all_news():
    data = article_storage.read()
    return jsonify(data)


@api_bp.route('/news/<int:limit>')
def get_news(limit):
    data = article_storage.read(limit)
    return jsonify(data)
