import os
from Passwd import Passwd
import Usuario
import sendgrid
from sendgrid.helpers.mail import *

class UsuarioFinal(Usuario):

    def __init__(self):
        """Hereda la clase"""
        Usuario.__init__()
        """Inicializa la clase"""
        self.FINALUSERLOGINS = {
            "pablo": ["pablo", 1234, "Pablo", "Rosales", "0102 0304 0506", "12/21", "345"]
        }

    

    def send_mail(self):
        # using SendGrid's Python Library
        # https://github.com/sendgrid/sendgrid-python
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("info@proyectoulacit.com")
        to_email = Email("pablo2412@gmail.com")
        subject = "Sending with SendGrid is Fun"
        content = Content("text/plain", "and easy to do anywhere, even with Python")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)


