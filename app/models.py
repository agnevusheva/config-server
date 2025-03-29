from app import db
from enum import Enum

class ShapeEnum(Enum):
    ROUND = "round"
    SQUARE = "square"

class TableSpot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shape = db.Column(db.Enum(ShapeEnum), nullable=False)

    def __repr__(self):
        return f'<TableSpot {self.id} - {self.shape.value}>'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=True)

    def __repr__(self):
        return f'<Item {self.name} - ${self.price}>'

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship('Item', backref='menu', lazy=True)

    def __repr__(self):
        return f'<Menu {self.id}>'