"""This module executes actions."""
import Passwd as pwd
import Usuario as u

def create_username(username, password):
    """executes create user action"""
    if pwd.validatePwd(password):
        u.add_user(username, password)

def print_user_list():
    """imprime la lista de usuarios"""
    print( u.show_users())

def ask_user_information():
    inputUsername = input("Ingrese el nuevo usuario:\n")
    inputPassword1 = input("Ingrese el password del usuario: "+inputUsername+"\n")
    inputPassword2 = input("Confirme el password del usuario: "+inputUsername+"\n")
    if inputPassword1 == inputPassword2:
        create_username(inputUsername, inputPassword1)
    else:
        print("Las contrasenhas no coinciden, por favor intentelo de nuevo")
        ask_user_information()

def ask_y_n(message):
    """Imprime mensajes Yes/No y retorna true o false repectivamente"""
    answer = input(message+" (y/n): ").lower()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        ask_y_n(message)


def edit_user():
    """Edita informacion de usuario"""
    user = input("Ingrese el usuario que desea modificar: ")
    if u.check_if_user_exists(user) == "True":
        print("El usuario ingresado no existe, intentelo nuevamente")
    else:
        if ask_y_n("Desea modificar el nombre de usuario?"):
            username = input("Ingrese el nuevo nombre de usuario:\n ")
            u.update_username(user, username)

        if ask_y_n("Desea modificar el password del usuario?"):
            password1 = input("Ingrese el nuevo password de usuario:\n ")
            if pwd.validatePwd(password1):
                password2 = input("Confirme el nuevo password de usuario:\n ")
                if password1 == password2:
                    u.update_password(user, password1)            
        else:
            print("No se ha realizado ningun cambio al usuario.\n ")

def delete_user():
    user = input("Ingrese el usuario que desea eliminar: ")
    if u.check_if_user_exists(user) == "True":
        print("El usuario ingresado no existe, intentelo nuevamente")
    else:
        if ask_y_n("Seguro que desea eliminar el usuario: "+user+"?"):            
            u.delete_user(user)
        else:
            print("No se ha ejecutado ningun cambio al usuario "+user+" \n")



def main():
    choice = '0'
    while choice == '0':
        print("****Menu Usuarios Administrativos****\n Seleccione la Accion que desea realizar")
        print("1. Crear usuario")
        print("2. Editar Usuario")
        print("3. Eliminar Usuario")
        print("4. Listar Usuarios")
        print("5. to go to another menu")
        print("0. Salir")

        choice = input ("\nDigite su opcion:")
        try:
            val = int(choice)
        except ValueError:
                print("\nValor ingresado no corresponde a ninguna opcion, por favor intentelo de nuevo\n\n")
                main()

        
        if choice == "5":
            print("Go to another menu")
            second_menu()
        elif choice == "4":
            print_user_list()
            print("Digite \"Enter\" para continuar: ")
            input()
            main()
        elif choice == "3":            
            delete_user()            
            print("Digite \"Enter\" para continuar: ")
            input()
            main()
        elif choice == "2":
            edit_user()
            print("Digite \"Enter\" para continuar: ")
            input()
            main()
        elif choice == "1":
            ask_user_information()
            print("Bienvenido")
            print("Digite \"Enter\" para continuar: ")
            main()
        elif choice == "0":
            print("Gracias por preferirnos\n")
            exit()
        else:
            print("\nValor ingresado no corresponde a ninguna opcion, por favor intentelo nuevamente\n")
            main()
            
        

def second_menu():
    print("This is the second menu")

main()

#print_user_list()
#print(u.check_password("Raptor2017++", "$pbkdf2-sha256$20000$mZOyllLqPQcghHCOsfbeOw$qU5Ft.J2se.x/WEez.QwF4Gele9x9sL6jEvKvOOkxNg"))

#input()
        