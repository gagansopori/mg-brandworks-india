from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_mail import Message
# Import your ContactForm class here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

from app.email_service import EmailService
from app.utils.extensions import mail

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def index():
    data = request.form.to_dict()
    service = EmailService(data)
    success = service.send_email()
    if success:
        flash('Message Sent!', 'success')
        return redirect(url_for('contact.index'))
    else:
        flash('Failed to send message. Please try again...', 'danger')
        return render_template('contact.html')