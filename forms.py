from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length

class RegisterUserForm(FlaskForm):
    username = StringField("Username:", validators=[InputRequired(), Length(1, 20)])
    password = PasswordField("Password:", validators=[InputRequired()])
    email = EmailField("Email:", validators=[InputRequired(), Length(1, 50)])
    first_name = StringField("First Name:", validators=[InputRequired(), Length(1, 30)])
    last_name = StringField("Last Name:", validators=[InputRequired(), Length(1, 30)])

class LoginUserForm(FlaskForm):
    username = StringField("Username:", validators=[InputRequired(), Length(1, 20)])
    password = PasswordField("Password:", validators=[InputRequired()])