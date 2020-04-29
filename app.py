from flask import Flask
from flask_restful import Api

from resources.tamagotchi import Tamagotchi, TamagotchiAction
from resources.item import Item


app = Flask(__name__)

api = Api(app)


api.add_resource(Tamagotchi, '/tamagotchi/<string:name>')
api.add_resource(Item, '/item/<string:name>')