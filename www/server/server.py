from flask import Flask
from flask_cors import CORS
#from mariadb.router import router as mariadb_router
from mongodb.mongo_router import mongo_router

app = Flask(__name__)
CORS(app)  # Tillåter anrop från annan domän

# Registrera båda blueprints
#app.register_blueprint(mariadb_router)
app.register_blueprint(mongo_router)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    