from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Brewery(db.Model):
    __tablename__ = 'breweries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Brewery id={} name={}>'.format(self.id, self.name)