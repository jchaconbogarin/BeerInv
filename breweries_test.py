import unittest 
import os 
import json
from config import TestingConfig
from app import initApp, db

class BreweryTestCase(unittest.TestCase):
    
    def setUp(self):
        
        self.app = initApp(TestingConfig)
        self.client = self.app.test_client
        self.brewery = {'name':'Test brewery'}
        
        with self.app.app_context():
            db.create_all()
            
    def test_brewery_create(self):
        
        response = self.client().post('/breweries', data=self.brewery)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test brewery', str(response.data)) 
        
    def test_api_can_get_all_breweries(self):
        
        response = self.client().post('/breweries', data=self.brewery)
        self.assertEqual(response.status_code, 201)
        response = self.client().get('/breweries')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test brewery', str(response.data))
        
    def test_brewery_can_be_updated(self):
        
        response = self.client().post('/breweries', data={'name':'3 cordiras'})
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/breweries/1', data={'name':'3 Cordilleras'})
        self.assertEqual(response.status_code, 200)
        results = self.client().get('/breweries/1')
        self.assertIn('3 Cordilleras', str(results.data))
        
    def test_brewery_can_be_deleted(self):
        
        response = self.client().post('/breweries', data={'name':'Cervecería Errónea'})
        self.assertEqual(response.status_code, 201)
        response = self.client().delete('/breweries/1')
        self.assertEqual(response.status_code, 200)
        result = self.client().get('breweries/1')
        self.assertEqual(result.status_code, 404)
        
    def tearDown(self):
        
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            
if __name__ == '__main__':
    unittest.main()
    