import unittest 
import os 
import json
from beerinv import initApp, db
from config import TestingConfig

class BreweryTestCase(unittest.TestCase):
    
    def setUp(self):
        
        self.app = initApp(TestingConfig)
        self.client = self.app.test_client
        self.brewery = {'name':'Test brewery'}
        self.url_prefix = '/breweries'
        
        with self.app.app_context():
            db.create_all()
            
    """ Happy path """
            
    def test_brewery_create(self):
        
        response = self.client().post(self.url_prefix, data=self.brewery)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test brewery', str(response.data)) 
        
    def test_api_can_get_all_breweries(self):
        
        response = self.client().post(self.url_prefix, data=self.brewery)
        self.assertEqual(response.status_code, 201)
        response = self.client().get(self.url_prefix)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test brewery', str(response.data))
        
    def test_brewery_can_be_updated(self):
        
        response = self.client().post(self.url_prefix, data={'name':'3 cordiras'})
        self.assertEqual(response.status_code, 201)
        response = self.client().put(self.url_prefix + '/1', data={'name':'3 Cordilleras'})
        self.assertEqual(response.status_code, 200)
        results = self.client().get(self.url_prefix + '/1')
        self.assertIn('3 Cordilleras', str(results.data))
        
    def test_brewery_can_be_deleted(self):
        
        response = self.client().post(self.url_prefix, data={'name':'Cerveceria Erronea'})
        self.assertEqual(response.status_code, 201)
        response = self.client().delete(self.url_prefix + '/1')
        self.assertEqual(response.status_code, 200)
        result = self.client().get(self.url_prefix + '/1')
        self.assertEqual(result.status_code, 404)
        
    """ Errors expected """
        
    def test_brewery_create_empty_name(self):
        
        self.brewery = {  }
        response = self.client().post(self.url_prefix, data=self.brewery)
        self.assertEqual(response.status_code, 400)
        self.assertIn('This field is required.', str(response.data))
        
        
    def tearDown(self):
        
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            
if __name__ == '__main__':
    unittest.main()
    