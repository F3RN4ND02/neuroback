from resources.admin import Admin

def init_admin_routes(api):
    api.add_resource(Admin, "/admin")