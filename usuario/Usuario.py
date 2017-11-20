from passlib.hash import pbkdf2_sha256
import sendgrid
import os
from sendgrid.helpers.mail import *
import string
import random
from itertools import islice

class Usuario():
    """Modulo usuario para control de accinoes de usuario"""
    

    def __init__(self):
        """Inicializa la clase"""
        self.USERLOGINS = {
            "pablo": ["pablo", "$pbkdf2-sha256$20000$/P8fA4CQEgKAECKkNKaUUg$8c00wy9i7Aj8U3WtLpzzJFhQ1XtaQfIifSypu00Q2SQ"]
        }
        self.FINALUSERLOGINS = {
            "pablo": ["pablo", "$pbkdf2-sha256$20000$/P8fA4CQEgKAECKkNKaUUg$8c00wy9i7Aj8U3WtLpzzJFhQ1XtaQfIifSypu00Q2SQ", "Pablo", "Rosales", "pablo2412@gmail.com","0102 0304 0506", "12/21", "345"]
        }


    """
        *
            getters y setters
        *
    """
    def get_userlogins(self):
        """Devuelve los usuarios del diccionario"""
        return self.USERLOGINS


    def set_userlogins(self):
        """configura"""
        self.USERLOGINS = {
            "pablo": ["pablo", 1234]
        }



    """
        *
            fin getters y setters
        *
    """
    def check_if_user_exists(self, username):
        """Verifica que el usuario exista"""
        return self.USERLOGINS.get(username, "True")
        


    def add_user(self, username, password):
        """Agrega un Usuario a la lista"""
        if(self.check_if_user_exists(username) == "True"):
            self.USERLOGINS[username] = [username, self.encode_password(password)]
            print ("El usuario ha sido creado exitosamente\n")
        else:
            print ("El nombre de usuario ya existe, por favor intente de nuevo\n")
            


    def show_users(self):
        """Devuelve la lista con todos los usuarios"""
        return self.USERLOGINS



    def encode_password(self, password):
        """codifica el password para almacenarlo"""
        hash = pbkdf2_sha256.encrypt(password, rounds=20000, salt_size=16)
        return hash



    def update_username(self, oldUsername, newUsername):
        """Actualiza el nombre de usuario seleccionado"""
        rl = self.USERLOGINS[oldUsername]    
        originalPassword = rl[1]
        nl = [newUsername, originalPassword]
        self.USERLOGINS.pop(oldUsername)
        self.USERLOGINS[newUsername] = [newUsername, originalPassword]
        print("Usuario actualizado correctamente")
        return True



    def update_password(self, username, newPassword):
        """Actualiza el password del usuario seleccionado"""
        rl = self.USERLOGINS[username]    
        hashedPwd = self.encode_password(newPassword)
        nl = [username, hashedPwd]
        self.USERLOGINS[username] = nl
        print("Usuario actualizado correctamente\n")
        return True



    def delete_user(self, username):
        del self.USERLOGINS[username]
        print("Usuario ha sido eliminado correctamente\n")



    def check_password(self, clear_password, password_hash):
        """valida que el password ingresado coincida con el que esta almacenado"""
        return pbkdf2_sha256.verify(clear_password, password_hash)

    
    def validate_login(self, username, password):
        if self.check_password(password, self.USERLOGINS[username][1]) == True:
            print("Se valido correctamente")
            return True
            #aqui se envia a la opcion interna de salas o carteleras
            
    """"Usuarios finales"""


    def add_final_user(self, username, password, name, lastname, mail, card_number, card_exp, cvn):
        """Agrega Usuario Final a la lista"""
        if(self.check_if_final_user_exists(username) == "True"):
            self.FINALUSERLOGINS[username] = [username, self.encode_password(password),name, lastname, mail, card_number, card_exp, cvn]
            print ("El usuario ha sido creado exitosamente\n")
            self.send_mail(name, lastname, mail, password, username, "Bienvenido al sistema de boleteria electronica")
        else:
            print ("El nombre de usuario ya existe, por favor intente de nuevo\n")



    def check_if_final_user_exists(self, username):
        """Verifica que el usuario final exista"""
        return self.FINALUSERLOGINS.get(username, "True")


    def show_final_users(self):
        """Devuelve la lista con todos los usuarios"""
        return self.FINALUSERLOGINS


    def final_user_pass_generator(self, size, chars = string.ascii_uppercase + string.digits):
        selection = iter(lambda: random.choice(chars), object())
        while True:
            yield ''.join(islice(selection, size))


    def final_user_pass_generate(self, username):
        random_gen = self.final_user_pass_generator(12)
        s =  next(random_gen)
        self.update_final_user_password(username, s)
        uv = self.FINALUSERLOGINS[username] 
        self.send_mail(uv[2], uv[3], uv[4], s, username, "Hemos reiniciado su password de forma temporal. ")

    def update_final_user_password(self, username, newPassword):
        """Actualiza el password del usuario seleccionado"""
        rl = self.FINALUSERLOGINS[username]    
        hashedPwd = self.encode_password(newPassword)
        nl = rl
        nl[1] = hashedPwd
        print("Usuario actualizado correctamente\n")
        return True


    def send_mail(self, name, lastname, email, password, username, mensaje):
        # using SendGrid's Python Library
        # https://github.com/sendgrid/sendgrid-python
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("info@proyectoulacit.com")
        to_email = Email(email)
        subject = "Bienvenido al sistema de boleteria de xxxxxxx"
        content = Content("text/plain", mensaje+". \n"+name+" "+lastname+", \n Su nombre de usuario es: "+username+"\n password: "+password)
        mail = Mail(from_email, subject, to_email, content)
        

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)

