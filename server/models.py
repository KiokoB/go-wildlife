from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import aliased
from sqlalchemy import MetaData, func

from config import db

# Models go here!
# Define the animal model
#   TABLE: Animal
# ==========================
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    year_of_arrival = db.Column(db.Integer, nullable=False)

    # Foreign Keys (MUST MATCH TABLE NAMES)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
    diet_id = db.Column(db.Integer, db.ForeignKey('diets.id'), nullable=False)
    keeper_id = db.Column(db.Integer, db.ForeignKey('keepers.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=False)

    def __repr__(self):
        return f"<Animal {self.name} ({self.gender})>"


# ==========================
#   TABLE: Keeper
# ==========================
class Keeper(db.Model):
    __tablename__ = 'keepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    rank = db.Column(db.String(20), nullable=False)

    # One keeper has many animals
    animals = db.relationship('Animal', backref='keeper', lazy=True)

    def __repr__(self):
        return f"<Keeper {self.name} ({self.rank})>"


# ==========================
#   TABLE: Enclosure
# ==========================
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    enclosure_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    # One enclosure has many animals
    animals = db.relationship('Animal', backref='enclosure', lazy=True)

    def __repr__(self):
        return f"<Enclosure {self.enclosure_type} - {self.location}>"


# ==========================
#   TABLE: Species
# ==========================
class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)
    species_type = db.Column(db.String(50), nullable=False)
    species_group = db.Column(db.String(50), nullable=False)
    lifestyle = db.Column(db.String(50), nullable=False)
    conservation_status = db.Column(db.String(50), nullable=False)

    # One species has many animals
    animals = db.relationship('Animal', backref='species', lazy=True)

    def __repr__(self):
        return f"<Species {self.species_type}>"


# ==========================
#   TABLE: Diet
# ==========================
class Diet(db.Model):
    __tablename__ = 'diets'

    id = db.Column(db.Integer, primary_key=True)
    diet_type = db.Column(db.String(50), nullable=False)
    feeds_per_day = db.Column(db.Integer, nullable=False)

    # One diet has many animals
    animals = db.relationship('Animal', backref='diet', lazy=True)

    def __repr__(self):
        return f"<Diet {self.diet_type}>"