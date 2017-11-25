
from abc import ABCMeta, abstractproperty, abstractmethod

from flask_restful import Resource, Api, reqparse, abort

from beerinv.models.base_model import db


class BaseResource(Resource):
    
    klass = None
    parser = reqparse.RequestParser()
    
    @property
    @abstractmethod
    def arguments(self):
        pass
    
    def get_single(self, id):
        obj = self.klass.query.get(id)
        if obj is not None:
            return obj
        else:
            abort(404, message="The object you're looking for doesn't exist.")
            
    def return_single(self, obj, http_return_code):
        return { 'data': { self.klass.object_name_singular: obj.serialize } }, http_return_code
    
    def return_all(self):
        return { 'data': { self.klass.object_name_plural : [i.serialize for i in self.klass.query.all()] } }, 200
    
    def add_parser_arguments(self):
        for a in self.arguments:
            self.parser.add_argument('name', required=a['required'], type=a['type'], help=a['help'])
    
    def parse_args(self):
        self.add_parser_arguments()
        return self.parser.parse_args()