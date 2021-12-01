import smtplib
from email.message import EmailMessage
from constants import __EMAIL_ADRESS__, __EMAIL_PASSWORD__
from contact import Contact
from file import File

class Mail:

    def __init__(self, file: File):
        self.port = 587
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = __EMAIL_ADRESS__
        self.password = __EMAIL_PASSWORD__
        self.file = file.name

    def connect(self):
        server = smtplib.SMTP(self.smtp_server_domain_name, self.port)  
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.sender_mail, self.password)
        return server
    
    def compute_subject(self):
        return ("Informations à propos du fichier : " + self.file)
    
    def compute_message(self, state, lines_count=0):
        if state and lines_count != 0:
            return (str(lines_count) + " lignes ont été supprimées pour traiter le fichier " + self.file + " avec réussite.")
        else:
            return ("Le fichier " + self.file + " n'a pas été traité suite à une erreur")

    def send_success_message(self, recipients: list[Contact]):
        for recipient in recipients:
            server = self.connect()
            msg = EmailMessage()
            msg.set_content(self.compute_message(True, 3))
            msg['Subject'] = self.compute_subject()
            msg['From'] = self.sender_mail
            msg['To'] = recipient.email
            server.send_message(msg)
            server.quit()
            print('Un email a été envoyé à ', recipient.email)

    def send_failed_message(self, recipients: list[Contact]):
        for recipient in recipients:
            server = self.connect()
            msg = EmailMessage()
            msg.set_content(self.compute_message(False))
            msg['Subject'] = self.compute_subject()
            msg['From'] = self.sender_mail
            msg['To'] = recipient.email
            server.send_message(msg)
            server.quit()
            print('Un email a été envoyé à ', recipient.email)