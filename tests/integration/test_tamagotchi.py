from tests.test_base import BaseTest
from models.tamagotchi import TamagotchiModel

class IntegrationTestTamagotchi(BaseTest):

    def test_create(self):
        with self.app_context():
            tamagotchi = TamagotchiModel("Test Name")

            self.assertIsNone(tamagotchi.find_by_name(tamagotchi.name), 
                              f"{tamagotchi.name} already exists in the database")

            tamagotchi.save_to_db()
            self.assertIsNotNone(tamagotchi.find_by_name(tamagotchi.name), 
                                 f"{tamagotchi.name} was not found in the database")

    def test_delete(self):
            with self.app_context():
                tamagotchi = TamagotchiModel("Test Name")

                self.assertIsNone(tamagotchi.find_by_name(tamagotchi.name), 
                                f"{tamagotchi.name} already exists in the database")

                tamagotchi.save_to_db()
                self.assertIsNotNone(tamagotchi.find_by_name(tamagotchi.name), 
                                    f"{tamagotchi.name} was not found in the database")

                tamagotchi.delete_from_db()
                self.assertIsNone(tamagotchi.find_by_name(tamagotchi.name), 
                                f"{tamagotchi.name} still exists in the database")