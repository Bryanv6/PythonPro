from flask import render_template
from app import p_app
from app.forms import Register, Login, Contact, Search, Platform_dropdown
from app.accounts import register_account, login_account
from app.metascrap import meta
from app.top10 import get_top10
from app.contact import send_email

@p_app.route('/', methods=['GET', 'POST'])
@p_app.route('/index', methods=['GET', 'POST'])
@p_app.route('/index.html', methods=['GET', 'POST'])
def index():
    form = Search()
    return render_template('index.html', form=form)

@p_app.route('/about', methods=['GET', 'POST'])
@p_app.route('/about.html', methods=['GET', 'POST'])
def about():
    form = Search()
    return render_template('about.html', form=form)

@p_app.route('/login', methods=['GET', 'POST'])
@p_app.route('/login.html', methods=['GET', 'POST'])
def login():
    signin = None
    form = Login()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        signin = login_account(username, password)
    return render_template('login.html', form=form, signin=signin)

@p_app.route('/register', methods=['GET', 'POST'])
@p_app.route('/register.html', methods=['GET', 'POST'])
def register():
    register = None
    form = Register()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        password2 = form.password2.data
        register = register_account(username, password, password2)
    return render_template('register.html', form=form, register=register)

@p_app.route('/contact', methods=['GET', 'POST'])
@p_app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    sent = None
    form = Contact()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        sent = send_email(name, email, message)
    return render_template('contact.html', form=form, sent=sent)

@p_app.route('/search-result', methods=['GET', 'POST'])
@p_app.route('/search-result.html', methods=['GET', 'POST'])
def search_result():
    info = None
    form = Search()
    if form.validate_on_submit():
        game_name = form.game_name.data
        info = meta('playstation-4', game_name)
    return render_template('search_result.html', form=form, info=info)

@p_app.route('/top10', methods=['GET', 'POST'])
@p_app.route('/top10.html', methods=['GET', 'POST'])
def top10():
    form = Platform_dropdown()
    _platform = 'Playstation 4'
    _timeFrame = 'All Time'
    top10 = get_top10(_platform, _timeFrame)

    return render_template('top10.html', form=form, top10=top10)

