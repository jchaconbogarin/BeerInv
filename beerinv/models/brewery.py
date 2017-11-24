from flask_sqlalchemy import SQLAlchemy
from beerinv.models.base_model import db, BaseModel

class Brewery(BaseModel):
    __tablename__ = 'breweries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }