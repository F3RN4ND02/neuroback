from marshmallow import ValidationError
from .custom_errors import * 

def try_except(f):
    def wrapper(*args, **kw):
        try:
            return f(*args, **kw)
        except ValidationError as err:
            return { "success": False, "errors": err.messages}, 400
        except ResourceAlreadyExists:
            return { "success": False, "errors": "Resource with given primary key already exists"}, 400
        except InvalidCredentials:
            return { "success": False, "errors": "Invalid credentials"}, 401
        except ResourceNotFound:
            return { "success": False, "errors": "Resource not found"}, 404
        except NotAuthorized:
            return { "success": False, "errors": "You have no access to this resource"}, 401
    return wrapper
