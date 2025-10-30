# #!/usr/bin/env python3

# # Standard library imports
# from random import randint, choice as rc

# # Remote library imports
# from faker import Faker

# # Local imports
# from app import app
# from models import db


# def seed_data():
#     fake = Faker()

#     # Clear existing data
#     print("Clearing old data...")
#     Animal.query.delete()
#     Keeper.query.delete()
#     db.session.commit()

#     # Create Keepers
#     print("Seeding keepers...")
#     keepers = []
#     for _ in range(5):
#         keeper = Keeper(
#             name=fake.name(),
#             date_of_birth=fake.date_of_birth(minimum_age=25, maximum_age=60),
#             rank=random.choice(['Junior', 'Standard', 'Senior'])
#         )
#         db.session.add(keeper)
#         keepers.append(keeper)
#     db.session.commit()

#     # Create Animals
#     print("Seeding animals...")
#     for _ in range(10):
#         animal = Animal(
#             name=fake.first_name(),
#             gender=random.choice(['M', 'F']),
#             year_of_arrival=random.randint(2015, 2024),
#             keeper_id=random.choice(keepers).id
#         )
#         db.session.add(animal)

#     try:
#         db.session.commit()
#         print(f"✅ Seeded {len(keepers)} keepers and 10 animals successfully!")
#     except IntegrityError:
#         db.session.rollback()
#         print("❌ Integrity error — data not committed.")

# if __name__ == '__main__':
#     fake = Faker()
#     with app.app_context():
#         print("Starting seed...")
#         # Seed code goes here!

#!/usr/bin/env python3

from faker import Faker
from random import choice, randint
from sqlalchemy.exc import IntegrityError
from datetime import date
from config import db, app
from models import Animal, Keeper, Species, Diet, Enclosure

import random


def seed_data():
    fake = Faker()

    # ==============================
    # 1️⃣ Clear existing data
    # ==============================
    print("Clearing old data...")
    Animal.query.delete()
    Keeper.query.delete()
    Species.query.delete()
    Diet.query.delete()
    Enclosure.query.delete()
    db.session.commit()

    # ==============================
    # 2️⃣ Seed Species
    # ==============================
    print("Seeding species...")
    species_list = [
        ('African Elephant', 'Mammal', 'Herbivore', 'Vulnerable'),
        ('Bengal Tiger', 'Mammal', 'Carnivore', 'Endangered'),
        ('Komodo Dragon', 'Reptile', 'Carnivore', 'Vulnerable'),
        ('Giant Panda', 'Mammal', 'Herbivore', 'Endangered'),
        ('Emperor Penguin', 'Bird', 'Carnivore', 'Least Concern'),
    ]
    species_objects = []
    for s in species_list:
        sp = Species(
            species_type=s[0],
            species_group=s[1],
            lifestyle=s[2],
            conservation_status=s[3]
        )
        db.session.add(sp)
        species_objects.append(sp)
    db.session.commit()

    # ==============================
    # 3️⃣ Seed Diets
    # ==============================
    print("Seeding diets...")
    diet_list = [
        ('Herbivore', 3),
        ('Carnivore', 2),
        ('Omnivore', 3),
        ('Insectivore', 4),
        ('Piscivore', 2)
    ]
    diet_objects = []
    for d in diet_list:
        diet = Diet(diet_type=d[0], feeds_per_day=d[1])
        db.session.add(diet)
        diet_objects.append(diet)
    db.session.commit()

    # ==============================
    # 4️⃣ Seed Enclosures
    # ==============================
    print("Seeding enclosures...")
    enclosure_list = [
        ('Grassland Habitat', 'North Zone'),
        ('Jungle Habitat', 'Central Zone'),
        ('Reptile House', 'East Wing'),
        ('Bird Aviary', 'South Zone'),
        ('Aquatic Dome', 'West Wing'),
    ]
    enclosure_objects = []
    for e in enclosure_list:
        enc = Enclosure(enclosure_type=e[0], location=e[1])
        db.session.add(enc)
        enclosure_objects.append(enc)
    db.session.commit()

    # ==============================
    # 5️⃣ Seed Keepers
    # ==============================
    print("Seeding keepers...")
    keeper_objects = []
    for _ in range(5):
        keeper = Keeper(
            name=fake.name(),
            date_of_birth=fake.date_of_birth(minimum_age=25, maximum_age=60),
            rank=random.choice(['Junior', 'Standard', 'Senior'])
        )
        db.session.add(keeper)
        keeper_objects.append(keeper)
    db.session.commit()

    # ==============================
    # 6️⃣ Seed Animals
    # ==============================
    print("Seeding animals...")
    for _ in range(20):
        animal = Animal(
            name=fake.first_name(),
            gender=random.choice(['M', 'F']),
            year_of_arrival=random.randint(2015, 2024),
            species_id=random.choice(species_objects).id,
            diet_id=random.choice(diet_objects).id,
            keeper_id=random.choice(keeper_objects).id,
            enclosure_id=random.choice(enclosure_objects).id,
        )
        db.session.add(animal)

    try:
        db.session.commit()
        print("✅ Database successfully seeded!")
        print(f"Added {len(species_objects)} species, {len(diet_objects)} diets, "
              f"{len(enclosure_objects)} enclosures, {len(keeper_objects)} keepers, and 20 animals.")
    except IntegrityError:
        db.session.rollback()
        print("❌ IntegrityError: Could not commit data.")


if __name__ == '__main__':
    with app.app_context():
        print("Starting Wildlife Park seeding process...")
        seed_data()
