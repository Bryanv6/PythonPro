from app import p_app

@p_app.route('/')
@p_app.route('/index')
def index():
    return "Welcome to the main page!"
    #TODO: display main page contexts here