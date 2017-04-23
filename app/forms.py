from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    password2 = StringField('Re-type Password', validators=[DataRequired()])

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])