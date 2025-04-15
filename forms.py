from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, PasswordField
from wtforms.validators import DataRequired, Length, Optional, URL, Email

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10)])
    technologies = StringField('Technologies', validators=[DataRequired()])
    project_link = StringField('Project Link', validators=[Optional(), URL()])
    image = FileField('Project Image')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=500)])