from tests.unit.test_unit_base import UnitBaseTest
from models.tamagotchi import TamagotchiModel

class UnitTestAction(UnitBaseTest):
     
    def test_cuddle(self):
        tamagotchi = TamagotchiModel("TestName")
        
        old_love = tamagotchi.love

        tamagotchi.cuddle()

        if tamagotchi.love == 100:
            self.assertGreaterEqual(tamagotchi.love, old_love)
        else:
            self.assertGreater(tamagotchi.love, old_love)

    def test_feed(self):
        tamagotchi = TamagotchiModel("TestName")
        
        old_hunger = tamagotchi.hunger

        tamagotchi.feed()

        if tamagotchi.hunger == 0:
            self.assertLessEqual(tamagotchi.hunger, old_hunger)
        else:
            self.assertLess(tamagotchi.hunger, old_hunger)
        

        
