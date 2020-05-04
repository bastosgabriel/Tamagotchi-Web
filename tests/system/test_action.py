from tests.test_base import BaseTest
import json

class SystemTestAction(BaseTest):

    def test_cuddle(self):
        with self.app() as c:
            with self.app_context():
                c.post('/tamagotchi/TestName', data=dict(name='TestName'))

                response = c.post('/action/TestName', data=dict(action='cuddle'))

                self.assertEqual(response.status_code, 200)
                self.assertEqual(json.loads(response.data),
                                    {
                                    "name":  "TestName", 
                                    "love": 70, 
                                    "hunger": 0, 
                                    "hp": 100,
                                    "message": "Received some love (´｡• ᵕ •｡`)♡"
                                    }
                                )

    def test_feed(self):
        with self.app() as c:
            with self.app_context():
                c.post('/tamagotchi/TestName', data=dict(name='TestName'))

                response = c.post('/action/TestName', data=dict(action='feed'))

                self.assertEqual(response.status_code, 200)
                self.assertEqual(json.loads(response.data),
                                    {
                                    "name":  "TestName", 
                                    "love": 50, 
                                    "hunger": 0, 
                                    "hp": 100,
                                    "message": "Received some food (´｡• ᵕ •｡`)♡"
                                    }
                                )
