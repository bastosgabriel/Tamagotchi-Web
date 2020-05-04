from tests.unit.test_unit_base import UnitBaseTest
from models.tamagotchi import TamagotchiModel

class UnitTestTamagotchi(UnitBaseTest):

    def test_create(self):
        tamagotchi = TamagotchiModel("TestName")
        
        self.assertEqual(tamagotchi.name, "TestName")
        self.assertEqual(tamagotchi.love, 50)
        self.assertEqual(tamagotchi.hunger, 0)
        self.assertEqual(tamagotchi.hp, 100)


    def test_json(self):
        tamagotchi = TamagotchiModel("TestName")

        expected_json = {
            "name": tamagotchi.name, 
            "love": tamagotchi.love, 
            "hunger": tamagotchi.hunger, 
            "hp": tamagotchi.hp,
            "message": "Test message"
        }

        self.assertEqual(tamagotchi.json("Test message"), expected_json)

