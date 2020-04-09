from .Restful import Restful


class Telegram(Restful):

    def __init__(self):
        self.restful = Restful()
        token = '836730623:AAEoowkDezTME-NoZGanmrChHo7ZGMSM5ek'
        self.base_url = 'https://api.telegram.org/bot{}'.format(token)

    def sendMessenge(self, params):
        payload = {
            'method': 'POST',
            'url': '{}/sendMessage'.format(self.base_url),
            'data': {
                'chat_id':params['chat_id'],
                'text':params['text'],
                'parse_mode':'html'
            }
        }

        return self.restful.sendRequest(payload)

    def setWebhook(self, url):
        payload = {
            'method': 'POST',
            'url': '{}/setWebhook'.format(self.base_url),
            'data': {
                'url': url
            }
        }

        return self.restful.sendRequest(payload)
