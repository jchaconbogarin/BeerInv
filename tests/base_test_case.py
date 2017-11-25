import unittest 
from beerinv import initApp, db
from config import TestingConfig

class BaseTestCase(unittest.TestCase):
    
    def setUp(self):
        
        self.app = initApp(TestingConfig)
        self.client = self.app.test_client
        
        with self.app.app_context():
            db.create_all()
            
    def tearDown(self):
        
        with self.app.app_context():
            db.session.remove()
            db.drop_all()