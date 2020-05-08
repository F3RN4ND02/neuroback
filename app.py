from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from blacklist import BLACKLIST
from resources.doctor import DoctorRegister, DoctorLogin, Doctor, DoctorLogout
from resources.pacient import CreatePacient, Pacient
from resources.clinical_story import CreateClinicalStory, ClinicalStory

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True  # enable blacklist feature
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens
app.secret_key = "jose"  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return (
        decrypted_token["jti"] in BLACKLIST
    )

api.add_resource(DoctorRegister, "/register")
api.add_resource(Doctor, "/doctors/<int:doctor_id>")
api.add_resource(DoctorLogin, "/login")
api.add_resource(DoctorLogout, "/logout")

api.add_resource(CreatePacient, "/pacients")
api.add_resource(Pacient, "/pacients/<int:pacient_id>")

api.add_resource(CreateClinicalStory, "/clinical_stories")
api.add_resource(ClinicalStory, "/clinical_stories/<int:clinical_story_id>")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)