import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from controllers import BreweryList, BreweryResource
from models import db 

def initApp(config):
    
    ####################
    # Application init
    ####################
    
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    ####################
    # Database & api init
    ####################
    
    db.init_app(app)
    api = Api(app)

    #api.add_resource(Index, '/')
    api.add_resource(BreweryList, '/breweries')
    api.add_resource(BreweryResource, '/breweries/<brewery_id>')
    
    return app