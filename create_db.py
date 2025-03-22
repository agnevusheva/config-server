import os
from app import app, db
from models import Table, Item, Menu
from sqlalchemy import inspect

print("Current working directory:", os.getcwd())

with app.app_context():
    db.create_all()
    print("Database created!")
    inspector = inspect(db.engine)
    print("Tables:", inspector.get_table_names())