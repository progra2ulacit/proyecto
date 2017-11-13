from passlib.hash import pbkdf2_sha256

class Usuario():
    """Modulo usuario para control de accinoes de usuario"""
    

    def __init__(self):
        """Inicializa la clase"""
        self.USERLOGINS = {
            "pablo": ["pablo", 1234]
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
            #aqui se envia a la opcion interna de salas o carteleras
            