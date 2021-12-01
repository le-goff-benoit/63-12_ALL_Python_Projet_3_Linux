import smtplib, ssl
from constants import __EMAIL_ADRESS__, __EMAIL_PASSWORD__

class Mail:

    def __init__(self):
        self.port = 587
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = __EMAIL_ADRESS__
        self.password = __EMAIL_PASSWORD__

    def send(self, recipient, subject):
        server = smtplib.SMTP(self.smtp_server_domain_name, self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.sender_mail, self.password)
        server.sendmail(
        self.sender_mail,
        recipient,   
        "subject: " + subject)
        server.quit()