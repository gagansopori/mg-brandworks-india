import logging
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.email_service import EmailService

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