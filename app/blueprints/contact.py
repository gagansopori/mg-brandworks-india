from flask import Blueprint, render_template, flash, request
from app.services.email_service import EmailService
from app.utils.forms import ContactForm

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        user_data = {
            'name': form.name.data,
            'email': form.email.data,
            'subject': form.subject.data,
            'message': form.message.data
        }
        service = EmailService(user_data)
        success = service.send_email()

        if success:
            flash('Message Sent!', 'success')
        else:
            flash('Failed to send message. Please try again...', 'danger')
    elif request.method == 'POST':
        flash("Please correct the errors in the form.", "danger")
    return render_template('contact.html', form=form)