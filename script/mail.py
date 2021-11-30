import requests

class Mail:

    def __init__(self, apikey, email_to):
        self.apikey = apikey
        self.email_to = email_to

    def send_message(self, subject):
        return requests.post(
            "https://api.mailgun.net/v3/sandbox91ef0ba9632b459c8e56c4ab5fdb6b59.mailgun.org/messages",
            auth=("api", self.apikey),
            data={"from": "CSV Server <postmaster@sandbox91ef0ba9632b459c8e56c4ab5fdb6b59.mailgun.org>",
                "to": self.email_to,
                "subject": subject,
                "text": "Congratulations Benoît Le Goff, you just sent an email with Mailgun!  You are truly awesome!"}
            )