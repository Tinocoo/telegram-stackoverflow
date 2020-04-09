from flask.globals import request
from flask.json import jsonify
from flask.views import MethodView

from app.inc import Telegram


class ManagerWebhook(MethodView, Telegram):

    def post(self):
        data = request.json
        return jsonify(self.setWebhook(data['url']))
