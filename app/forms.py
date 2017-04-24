from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import SelectField

class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    password2 = StringField('Re-type Password', validators=[DataRequired()])
    game_name = StringField()

class About(FlaskForm):
    game_name = StringField()

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    game_name = StringField()

class Contact(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    game_name = StringField()

class Search(FlaskForm):
    game_name = StringField()
	

class Platform_dropdown(FlaskForm):
    game_name = StringField()
    """
    platform = []
    platform.append(('Playstation 4', 'ps4'))
    platform.append(('Xbox One', 'xboxone'))
    platform.append(('Switch', 'switch'))
    platform.append(('PC', 'pc'))
    platform.append(('Wii U', 'wii-u'))
    platform.append(('3DS', '3ds'))
    platform.append(('PS Vita', 'vita'))
    platform.append(('iOS', 'ios')) """

    timeFrames = []
    timeFrames.append(('All Time','all'))
    timeFrames.append(('Last 90 Days','90day'))
    timeFrames.append(('2017','2017'))
    timeFrames.append(('2016','2016'))
    timeFrames.append(('2015','2015'))
    timeFrames.append(('2014','2014')) 
    timeFrames.append(('2013','2013'))
    timeFrames.append(('2012','2012'))
    timeFrames.append(('2011','2011'))
    timeFrames.append(('2010','2010'))
    timeFrames.append(('2009','2009'))
    timeFrames.append(('2008','2008'))
    timeFrames.append(('2007','2007'))
    timeFrames.append(('2006','2006'))
    timeFrames.append(('2005','2005'))
    timeFrames.append(('2004','2004'))
    timeFrames.append(('2003','2003'))
    timeFrames.append(('2002','2002'))
    timeFrames.append(('2001','2001'))
    timeFrames.append(('2000','2000'))
    timeFrames.append(('1999','1999'))
    timeFrames.append(('1998','1998'))
    timeFrames.append(('1997','1997'))
    timeFrames.append(('1996','1996'))
    timeFrames.append(('1995','1995'))
    _platform = 'Playstation 4'
    _timeFrame = 'All Time'
    #_platform = SelectField('Platform', choices=[('Playstation 4', 'ps4'), ('Xbox One', 'xboxone'), ('Switch', 'switch'), ('PC', 'pc'), ('Wii U', 'wii-u'), ('3DS', '3ds'), ('PS Vita', 'vita'), ('iOS', 'ios')])
    #_timeFrame = SelectField('Timeframe', choices=timeFrames)