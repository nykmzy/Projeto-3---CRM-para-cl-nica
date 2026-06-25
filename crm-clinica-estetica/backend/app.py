from flask import Flask
from flask_cors import CORS

from app.database.db import db
from app.routes.clientes import clientes_bp

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crm.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(clientes_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {
        "sistema": "CRM Clínica Estética",
        "status": "online"
    }

if __name__ == "__main__":
    app.run(debug=True)