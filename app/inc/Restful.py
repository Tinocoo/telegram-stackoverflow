import json
import requests


class Restful(object):

    def sendRequest(self, payload):
        try:
            res = requests.request(**payload)
            status = 'success'
            msg = 'ok'
            if res.ok is False:
                status = 'fail'
                msg = 'error'
            return {'status': status, 'msg': msg, 'data': json.loads(res.text)} 
        except Exception as error:
            return {'status': 'error', 'msg': str(error), 'data': []}
