from flask import render_template
from app import p_app
from app.forms import Register, Login, Contact

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
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        #TODO: call login function here
    return render_template('login.html', form=form)

@p_app.route('/register', methods=['GET', 'POST'])
@p_app.route('/register.html', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        password2 = form.password2.data
        #TODO: call register function here
    return render_template('register.html', form=form)

@p_app.route('/contact', methods=['GET', 'POST'])
@p_app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    form = Contact()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        #TODO: call contact function here
    return render_template('contact.html', form=form)

