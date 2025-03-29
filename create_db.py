import os
from app import app, db
from app.models import TableSpot, Item, Menu
from sqlalchemy import ins

with app.app_context():
    db.create_all()
    print("Database created!")
    inspector = inspect(db.engine)
    print("Tables:", inspector.get_table_names())