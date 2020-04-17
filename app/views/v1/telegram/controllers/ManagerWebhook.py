from flask.globals import request
from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse

from app.inc import Telegram


class ManagerWebhook(MethodView, Telegram):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url')
        data = parser.parse_args()
        
        return jsonify(self.setWebhook(data['url']))
