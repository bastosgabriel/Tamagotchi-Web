from unittest import TestCase
from app import app
import json

class TestTamagotchi(TestCase):
    
    def test_tamagotchi_create(self):
        with app.test_client() as c:
            response = c.post('/tamagotchi', data=dict(name='TestName'))

            self.assertEqual(response.status_code, 201)
    
    def test_get_tamagotchi(self):
        with app.test_client() as c:
            response = c.get('/tamagotchi/TestName')

            self.assertEqual(response.status_code, 200)
            # self.assertEqual(json.loads(response.get_data()),
            #                     {
            #                     "name":  "TestName", 
            #                     "love": self.love, 
            #                     "hunger": self.hunger, 
            #                     "hp": self.hp,
            #                     "message": "message"
            #                     }
            #                 )

    def test_post_action(self):
        with app.test_client() as c:
            response = c.post('/tamagotchi/TestName', data=dict(action='cuddle'))

            self.assertEqual(response.status_code, 200)

