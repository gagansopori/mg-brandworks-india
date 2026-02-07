from flask import Blueprint, render_template, redirect, url_for, flash
from flask_mail import Message
# Import your ContactForm class here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

from app.extensions import mail

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(subject=f"Inquiry from {form.name.data}",
                      sender="your-email@gmail.com",
                      recipients=["business@mgbrandworks.in"],
                      body=form.message.data)
        mail.send(msg)
        flash('Message Sent!', 'success')
        return redirect(url_for('contact.index'))
    return render_template('contact.html', form=form)


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')