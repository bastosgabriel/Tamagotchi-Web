from flask_restful import Resource, reqparse
from models.tamagotchi import TamagotchiModel


class Action(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('action',
                        type=str,
                        required=True,
                        help="This field is required"
                        )

    def post(self, name):
        data = Action.parser.parse_args()

        if not(TamagotchiModel.find_by_name(name)):
            return {"message": "Who is this? (⌒_⌒;)"},404
        else:
            tamagotchi = TamagotchiModel.find_by_name(name)


        if data['action'] == "cuddle":
            tamagotchi.cuddle()
            tamagotchi.save_to_db()
            return TamagotchiModel.find_by_name(name).json("Received some love (´｡• ᵕ •｡`)♡"), 200
        
        elif data['action'] == "feed":
            tamagotchi.feed()
            tamagotchi.save_to_db()
            return TamagotchiModel.find_by_name(name).json("Received some food (´｡• ᵕ •｡`)♡"), 200

        else:
            return {"message": "That action can't be done (ಥ﹏ಥ)"},400