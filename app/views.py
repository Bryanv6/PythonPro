from flask import render_template
from app import p_app
from app.forms import Register, Login, Contact, Search
from app.accounts import register_account, login_account
from app.metascrap import meta

@p_app.route('/', methods=['GET', 'POST'])
@p_app.route('/index', methods=['GET', 'POST'])
@p_app.route('/index.html', methods=['GET', 'POST'])
def index():
    info = None
    form = Search()
    if form.validate_on_submit():
        game_name = form.game_name.data
        info = meta('playstation-4', game_name)
    return render_template('index.html', form=form, info=info)

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
    form = Contact()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        #TODO: call contact function here
    return render_template('contact.html', form=form)

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
    top10 = None
    form = Platform_dropdown()
    _platform = form._platform
    _timeFrame = form._timeFrame
    top10 = get_top10('','')
    return render_template('top10.html', form=form, top10=top10)

