from tests.base_test_case import BaseTestCase

class BreweryTestCase(BaseTestCase):
    
    brewery = {'name':'Test brewery'}
    url_prefix = '/breweries'
    
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