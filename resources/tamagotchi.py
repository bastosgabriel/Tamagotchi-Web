from flask_restful import Resource, reqparse
from models.tamagotchi import TamagotchiModel

class TamagotchiCreate(Resource):

    tamagotchi_parser = reqparse.RequestParser()
    tamagotchi_parser.add_argument('name',
                            type=str,
                            required=True,
                            help="This field is required"
                            )
        
    def post(self):
        data = TamagotchiCreate.tamagotchi_parser.parse_args()
        tamagotchi = TamagotchiModel(**data)

        if TamagotchiModel.find_by_name(tamagotchi['name']):
            return {"message": f"{tamagotchi['name']} already exists! (`ー´)"}, 400

        try:
            tamagotchi.save_to_db()
        except Exception as err:
            return {"message": "Something bad happened trying to save model to db ( ͠° ͟ʖ ͡°)"}, 500

        return {"message": f"{tamagotchi['name']} was born! ( ͡ᵔ ͜ʖ ͡ᵔ)"}, 201



class Tamagotchi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('action',
                        type=str,
                        required=True,
                        help="This field is required"
                        )

    def get(self, name):
        if TamagotchiModel.find_by_name(name):
            return {TamagotchiModel.find_by_name(name).json("Such a beaultiful creature (/ =ω=)/")}

    def post(self, name):
        data = Tamagotchi.parser.parse_args()

        if not(TamagotchiModel.find_by_name(name)):
            return {"message": "Who is this? (⌒_⌒;)"},404

        if data['action'] == "cuddle":
            TamagotchiModel.cuddle(name)
            return TamagotchiModel.find_by_name(name).json("Received some love (´｡• ᵕ •｡`)♡"),200

        else:
            return {"message": "That action can't be done (ಥ﹏ಥ)"},400