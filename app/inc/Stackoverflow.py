from .Restful import Restful


class Stackoverflow(Restful):

    def __init__(self):
        self.restful = Restful()
        self.base_stack = 'https://api.stackexchange.com/2.2'

    def searchDiscussion(self, search):
        payload = {
            'method': 'GET',
            'url': '{}/search'.format(self.base_stack),
            'params': {
                'order':'desc',
                'sort':'activity',
                'intitle':search,
                'site':'stackoverflow'
            }
        }

        return self.restful.sendRequest(payload)
