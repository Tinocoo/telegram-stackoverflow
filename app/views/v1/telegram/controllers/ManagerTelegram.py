from flask.globals import request
from flask.views import MethodView
from flask_restful import reqparse

from app.inc import Telegram, Stackoverflow


class ManagerTelegram(MethodView, Telegram):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('update_id')
        parser.add_argument('message', type=dict)
        telegram_msg = parser.parse_args()
        
        if telegram_msg['message']['text'] == '/start':
            return 'ok', 200

        stack = Stackoverflow()
        response_stackoverflow = stack.searchDiscussion(telegram_msg['message']['text'].lower())
        responses = response_stackoverflow['data']['items']
        msg = 'your search returned no results'
        if len(responses) > 0:
            answered = [i for i in responses if i['is_answered'] is True][0]
            msg = 'Title: {}\n\Link: {}'.format(answered['title'], answered['link'])

        payload = {
            'chat_id':telegram_msg['message']['chat']['id'],
            'text': msg,
        }
        self.sendMessenge(payload)
        return 'ok', 200