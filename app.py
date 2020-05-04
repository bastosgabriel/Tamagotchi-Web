from flask import Flask
from flask_restful import Api

from resources.tamagotchi import Tamagotchi
from resources.action import Action

from models.tamagotchi import TamagotchiModel

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/bastosgabriel/code/Tamagotchi-Web/tamagotchi.db"

api = Api(app)

api.add_resource(Tamagotchi, '/tamagotchi/<string:name>')
api.add_resource(Action, '/action/<string:name>')



if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(debug=True)