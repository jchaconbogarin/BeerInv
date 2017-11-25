
from flask_restful import Resource, Api, reqparse, abort

from beerinv.controllers.base_resource import BaseResource
from beerinv.models.brewery import Brewery



class BreweryBaseResource(BaseResource):
    
    def __init__(self):
        self.klass = Brewery
        
    @property
    def arguments(self):
        return [
            { 'field_name':'name', 'required':True, 'type':str, 'help':'This field is required.' }
        ]   
    
class BreweryResource(BreweryBaseResource):
    
    def put(self, brewery_id):
        args = self.parse_args()
        brewery = self.get_single(brewery_id)
        brewery.name = args['name']
        brewery.save()
        return self.return_single(brewery, 200)
    
    def delete(self, brewery_id):
        brewery = self.get_single(brewery_id)
        brewery.delete()
        return self.return_all()
    
    def get(self, brewery_id):
        brewery = self.get_single(brewery_id)
        return self.return_single(brewery, 200)

class BreweryList(BreweryBaseResource):
    
    def get(self):
        return self.return_all()
    
    def post(self):
        args = self.parse_args()
        brewery = Brewery(name=args['name'])
        brewery.save()
        return self.return_single(brewery, 201)
