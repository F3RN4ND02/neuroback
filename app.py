from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from marshmallow import ValidationError

from db import db
from blacklist import BLACKLIST
from routes.all import init_all_routes
from utils.custom_errors import *
from utils.error_handlers import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/mydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["UPLOAD_FOLDER"] = "public"
app.config["JWT_BLACKLIST_ENABLED"] = True  # enable blacklist feature
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens
app.secret_key = "jose"  # could do app.config['JWT_SECRET_KEY'] if we prefer
CORS(app)
api = Api(app)

jwt = JWTManager(app)

# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return (
        decrypted_token["jti"] in BLACKLIST
    )

# ERROR HANDLING
app.register_error_handler(ValidationError, handle_validation_error)
app.register_error_handler(ResourceAlreadyExists, handle_resource_exists_error)
app.register_error_handler(ResourceNotFound, handle_resource_not_found_error)
app.register_error_handler(InvalidCredentials, handle_invalid_cred_error)
app.register_error_handler(NotAuthorized, handle_authorization_error)

init_all_routes(api)

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)