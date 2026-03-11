from flask import Blueprint, jsonify
from .connect import getDB

router = Blueprint('router', __name__)

# Returnerar länder i Europa.
@router.route('/countries', methods=['GET'])
def get_countries_in_europe():
    db = getDB()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM country WHERE Continent='Europe' ORDER BY Name")
    rows = cursor.fetchall()
  
    cursor.close()
    db.close()
    
    return jsonify(rows)

# Returnerar länder i vald kontinent.
@router.route('/countries/<continent>', methods=['GET'])
def get_countries_by_continent(continent):
    db = getDB()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM country WHERE Continent=%s ORDER BY Name", (continent,))
    rows = cursor.fetchall()

    cursor.close()
    db.close()
    
    return jsonify(rows)

# Returnerar land med vald landskod.
@router.route('/country/<code>', methods=['GET'])
def get_country_by_code(code):
    db = getDB()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM country WHERE Code = %s", (code,))
    rows = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    return jsonify(rows)

# Returnerar städer i land med vald landskod."
@router.route('/cities/<code>', methods=['GET'])
def get_cities_by_country_code(code):
    db = getDB()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM city WHERE CountryCode = %s", (code,))
    rows = cursor.fetchall()
    
    cursor.close()
    db.close()
    return jsonify(rows)

# Fångar upp övriga anrop.
@router.route('/', defaults={'path': ''}, methods=['GET'])
@router.route('/<path>', methods=['GET'])
def catch_all(path):
    return jsonify({'success': False})
