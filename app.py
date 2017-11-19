import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, abort

from models import db, Brewery

####################
# Application init
####################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

####################
# Database & api init
####################

db.init_app(app)
api = Api(app)
#parser = reqparse.RequestParser()
#parser.add_argument('name')

####################
# Routes init
####################

class Index(Resource):
    def get(self):
        return {'message':'Boga\'s beer collection inventory'}
    
class BreweryBaseResource(Resource):
    
    arguments = ['name']
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
        return { 'data': { 'breweries' : [i.serialize for i in Brewery.query.all()] } }
    
    def add_parser_arguments(self):
        for argument in self.arguments:
            self.parser.add_argument(argument)
    
    def parse_args(self):
        # Include validations here
        self.add_parser_arguments()
        return self.parser.parse_args()
    
class BreweryResource(BreweryBaseResource):
    def put(self, brewery_id):
        args = self.parse_args()
        brewery = self.get_brewery(brewery_id)
        brewery.name = args['name']
        db.session.commit()
        return self.return_single_brewery(brewery, 200)
    
    def delete(self, brewery_id):
        brewery = self.get_brewery(brewery_id)
        db.session.delete(brewery)
        db.session.commit()
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
        db.session.add(brewery)
        db.session.commit()
        return self.return_single_brewery(brewery, 201)
    
api.add_resource(Index, '/')
api.add_resource(BreweryList, '/breweries')
api.add_resource(BreweryResource, '/breweries/<brewery_id>')
    
if __name__ == '__main__':
    app.run()


















