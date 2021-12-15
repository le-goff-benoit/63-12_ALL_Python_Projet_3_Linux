import smtplib
from email.message import EmailMessage
from constants import __EMAIL_ADRESS__, __EMAIL_PASSWORD__
from contact import Contact
from file import File


# Class gérant la gestion de l'envoi des emails
class Mail:
    def __init__(self, file: File):
        self.port = 587
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = __EMAIL_ADRESS__
        self.password = __EMAIL_PASSWORD__
        self.file = file.name

    # Connection au serveut SMTP de Google avec credentials dans constants.py
    def connect(self):
        server = smtplib.SMTP(self.smtp_server_domain_name, self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.sender_mail, self.password)
        return server

    # Computation de l'objet de l'email avec les infos disponibles
    def compute_subject(self, name):
        return (name + " : Informations à propos du fichier : " + self.file)

    # Computation du corps de l'email avec les infos disponibles
    def compute_message(self, state, lines_count=0):
        if state:
            if lines_count != 0:
                return (str(lines_count) +
                        " lignes ont été supprimées pour traiter le fichier " +
                        self.file + " avec réussite.")
            else:
                return ("Le traitement du fichier " + self.file +
                        " a été effectué avec réussite.")
        else:
            return ("Le fichier " + self.file +
                    " n'a pas été traité suite à une erreur de structure")

    # Envoi d'un message de succès avec indication du nombres de lignes
    def send_success_message(self, recipients: list[Contact], deleted_lines=0):
        for recipient in recipients:
            server = self.connect()
            msg = EmailMessage()
            msg.set_content(self.compute_message(True, deleted_lines))
            msg['Subject'] = self.compute_subject(recipient.name)
            msg['From'] = self.sender_mail
            msg['To'] = recipient.email
            server.send_message(msg)
            server.quit()
            print('Un email de succès a été envoyé à ', recipient.name)

    # Envoi d'un message d'echec dans le cas d'un problème de traitement
    def send_failed_message(self, recipients: list[Contact]):
        for recipient in recipients:
            server = self.connect()
            msg = EmailMessage()
            msg.set_content(self.compute_message(False))
            msg['Subject'] = self.compute_subject(recipient.name)
            msg['From'] = self.sender_mail
            msg['To'] = recipient.email
            server.send_message(msg)
            server.quit()
            print('Un email triste a été envoyé à ', recipient.name)