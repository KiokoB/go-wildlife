#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db


def seed_data():
    fake = Faker()

    # Clear existing data
    print("Clearing old data...")
    Animal.query.delete()
    Keeper.query.delete()
    db.session.commit()

    # Create Keepers
    print("Seeding keepers...")
    keepers = []
    for _ in range(5):
        keeper = Keeper(
            name=fake.name(),
            date_of_birth=fake.date_of_birth(minimum_age=25, maximum_age=60),
            rank=random.choice(['Junior', 'Standard', 'Senior'])
        )
        db.session.add(keeper)
        keepers.append(keeper)
    db.session.commit()

    # Create Animals
    print("Seeding animals...")
    for _ in range(10):
        animal = Animal(
            name=fake.first_name(),
            gender=random.choice(['M', 'F']),
            year_of_arrival=random.randint(2015, 2024),
            keeper_id=random.choice(keepers).id
        )
        db.session.add(animal)

    try:
        db.session.commit()
        print(f"✅ Seeded {len(keepers)} keepers and 10 animals successfully!")
    except IntegrityError:
        db.session.rollback()
        print("❌ Integrity error — data not committed.")

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
