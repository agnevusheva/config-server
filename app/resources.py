from flask_restful import Resource
from app.models import Item, TableSpot

print("LOADING RESOURCES")
class ItemListResource(Resource):
    def get(self):
        items = Item.query.all()
        return [{"id": item.id, "name": item.name, "price": item.price} for item in items]

class TableListResource(Resource):
    def get(self):
        tables = TableSpot.query.all()
        return [{"id": table.id, "shape": table.shape.value} for table in tables]