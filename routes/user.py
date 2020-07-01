from resources.user import UserRegister, UserLogin, User, UserLogout, Users

def init_user_routes(api):
    api.add_resource(UserRegister, "/register")
    api.add_resource(User, "/users/<int:user_id>")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogout, "/logout")
    api.add_resource(Users, "/users")
