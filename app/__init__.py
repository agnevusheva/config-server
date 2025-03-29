from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'data.db')
    
    db.init_app(app)
    api.init_app(app)
    
    os.makedirs(app.instance_path, exist_ok=True)
    
    from app.resources import ItemListResource, TableListResource
    api.add_resource(ItemListResource, '/items')
    api.add_resource(TableListResource, '/tables')
    
    return app