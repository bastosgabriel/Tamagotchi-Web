from flask_sqlalchemy import SQLAlchemy
from db import db

class TamagotchiModel(db.Model):
    __tablename__ = 'tamagotchis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    love = db.Column(db.Integer)
    hunger = db.Column(db.Integer)
    hp = db.Column(db.Integer)


    def __init__(self, name):
        self.name = name
        self.love = 50
        self.hunger = 0
        self.hp = 100

    '''
    Returns tamagotchi attributes in json format
    '''
    def json(self, message=""):
        return {"name": self.name, 
                "love": self.love, 
                "hunger": self.hunger, 
                "hp": self.hp,
                "message": message
                }

    '''
    Search for a tamagotchi with the given name on the database
    '''
    @staticmethod
    def find_by_name(name):
        return TamagotchiModel.query.filter_by(name=name).first()
        

    '''
    Saves model to db
    '''
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    '''
    Increases tamagotchi's love bar on the database
    '''
    def cuddle(self):
        self.love += 20


    '''
    Decreases the hunger bar
    '''
    @staticmethod
    def feed(name):
        pass



    