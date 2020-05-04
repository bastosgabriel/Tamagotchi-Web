from flask_restful import Resource, reqparse
from models.tamagotchi import TamagotchiModel

class Tamagotchi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                            type=str,
                            required=True,
                            help="This field is required"
                            )
    
    def get(self, name):
        if TamagotchiModel.find_by_name(name):
            return TamagotchiModel.find_by_name(name).json("Such a beaultiful creature (/ =ω=)/"), 200
        else:
            return {"message": "Who is this? (⌒_⌒;)"},404

    def post(self, name):
        data = Tamagotchi.parser.parse_args()
        tamagotchi = TamagotchiModel(**data)

        try:
            if TamagotchiModel.find_by_name(name):
                return {"message": f"{name} already exists! (`ー´)"}, 400
        except Exception as err:
            return {"message": f"Something bad happened trying to find this little pet on db ( ͠° ͟ʖ ͡°) - {err}"}, 500


        try:
            tamagotchi.save_to_db()
        except Exception as err:
            return {"message": "Something bad happened trying to save model to db ( ͠° ͟ʖ ͡°)"}, 500

        return {"message": f"{name} was born! ( ͡ᵔ ͜ʖ ͡ᵔ)"}, 201