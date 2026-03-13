from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message="Please enter your name."),
        Length(min=2, max=50)
    ])
    email = StringField('Email', validators=[
        DataRequired(message="Please enter your email."),
        Email(message="Invalid email address.")
    ])
    subject = StringField('Subject', validators=[
        DataRequired(message="Please enter a subject."),
        Length(min=5, max=100)
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(message="Please enter your message."),
        Length(min=10, max=1000)
    ])