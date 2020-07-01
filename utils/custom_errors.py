class ResourceAlreadyExists(Exception):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field

class ResourceNotFound(Exception):
    pass

class InvalidCredentials(Exception):
    pass

class NotAuthorized(Exception):
    pass