from flask import Blueprint, Response, jsonify
from .connect import get_db
from bson.json_util import dumps

mongo_router = Blueprint('mongo_router', __name__)

# Returnerar länder i Europa.
@mongo_router.route('/countries', methods=['GET'])
def get_countries_in_europe():
    db = get_db()
    countries = db.country.find({"Continent": "Europe"})
    return Response(dumps(countries), mimetype='application/json')

# Returnerar länder i vald kontinent.
@mongo_router.route('/countries/<continent>', methods=['GET'])
def get_countries_by_continent(continent):
    db = get_db()
    countries = db.country.find({"Continent": continent}).sort("Name")
    return Response(dumps(countries), mimetype='application/json')

# Returnerar land med vald landskod.
@mongo_router.route('/country/<code>', methods=['GET'])
def get_country_by_code(code):
    db = get_db()
    # MongoDB är skiftlägeskänsligt, så vi använder en regex för att vara säker.
    country = db.country.find({"Code": {"$regex": f"^{code}$", "$options": "i"}})
    return Response(dumps(country), mimetype='application/json')

# Returnerar städer i land med vald landskod."
@mongo_router.route('/cities/<code>', methods=['GET'])
def get_cities_by_country_code(code):
    db = get_db()
    # MongoDB är skiftlägeskänsligt, så vi använder en regex för att vara säker.
    cities = db.city.find({"CountryCode": {"$regex": f"^{code}$", "$options": "i"}})
    return Response(dumps(cities), mimetype='application/json')

# Fångar upp övriga anrop.
@mongo_router.route('/', defaults={'path': ''}, methods=['GET'])
@mongo_router.route('/<path:path>', methods=['GET'])
def catch_all(path):
    # Använder Response för att säkerställa korrekt JSON-format
    return Response(dumps({'success': False}), mimetype='application/json', status=404)