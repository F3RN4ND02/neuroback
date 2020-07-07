def handle_validation_error(err):
    return { "success": False, "errors": err.messages}, 400

def handle_resource_exists_error(err):
    return { "success": False, "errors": err.field}, 400

def handle_invalid_cred_error(err):
    return { "success": False, "errors": "Contraseña invalida"}, 401

def handle_resource_not_found_error(err):
    return { "success": False, "errors": "Recurso no encontrado"}, 404

def handle_authorization_error(err):
    return { "success": False, "errors": "No tienes acceso a este recurso"}, 401