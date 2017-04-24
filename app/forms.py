from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, fields
from wtforms.validators import DataRequired

class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-type Password', validators=[DataRequired()])
    game_name = StringField()

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    game_name = StringField()

class Contact(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = fields.TextAreaField("Message", validators=[DataRequired()],
                                   render_kw=({"rows": 10, "cols": 30}))
    game_name = StringField()

class Search(FlaskForm):
    game_name = StringField('Game name', validators=[DataRequired()])

class About(FlaskForm):
    game_name = StringField()