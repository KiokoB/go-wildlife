#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, jsonify, abort

from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Animal, Keeper, Enclosure, Species, Diet

# Views go here!
# Animal endpoints
def serialize_animal(animal):
    """Return animal as a dictionary"""
    return {
        'id': animal.id,
        'name': animal.name,
        'gender': animal.gender,
        'year_of_arrival': animal.year_of_arrival,
        'species': animal.species.species_type,
        'diet': animal.diet.diet_type,
        'keeper': animal.keeper.name,
        'enclosure': animal.enclosure.enclosure_type
    }
 
# Routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Go Wild Wildlife Park API 🐾"}), 200


#   ANIMAL ENDPOINTS
@app.route('/animals', methods=['GET'])
def get_animals():
    animals = Animal.query.all()
    return jsonify([serialize_animal(a) for a in animals]), 200

@app.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    animal = Animal.query.get_or_404(id)
    return jsonify(serialize_animal(animal)), 200

@app.route('/animals', methods=['POST'])
def create_animal():
    data = request.get_json()
    try:
        new_animal = Animal(
            name=data['name'],
            gender=data['gender'],
            year_of_arrival=data['year_of_arrival'],
            species_id=data['species_id'],
            diet_id=data['diet_id'],
            keeper_id=data['keeper_id'],
            enclosure_id=data['enclosure_id']
        )
        db.session.add(new_animal)
        db.session.commit()
        return jsonify(serialize_animal(new_animal)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    animal = Animal.query.get_or_404(id)
    data = request.get_json()

    for field in ['name', 'gender', 'year_of_arrival', 'species_id', 'diet_id', 'keeper_id', 'enclosure_id']:
        if field in data:
            setattr(animal, field, data[field])

    db.session.commit()
    return jsonify(serialize_animal(animal)), 200

@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    return jsonify({'message': 'Animal deleted successfully'}), 204


#   KEEPER ENDPOINTS
@app.route('/keepers', methods=['GET'])
def get_keepers():
    keepers = Keeper.query.all()
    return jsonify([
        {'id': k.id, 'name': k.name, 'date_of_birth': str(k.date_of_birth), 'rank': k.rank}
        for k in keepers
    ]), 200

#   SPECIES ENDPOINTS
# ----------------------
@app.route('/species', methods=['GET'])
def get_species():
    species = Species.query.all()
    return jsonify([
        {'id': s.id, 'species_type': s.species_type, 'species_group': s.species_group,
         'lifestyle': s.lifestyle, 'conservation_status': s.conservation_status}
        for s in species
    ]), 200

#   DIET ENDPOINTS
# ----------------------
@app.route('/diets', methods=['GET'])
def get_diets():
    diets = Diet.query.all()
    return jsonify([
        {'id': d.id, 'diet_type': d.diet_type, 'feeds_per_day': d.feeds_per_day}
        for d in diets
    ]), 200

#   ENCLOSURE ENDPOINTS
# ----------------------
@app.route('/enclosures', methods=['GET'])
def get_enclosures():
    enclosures = Enclosure.query.all()
    return jsonify([
        {'id': e.id, 'enclosure_type': e.enclosure_type, 'location': e.location}
        for e in enclosures
    ]), 200


if __name__ == '__main__':
    app.run(port=4444, debug=True)

