from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from splitway.models import User
from wtforms.fields.html5 import DateTimeLocalField


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired()])
    last_name = StringField('Last Name',
                           validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SearchForm(FlaskForm):
    
    current_location = StringField('Current Location', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    time = DateTimeLocalField('Date/Time', format="%Y-%m-%dT%H:%M")
    #time = StringField('Date/Time MM/DD/YYYY HH:MM', validators=[DataRequired()])
    submit = SubmitField('Search')