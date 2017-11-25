
from flask_restful import Resource, Api, reqparse, abort

from beerinv.models.base_model import db
from beerinv.models.brewery import Brewery

class BreweryBaseResource(Resource):
    
    arguments = [
        { 'field_name':'name', 'required':True, 'type':str, 'help':'This field is required.' }
    ]
    parser = reqparse.RequestParser()
    
    def get_brewery(self, brewery_id):
        brewery = Brewery.query.get(brewery_id)
        if brewery is not None:
            return brewery
        else:
            abort(404, message="The brewery you're looking for doesn't exist.")
            
    def return_single_brewery(self, brewery, http_return_code):
        return { 'data': { 'brewery': brewery.serialize } }, http_return_code
    
    def return_all_breweries(self):
        return { 'data': { 'breweries' : [i.serialize for i in Brewery.query.all()] } }, 200
    
    def add_parser_arguments(self):
        for a in self.arguments:
            self.parser.add_argument('name', required=a['required'], type=a['type'], help=a['help'])
    
    def parse_args(self):
        self.add_parser_arguments()
        return self.parser.parse_args()
    
class BreweryResource(BreweryBaseResource):
    
    def put(self, brewery_id):
        args = self.parse_args()
        brewery = self.get_brewery(brewery_id)
        brewery.name = args['name']
        brewery.save()
        return self.return_single_brewery(brewery, 200)
    
    def delete(self, brewery_id):
        brewery = self.get_brewery(brewery_id)
        brewery.delete()
        return self.return_all_breweries()
    
    def get(self, brewery_id):
        brewery = self.get_brewery(brewery_id)
        return self.return_single_brewery(brewery, 200)    
    
class BreweryList(BreweryBaseResource):
    
    def get(self):
        return self.return_all_breweries()
    
    def post(self):
        args = self.parse_args()
        brewery = Brewery(name=args['name'])
        brewery.save()
        return self.return_single_brewery(brewery, 201)