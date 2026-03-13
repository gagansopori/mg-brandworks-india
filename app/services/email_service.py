import logging
from flask_mail import Message
from app.utils.extensions import mail

log = logging.getLogger(__name__)

class EmailService:
    def __init__(self, user_data):
        self.user_data = user_data
        self.subject = user_data.get('subject')
        self.sender_name = user_data.get('name')
        self.sender_email = user_data.get('email')
        self.body_content = user_data.get('message')

    def send_email(self):
        """
        Sends an email based on the dynamic payload from the contact form.
        """
        msg = Message(
            subject=self.subject,
            sender=(self.sender_name, self.sender_email),
            recipients=["admin@mgbrandworks.in"]  # This can also come from app_config
        )
        msg.body = f"Message from {self.sender_name}:\n\n{self.body_content}"
        try:
            mail.send(msg)
            log.info(f"Email Service: Successfully sent email with subject: '{self.subject}'")
            return True
        except Exception as e:
            log.error(f"Email Service: Failed to send email. Error: {str(e)}")
            return False