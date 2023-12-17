from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length

class RegisterUserForm(FlaskForm):
    """ A form to register a new user. """

    username = StringField("Username:", validators=[InputRequired(), Length(1, 20)])
    password = PasswordField("Password:", validators=[InputRequired()])
    email = EmailField("Email:", validators=[InputRequired(), Length(1, 50)])
    first_name = StringField("First Name:", validators=[InputRequired(), Length(1, 30)])
    last_name = StringField("Last Name:", validators=[InputRequired(), Length(1, 30)])

class LoginUserForm(FlaskForm):
    """ A form to log in an existing user with username and password. """

    username = StringField("Username:", validators=[InputRequired(), Length(1, 20)])
    password = PasswordField("Password:", validators=[InputRequired()])

class FeedbackForm(FlaskForm):
    """ A form to create or update feedback. """

    title = StringField("Title:", validators=[InputRequired(), Length(1, 100)])
    content = TextAreaField("Content:", validators=[InputRequired()])