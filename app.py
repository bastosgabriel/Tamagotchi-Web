from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.tamagotchi import Tamagotchi, TamagotchiCreate
from resources.item import Item

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tamagotchi.db"

api = Api(app)

api.add_resource(TamagotchiCreate, '/tamagotchi')
api.add_resource(Tamagotchi, '/tamagotchi/<string:name>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)