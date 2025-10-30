# #!/usr/bin/env python3

# from faker import Faker
# from random import choice, randint
# from sqlalchemy.exc import IntegrityError
# from datetime import date
# from config import db, app
# from models import Animal, Keeper, Species, Diet, Enclosure

# import random


# def seed_data():
#     fake = Faker()

#     # ==============================
#     # 1️⃣ Clear existing data
#     # ==============================
#     print("Clearing old data...")
#     Animal.query.delete()
#     Keeper.query.delete()
#     Species.query.delete()
#     Diet.query.delete()
#     Enclosure.query.delete()
#     db.session.commit()

#     # ==============================
#     # 2️⃣ Seed Species
#     # ==============================
#     print("Seeding species...")
#     species_list = [
#         ('African Elephant', 'Mammal', 'Herbivore', 'Vulnerable'),
#         ('Bengal Tiger', 'Mammal', 'Carnivore', 'Endangered'),
#         ('Komodo Dragon', 'Reptile', 'Carnivore', 'Vulnerable'),
#         ('Giant Panda', 'Mammal', 'Herbivore', 'Endangered'),
#         ('Emperor Penguin', 'Bird', 'Carnivore', 'Least Concern'),
#     ]
#     species_objects = []
#     for s in species_list:
#         sp = Species(
#             species_type=s[0],
#             species_group=s[1],
#             lifestyle=s[2],
#             conservation_status=s[3]
#         )
#         db.session.add(sp)
#         species_objects.append(sp)
#     db.session.commit()

#     # ==============================
#     # 3️⃣ Seed Diets
#     # ==============================
#     print("Seeding diets...")
#     diet_list = [
#         ('Herbivore', 3),
#         ('Carnivore', 2),
#         ('Omnivore', 3),
#         ('Insectivore', 4),
#         ('Piscivore', 2)
#     ]
#     diet_objects = []
#     for d in diet_list:
#         diet = Diet(diet_type=d[0], feeds_per_day=d[1])
#         db.session.add(diet)
#         diet_objects.append(diet)
#     db.session.commit()

#     # ==============================
#     # 4️⃣ Seed Enclosures
#     # ==============================
#     print("Seeding enclosures...")
#     enclosure_list = [
#         ('Grassland Habitat', 'North Zone'),
#         ('Jungle Habitat', 'Central Zone'),
#         ('Reptile House', 'East Wing'),
#         ('Bird Aviary', 'South Zone'),
#         ('Aquatic Dome', 'West Wing'),
#     ]
#     enclosure_objects = []
#     for e in enclosure_list:
#         enc = Enclosure(enclosure_type=e[0], location=e[1])
#         db.session.add(enc)
#         enclosure_objects.append(enc)
#     db.session.commit()

#     # ==============================
#     # 5️⃣ Seed Keepers
#     # ==============================
#     print("Seeding keepers...")
#     keeper_objects = []
#     for _ in range(5):
#         keeper = Keeper(
#             name=fake.name(),
#             date_of_birth=fake.date_of_birth(minimum_age=25, maximum_age=60),
#             rank=random.choice(['Junior', 'Standard', 'Senior'])
#         )
#         db.session.add(keeper)
#         keeper_objects.append(keeper)
#     db.session.commit()

#     # ==============================
#     # 6️⃣ Seed Animals
#     # ==============================
#     print("Seeding animals...")
#     for _ in range(20):
#         animal = Animal(
#             name=fake.first_name(),
#             gender=random.choice(['M', 'F']),
#             year_of_arrival=random.randint(2015, 2024),
#             species_id=random.choice(species_objects).id,
#             diet_id=random.choice(diet_objects).id,
#             keeper_id=random.choice(keeper_objects).id,
#             enclosure_id=random.choice(enclosure_objects).id,
#         )
#         db.session.add(animal)

#     try:
#         db.session.commit()
#         print("✅ Database successfully seeded!")
#         print(f"Added {len(species_objects)} species, {len(diet_objects)} diets, "
#               f"{len(enclosure_objects)} enclosures, {len(keeper_objects)} keepers, and 20 animals.")
#     except IntegrityError:
#         db.session.rollback()
#         print("❌ IntegrityError: Could not commit data.")


# if __name__ == '__main__':
#     with app.app_context():
#         print("Starting Wildlife Park seeding process...")
#         seed_data()


#!/usr/bin/env python3
from app import app
from models import db, Animal, Keeper, Species, Diet, Enclosure
from datetime import datetime

def seed_data():
    print("🌱 Starting seed process...")

    with app.app_context():
        # Clear existing records
        db.session.query(Animal).delete()
        db.session.query(Keeper).delete()
        db.session.query(Species).delete()
        db.session.query(Diet).delete()
        db.session.query(Enclosure).delete()
        db.session.commit()
        print("🧹 Cleared existing data")

        # === Embedded Data from CSV ===
        data = [
            {
                "animal_id": "A3",
                "animal_name": "Geoffrey",
                "gender": "M",
                "year_of_arrival": 2018,
                "species_id": "S3",
                "species_type": "Gorilla",
                "species_group": "Mammal",
                "lifestyle": "Troop",
                "conservation_status": "Threatened",
                "diet_id": "D1",
                "diet_type": "Omnivore",
                "feeds_per_day": 6,
                "keeper_id": "K1",
                "keeper_name": "Dave",
                "keeper_dob": "18-06-64",
                "keeper_rank": "Senior",
                "enclosure_id": "E2",
                "enclosure_type": "Glass",
                "enclosure_location": "North"
            },
            {
                "animal_id": "A4",
                "animal_name": "Oliver",
                "gender": "M",
                "year_of_arrival": 2011,
                "species_id": "S4",
                "species_type": "Orang-utan",
                "species_group": "Mammal",
                "lifestyle": "Solitary",
                "conservation_status": "Critically Endangered",
                "diet_id": "D1",
                "diet_type": "Omnivore",
                "feeds_per_day": 6,
                "keeper_id": "K1",
                "keeper_name": "Dave",
                "keeper_dob": "18-06-64",
                "keeper_rank": "Senior",
                "enclosure_id": "E1",
                "enclosure_type": "Moat",
                "enclosure_location": "North"
            },
            {
                "animal_id": "A6",
                "animal_name": "Roger",
                "gender": "M",
                "year_of_arrival": 2000,
                "species_id": "S6",
                "species_type": "Rhinoceros",
                "species_group": "Mammal",
                "lifestyle": "Solitary",
                "conservation_status": "Critically Endangered",
                "diet_id": "D2",
                "diet_type": "Herbivore",
                "feeds_per_day": 6,
                "keeper_id": "K2",
                "keeper_name": "Kayden",
                "keeper_dob": "21-01-85",
                "keeper_rank": "Junior",
                "enclosure_id": "E3",
                "enclosure_type": "Fence",
                "enclosure_location": "South"
            },
            {
                "animal_id": "A7",
                "animal_name": "Clive",
                "gender": "M",
                "year_of_arrival": 2013,
                "species_id": "S7",
                "species_type": "Crocodile",
                "species_group": "Reptile",
                "lifestyle": "Social",
                "conservation_status": "Vulnerable",
                "diet_id": "D3",
                "diet_type": "Carnivore",
                "feeds_per_day": 4,
                "keeper_id": "K2",
                "keeper_name": "Kayden",
                "keeper_dob": "21-01-85",
                "keeper_rank": "Junior",
                "enclosure_id": "E3",
                "enclosure_type": "Fence",
                "enclosure_location": "South"
            },
            {
                "animal_id": "A8",
                "animal_name": "Eddie",
                "gender": "M",
                "year_of_arrival": 2016,
                "species_id": "S8",
                "species_type": "Elephant",
                "species_group": "Mammal",
                "lifestyle": "Herd",
                "conservation_status": "Threatened",
                "diet_id": "D2",
                "diet_type": "Herbivore",
                "feeds_per_day": 6,
                "keeper_id": "K2",
                "keeper_name": "Kayden",
                "keeper_dob": "21-01-85",
                "keeper_rank": "Junior",
                "enclosure_id": "E4",
                "enclosure_type": "Walled",
                "enclosure_location": "South"
            }
        ]

        # === Create related records (avoid duplicates) ===
        for entry in data:
            # Species
            species = Species.query.filter_by(species_type=entry["species_type"]).first()
            if not species:
                species = Species(
                    species_type=entry["species_type"],
                    species_group=entry["species_group"],
                    lifestyle=entry["lifestyle"],
                    conservation_status=entry["conservation_status"]
                )
                db.session.add(species)

            # Diet
            diet = Diet.query.filter_by(diet_type=entry["diet_type"]).first()
            if not diet:
                diet = Diet(
                    diet_type=entry["diet_type"],
                    feeds_per_day=entry["feeds_per_day"]
                )
                db.session.add(diet)

            # Keeper
            keeper = Keeper.query.filter_by(name=entry["keeper_name"]).first()
            if not keeper:
                keeper = Keeper(
                    name=entry["keeper_name"],
                    date_of_birth=datetime.strptime(entry["keeper_dob"], "%d-%m-%y").date(),
                    rank=entry["keeper_rank"]
                )
                db.session.add(keeper)

            # Enclosure
            enclosure = Enclosure.query.filter_by(enclosure_type=entry["enclosure_type"]).first()
            if not enclosure:
                enclosure = Enclosure(
                    enclosure_type=entry["enclosure_type"],
                    location=entry["enclosure_location"]
                )
                db.session.add(enclosure)

            db.session.flush()  # ensures IDs are generated before animal creation

            # Animal
            animal = Animal(
                name=entry["animal_name"],
                gender=entry["gender"],
                year_of_arrival=entry["year_of_arrival"],
                species_id=species.id,
                diet_id=diet.id,
                keeper_id=keeper.id,
                enclosure_id=enclosure.id
            )
            db.session.add(animal)

        db.session.commit()
        print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
