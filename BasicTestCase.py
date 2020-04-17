import json
import unittest

from app import create_app


class BasicTestCase(unittest.TestCase):
    
    
    app = create_app()
    
    def testIndex(self):
        tester = self.app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 404)
    

    def testWebhook(self):
        tester = self.app.test_client(self)
        data = dict(
            url='https://d3cb5f61.ngrok.io/v1/telegram/msg'
        )
        res = tester.post('/v1/telegram/webhook', json=data, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('data',json.loads(res.data))


    def testChatIntegration(self):
        tester = self.app.test_client(self)
        data = {
            'update_id': '12341864516548',
            'message': {
                'message_id': 71, 
                'from': {
                    'id': 473277158, 
                    'is_bot': False, 
                    'first_name': 'Paulo', 
                    'last_name': 'Tinoco', 
                    'username': 'paulotinoco', 
                    'language_code': 'pt-br'
                }, 
                'chat': {
                    'id': 473277158, 
                    'first_name': 'Paulo', 
                    'last_name': 'Tinoco', 
                    'username': 'paulotinoco', 
                    'type': 'private'
                }, 
                'date': 1587115925, 
                'text': 'blip'
            }
        }
        res = tester.post('/v1/telegram/msg', json=data, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('',str(res.data))


if __name__ == "__main__":
    unittest.main()
