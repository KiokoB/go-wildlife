from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import aliased
from sqlalchemy import MetaData, func

from config import db

# # Define a naming convention for the metadata
# convention = {
#     "ix": "ix_%(column_0_label)s",
#     "uq": "uq_%(table_name)s_%(column_0_name)s",
#     "ck": "ck_%(table_name)s_%(constraint_name)s",
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#     "pk": "pk_%(table_name)s"
# }


# metadata = MetaData(naming_convention=convention)
# db = SQLAlchemy(metadata=metadata)

# Models go here!
# Define the animal model
class Animal (db.Model, SerializerMixin):
    __tablename__ = 'animals'


    aniaml_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    year_of_arrival = db.Column(db.Integer, nullable=False)


    # Forign keys
    keeper_id = db.Column(db.Integer, db.ForeignKey('keeper.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
    diet_id = db.Column(db.Integer, db.ForeignKey('diet.id'), nullable=False)


    def __repr__(self):
        return f"<Animal {self.name} ({self.gender})>"


# Define the keeper model
class Keeper (db.Model, SerializerMixin):
    __tablename__ = 'keepers'


    keeper_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Integer)
    rank = db.Column(db.String)


    # Relationship: one keeper has many animals
    animals = db.relationship('Animal', backref='keeper', lazy=True)


    def __repr__(self):
        return f"<Keeper {self.name} ({self.rank})>"

# Define the enclosure model
class Enclosure (db.Model, SerializerMixin):
    __tablename__ = 'enclosures'


    enclosure_id = db.Column(db.Integer, primary_key=True)
    en_type = db.Column(db.String, nullable=False)
    location = db.Column(db.String)
    # Relationship: one enclosure has many animals
    animals = db.relationship('Animal', backref='enclosure', lazy=True)


    def __repr__(self):
        return f"<Enclosure {self.enclosure_type} - {self.location}>"


# Define the animals' species model
class Species (db.Model, SerializerMixin):
    __tablename__ = 'species'


    species_id = db.Column(db.Integer, primary_key=True)
    sp_type = db.Column(db.String, nullable=False)
    sp_group = db.Column(db.String, nullable=False)
    lifestyle = db.Column(db.String, nullable=False)
    conservation_status = db.Column(db.String, nullable=False)


    # Relationships
    animals = db.relationship('Animal', backref='species')


    def __repr__(self):
        return f"<Species {self.species_type}>"

#Define the animals' diet model
class Diet (db.Model, SerializerMixin):
    __tablename__ = 'diets'


    diet_id = db.Column(db.Integer, primary_key=True)
    diet_type = db.Column(db.String, nullable=False)
    feed_per_day = db.Column(db.Integer)


    # Relationships
    animals = db.relationship('Animal', backref='diet', lazy=True)


    def __repr__(self):
        return f"<Diet {self.diet_type}>"