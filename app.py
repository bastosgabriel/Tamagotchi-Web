from flask import Flask
from flask_restful import Api

from db import db

from resources.tamagotchi import Tamagotchi, TamagotchiCreate
from resources.item import Item

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/bastosgabriel/code/Tamagotchi-Web/tamagotchi.db"

api = Api(app)

api.add_resource(TamagotchiCreate, '/tamagotchi')
api.add_resource(Tamagotchi, '/tamagotchi/<string:name>')

db.init_app(app)

if __name__ == '__main__':
    
    
    app.run(debug=True)