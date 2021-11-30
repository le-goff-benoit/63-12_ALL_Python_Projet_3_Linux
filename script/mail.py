from constants import API_KEY
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Email:
    def __init__(self, email_to):
        self.email_to = email_to

    def send_message(self, subject):
        message = Mail(
        from_email='benoit.le.goff@icloud.com',
        to_emails='benoit.le.goff@icloud.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
        try:
            sg = SendGridAPIClient(API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)