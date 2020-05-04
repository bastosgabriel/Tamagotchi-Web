from unittest import TestCase
from app import app
from db import db

'''
This class should be parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
'''
class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls): # runs once for every Test Case
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/bastosgabriel/code/Tamagotchi-Web/tamagotchi.db"
        app.config['DEBUG'] = False
        app.config['PROPAGATE_EXCEPTIONS'] = True
        with app.app_context():
            db.init_app(app)

    '''
    Make sure database exists and get a test client
    '''
    def setUp(self): # runs once for every test method
        # make sure database exists
        with app.app_context():
            db.create_all()

        self.testing = True
        self.app = app.test_client
        self.app_context = app.app_context

    '''
    Delete database
    '''
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()