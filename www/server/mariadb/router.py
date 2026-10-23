from flask import Blueprint, jsonify, request
from .connect import getDB
import bcrypt

router = Blueprint('router', __name__)

@router.route('/users', methods=['POST'])
def create_user():
    result = {'success': False}
    cost = 10

    data = request.get_json()
    first_name = data.get('firstName')
    sur_name = data.get('surName')
    user_name = data.get('userName')
    password = data.get('password')

    try:
        # Hasha lösenordet med bcrypt (motsvarar bcrypt.hash i Node.js)
        salt = bcrypt.gensalt(rounds=cost)
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

        db = getDB()
        cursor = db.cursor()
        
        # SQL-fråga för att lägga till användare (UUID() genererar uid direkt i MariaDB)
        sql = "INSERT INTO user(uid, firstname, surname, username, password) VALUES(UUID(), %s, %s, %s, %s)"
        cursor.execute(sql, (first_name, sur_name, user_name, password_hash))
        
        db.commit()
        cursor.close()
        db.close()
        
        result['success'] = True
    except Exception as err:
        print(err)

    return jsonify(result)

# Fångar upp övriga anrop.
@router.route('/', defaults={'path': ''}, methods=['GET'])
@router.route('/<path>', methods=['GET'])
def catch_all(path):
    return jsonify({'success': False})
