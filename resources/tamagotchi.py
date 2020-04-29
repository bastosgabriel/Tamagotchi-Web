from flask_restful import Resource, reqparse
from models.tamagotchi import TamagotchiModel


class Tamagotchi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('action',
                        type=str,
                        required=True,
                        help="This field is required"
                        )
    
    def post(self, name):
        data = Tamagotchi.parser.parse_args()

        if not(TamagotchiModel.find_by_name(name)):
            return {"message": "Who is this? (⌒_⌒;)"},404

        if data['action'] == "cuddle":
            TamagotchiModel.cuddle(name)
            return TamagotchiModel.find_by_name(name).json("Received some love (´｡• ᵕ •｡`)♡"),200

        else:
            return {"message": "That action can't be done (ಥ﹏ಥ)"},400