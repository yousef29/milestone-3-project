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
    submit = SubmitField("Submit")


class createRecipeForm(FlaskForm):
    recipe_name = StringField("Recipe name: ", validators=[DataRequired()])
    description = StringField("A short description: ",)
    cook_time = StringField("Cooking time: ", validators=[DataRequired()])
    prep_time = StringField("Preparation time: ", validators=[DataRequired()])
    serves = StringField("How many does it serve?", validators=[DataRequired()])
    ingredients = TextAreaField("One ingredient per line", validators=[DataRequired()])
    method = TextAreaField("1. Start by...", validators=[DataRequired()])
    submit = SubmitField("Submit")


class editRecipeForm(FlaskForm):
    recipe_name = StringField("Recipe name: ", validators=[DataRequired()])
    description = StringField("A short description: ",)
    cook_time = StringField("Cooking time: ", validators=[DataRequired()])
    prep_time = StringField("Preparation time: ", validators=[DataRequired()])
    serves = StringField("How many does it serve?", validators=[DataRequired()])
    ingredients = TextAreaField("One ingredient per line", validators=[DataRequired()])
    method = TextAreaField("1. Start by...", validators=[DataRequired()])
    submit = SubmitField("Submit")


class deleteRecipeForm(FlaskForm):
    submit = SubmitField("Delete recipe")
