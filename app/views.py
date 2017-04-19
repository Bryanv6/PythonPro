from flask import render_template
from app import p_app

@p_app.route('/')
@p_app.route('/index')
def index():
    return render_template('index.html')
    #TODO: display main page contexts here.