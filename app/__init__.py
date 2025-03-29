from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)

    CORS(app)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    if os.environ.get('FLASK_ENV') == 'development':
        app.config['DEBUG'] = True
    else:
        app.config['DEBUG'] = False
    
    db.init_app(app)
    api.init_app(app)
    
    os.makedirs(app.instance_path, exist_ok=True)
    
    from app.resources import ItemListResource, TableListResource
    api.add_resource(ItemListResource, '/items')
    api.add_resource(TableListResource, '/tables')
    
    return app