from tests.test_base import BaseTest
import json

class SystemTestTamagotchi(BaseTest):
    
    def test_create(self):
        with self.app() as c:
            with self.app_context():

                response = c.post('/tamagotchi/TestName', data=dict(name='TestName'))

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual(json.loads(response.data), {"message": "TestName was born! ( ͡ᵔ ͜ʖ ͡ᵔ)"})

    def test_create_duplicated(self):
        with self.app() as c:
            with self.app_context():

                c.post('/tamagotchi/TestName', data=dict(name='TestName'))
                response = c.post('/tamagotchi/TestName', data=dict(name='TestName'))

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual(json.loads(response.data), {"message": "TestName already exists! (`ー´)"})

    def test_get(self):
        with self.app() as c:
            with self.app_context():

                c.post('/tamagotchi/TestName', data=dict(name='TestName'))

                response = c.get('/tamagotchi/TestName')

                self.assertEqual(response.status_code, 200)
                self.assertEqual(json.loads(response.data),
                                    {
                                    "name":  "TestName", 
                                    "love": 50, 
                                    "hunger": 0, 
                                    "hp": 100,
                                    "message": "Such a beaultiful creature (/ =ω=)/"
                                    }
                                )

