from .user import init_user_routes
from .pacient import init_pacient_routes
from .clinical_story import init_clinical_story_routes
from .direction.country import init_country_routes
from .direction.state import init_state_routes
from .direction.municipality import init_municipality_routes
from .direction.direction import init_direction_routes
from .forms import init_forms_routes
from .chat.chat import init_chat_routes

def init_all_routes(api):
    init_user_routes(api)
    init_pacient_routes(api)
    init_clinical_story_routes(api)
    init_country_routes(api)
    init_state_routes(api)
    init_municipality_routes(api)
    init_direction_routes(api)
    init_forms_routes(api)
    init_chat_routes(api)
