from flask.globals import request
from flask.views import MethodView

from app.inc import Telegram, Stackoverflow


class ManagerTelegram(MethodView, Telegram):

    def post(self):
        telegram_msg = request.json

        if telegram_msg['message']['text'] == '/start':
            return 'ok', 200

        stack = Stackoverflow()
        response_stackoverflow = stack.searchDiscussion(telegram_msg['message']['text'])
        answered = [i for i in response_stackoverflow['data']['items'] if i['is_answered'] is True][0]
        msg = 'title: {}\n\nlink: {}'.format(answered['title'], answered['link'])
        payload = {
            'chat_id':telegram_msg['message']['chat']['id'],
            'text': msg,
        }
        self.sendMessenge(payload)
        return 'ok', 200