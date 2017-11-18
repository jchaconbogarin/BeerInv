import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return "Boga's beer collection inventory"

if __name__ == '__main__':
    app.run()