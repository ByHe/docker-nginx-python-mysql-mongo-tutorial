from flask import Flask
from flask_cors import CORS
from router import router

app = Flask(__name__)
CORS(app)  # Tillåter CORS (samma som app.use(cors()))
app.register_blueprint(router)

# ---- Starta servern ----
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

