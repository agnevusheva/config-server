from app import app, db
from models import Table, Item, Menu, ShapeEnum
from faker import Faker
import random

fake = Faker()
from faker_food import FoodProvider
fake.add_provider(FoodProvider)

def create_mock_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        for _ in range(10):
            table = Table(
                shape=random.choice([ShapeEnum.ROUND, ShapeEnum.SQUARE])
            )
            db.session.add(table)

        items = []
        for _ in range(20):
            item = Item(
                name=fake.dish(),
                price=round(random.uniform(1.0, 100.0), 2)
            )
            items.append(item)
            db.session.add(item)

        menu = Menu()
        db.session.add(menu)
        db.session.flush()

        for item in items:
            item.menu_id = menu.id

        db.session.commit()
        print("Database seeded with mock data!")

if __name__ == '__main__':
    create_mock_data()