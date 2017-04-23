from flask import render_template
from app import p_app
from app.forms import Register, Login

@p_app.route('/')
@p_app.route('/index')
@p_app.route('/index.html')
def index():
    return render_template('index.html')

@p_app.route('/about')
@p_app.route('/about.html')
def about():
    return render_template('about.html')

@p_app.route('/login', methods=['GET', 'POST'])
@p_app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('login.html', form=form)

@p_app.route('/register', methods=['GET', 'POST'])
@p_app.route('/register.html', methods=['GET', 'POST'])
def register():
    form = Register()
    return render_template('register.html', form=form)

@p_app.route('/contact')
@p_app.route('/contact.html')
def contact():
    return render_template('contact.html')

