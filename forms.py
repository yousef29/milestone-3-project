from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class loginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class signUpForm(FlaskForm):
    first_name = StringField("First name: ", validators=[DataRequired()])
    last_name = StringField("Last name: ", validators=[DataRequired()])
    username = StringField("Username: ", validators=[DataRequired()])
    email = StringField("Email address: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    repeat_password = PasswordField("Repeat your password: ", validators=[DataRequired()])
