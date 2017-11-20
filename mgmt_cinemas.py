from usuario.Passwd import Passwd
from usuario.Usuario import Usuario
from cartelera.carteleras import carteleras
from horario.horarios import horarios
from cines.cine import cine
from salas.sala import sala

#####////////////Funciones de usuario
"""This module executes actions."""

def create_username(username, password):
    """executes create user action"""
    if pwd.validatePwd(password):
        u.add_user(username, password)


def print_user_list():
    """imprime la lista de usuarios"""
    print(u.show_users())


def ask_user_information():
    inputUsername = input("Ingrese el nuevo usuario:\n")
    inputPassword1 = input("Ingrese el password del usuario: " + inputUsername + "\n")
    inputPassword2 = input("Confirme el password del usuario: " + inputUsername + "\n")
    if inputPassword1 == inputPassword2:
        create_username(inputUsername, inputPassword1)
    else:
        print("Las contrasenhas no coinciden, por favor intentelo de nuevo")
        ask_user_information()


def ask_y_n(message):
    """Imprime mensajes Yes/No y retorna true o false repectivamente"""
    answer = input(message + " (y/n): ").lower()
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
            return True
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
        if ask_y_n("Seguro que desea eliminar el usuario: " + user + "?"):
            u.delete_user(user)
        else:
            print("No se ha ejecutado ningun cambio al usuario " + user + " \n")


def main():
    choice = '0'
    while choice == '0':
        print("****Menu Usuarios Administrativos****\n Seleccione la Accion que desea realizar")
        print("1. Crear usuario")
        print("2. Editar Usuario")
        print("3. Eliminar Usuario")
        print("4. Listar Usuarios")
        print("5. Crear nuevo Usuario Final")
        print("6. Reiniciar password Usuario Final")
        print("7. Listar Usuarios Finales")

        print("0. Salir")

        choice = input("\nDigite su opcion:")
        try:
            val = int(choice)
        except ValueError:
            print("\nValor ingresado no corresponde a ninguna opcion, por favor intentelo de nuevo\n\n")
            main()

        if choice == "7":
            print(u.show_final_users())
            print("Digite \"Enter\" para continuar: ")
            input()
            main()
        elif choice == "6":
            username = input("Digite el usuario al que desea reiniciarle el password\n")
            u.final_user_pass_generate(username)
            print("Digite \"Enter\" para continuar: ")
            input()
            main()
        elif choice == "5":
            username = input("Digite el usuario que desea agregar\n")
            password = input("Digite el password del usuario " + username + "\n")
            confirm_password = input("Repita el password del usuario " + username + "\n")
            if password != confirm_password:
                print("Los passwords no coinciden, por favor intentelo nuevamente")
                print("Digite Enter para continuar\n")
                input()
                main()
            name = input("Digite el nombre del usuario " + username + "\n")
            lastname = input("Digite el apellido del usuario " + username + "\n")
            mail = input("Digite el correo del usuario " + username + "\n")
            card_number = input("Digite el numero de tarjeta del usuario " + username + "\n")
            card_exp = input("Digite la fecha de expiracion de la tarjeta del usuario " + username + "\n")
            cvn = input("Digite el codigo de tarjeta del usuario " + username + "\n")
            u.add_final_user(username, password, name, lastname, mail, card_number, card_exp, cvn)
            print("Digite \"Enter\" para continuar: ")
            input()
            main()
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

#####////////////Fin de usuario

##Validacion de usuario
def login(usuario, passwd):
    # pablo, Ulacit2017++
    if u.validate_login(usuario, passwd):
        run_app()

def run_app():

    ciness = {"paseo": ["paseo", "costa rica", "heredia", "heredia",[{"sala 1": ["sala 1", "paseo", "25", "25", [{"thor": ["thor", "2 hora", " accion", "+18", [{"1:00 PM": ["1:00 PM", "3:00 PM", "sala 1"] }] ]}] ]} ] ] }

    salass = {}
    horario = {}

    cin = cine("", "", "", "", ciness)
    sal = sala("", "", "", "", salass)
    cartele = carteleras('', '', '', '')
    hor = horarios("", "", horario)

    choice = '0'
    while choice == '0':
        print("****Menu Usuarios Administrativos****\n Seleccione la Accion que desea realizar")
        print("1. Modulo Usuarios")
        print("2. Modulo de Complejos de Cines")
        print("3. Modulo de Carteleras")

        print("0. Salir")

        choice = input("\nDigite su opcion:")
        try:
            val = int(choice)
        except ValueError:
            print("\nValor ingresado no corresponde a ninguna opcion, por favor intentelo de nuevo\n\n")
            main()

        if choice == "3":
            ##se ejecuta funcion de opcion 3
            '''menu de cines'''
            while True:
                texto = "\n\n\n Bienvenidos al complejo de cines \n\n\n 1- Creacion de cines \
                    \n 2- Edicion de cines \n 3- Lista de cines \
                    \n 4- Eliminacion de cines \n 5- Salir \n\n Ingrese el numero de cual opcion de sea: "
                
                try:
                    menu = int(input(texto))
                    if menu == 1:
                        try:
                            numero = int(input('Ingrese el numero de cines que desea agregar: '))
                            for x in range(numero): 
                                nombre = input('Ingrese el nombre del cine: ')
                                pais = input('Ingrese el pais donde se hubica el cine: ')
                                ciudad = input('Ingrese la ciudad donde se hubica el cine: ')
                                direccion = input('Ingrese la direccion donde se hubica el cine: ')
                                cin = cine(nombre, pais, ciudad, direccion, ciness)
                                try:
                                    numero2 = int(input('Ingrese el numero de salas que desea agregar en el cine ' + nombre + ': '))
                                    for y in range(numero2):
                                        nombre2 = input('Ingrese el nombre de la sala: ')
                                        total = input('Ingrese la capacidad total de la sala: ')
                                        disponibles = input('Ingrese la capacidad disponibles de la sala: ')
                                        sal = sala(nombre2, nombre, total, disponibles, salass)
                                        sal.set_salas({})
                                    cin.set_cine(salass)
                                    salass = {}
                                except ValueError:
                                    print("tiene que ingresar solamente numeros")
                            print(cine.get_cine())
                        except ValueError:
                            print("tiene que ingresar solamente numeros")

                    elif menu == 2:

                        texto2 = "\n\n\n Bienvenidos al editar de cines \n\n\n 1- Ediccion de nombre del cine \
                        \n 2- Ediccion de pais del cines \n 3- Ediccion de ciudad del cines \
                        \n 4- Ediccion de direccion del cines \n\n Ingrese el numero de cual opcion de sea: "

                        menu2 = int(input(texto2))

                        nombrecine = input('Ingrese el nombre del cine que desea editar: ')
                        if menu2 == 1:
                            nombre = input('Ingrese el nuevo nombre del cine: ')
                            cin.set_editar_nombre_cines(nombrecine, nombre)

                        elif menu2 == 2:

                            nombre = input('Ingrese el pais del cine: ')
                            cin.set_editar_pais_cines(nombrecine, nombre)

                        elif menu2 == 3:

                            nombre = input('Ingrese la ciudad del cine: ')
                            cin.set_editar_nombre_cines(nombrecine, nombre)

                        elif menu2 == 4:
                                
                            nombre = input('Ingrese la nueva direccion del cine: ')
                            cin.set_editar_nombre_cines(nombrecine, nombre)

                        else:
                            print("Ninguna opcion validad")
                        
                    elif menu == 3:

                        if len(cin.get_cine()) == 0:
                                print(" No existen cines, porfavor agrege 1")
                        else: 
                            print(cin.get_cine())

                            texto3 = "\n\n\n Bienvenidos al ver salas de cines \n\n\n 1- Lista de salas \n 2- Edicion de salas \
                            \n 3- Borrar de salas \n \n  Ingrese el numero de cual opcion de sea: "

                            try:
                                menu3 = int(input(texto3))

                                if menu3 == 1:
                                    nombre = input('Ingrese el nombre del cine al que desea ver las salas: ')
                                    print(sal.get_salas(ciness, nombre))
                                elif menu3 == 2:

                                    texto4 = "\n\n\n Bienvenidos al editar salas de cines \n\n\n 1- Ediccion de nombre de la sala \
                                    \n 2- Ediccion del nombre del cine de la sala \n 3- Ediccion de la capacidad total de la sala \
                                    \n 4- Ediccion de la capacidad disponible de la sala \n\n Ingrese el numero de cual opcion de sea: "
                                        
                                    try:
                                        menu4 = int(input(texto4))

                                        nombrecine = input('Ingrese el nombre del cine al que se va a editar: ')
                                        nombresala = input('Ingrese el nombre de la sala que desea editar: ')
                                        
                                        if menu4 == 1:
                                            nombre = input('Ingrese el nuevo nombre de la sala: ')
                                            sal.set_editar_salas_nombre(nombresala, nombre, ciness, nombrecine)
                                        elif menu4 == 2:
                                            nombre = input('Ingrese el nombre del cine de la sala: ')
                                            sal.set_editar_salas_cine(nombresala, nombre, ciness, nombrecine)
                                        elif menu4 == 3:
                                            num = int(input('Ingrese la capacidad total de la sala: '))
                                            sal.set_editar_salas_capacidadT(nombresala, num, ciness, nombrecine)
                                        elif menu4 == 4:
                                            num = int(input('Ingrese la capacidad disponible de la sala: '))
                                            sal.set_editar_salas_capacidadD(nombresala, num, ciness, nombrecine)
                                        else:
                                            print("Ninguna opcion validad")
                                        
                                    except ValueError:
                                        print("tiene que ingresar solamente numeros")

                                elif menu3 == 3:
                                    nombrecine = input('Ingrese el nombre del cine al que se va a borrar: ')
                                    nombre = input('Ingrese el nombre de la sala que desea borrar: ')
                                    sal.set_borrarsalascine(nombre, ciness, nombrecine)
                                else:
                                    print('no hizo ninguna opcion')
                            except ValueError:
                                print("tiene que ingresar solamente numeros")

                    elif menu == 4:
                        nombre = input('Ingrese el nombre del cine que desea borrar: ')
                        cin.set_borrarcine(nombre)

                    elif menu == 5:
                        print("salio")
                        break

                    else:
                        print("ingrese un numero valido")
                except ValueError:
                    print("tiene que ingresar solamente numeros")
        elif choice == "2":
            ##se ejecuta funcion de opcion 2
            ''' menu de carteleras '''
            while True:
                texto = "\n\n\n Bienvenidos a la cartelera de cines \n\n\n 1- Creacion de carteleras \
                    \n 2- Edicion de cartelera \n 3- Lista de carteleras \
                    \n 4- Eliminacion de carteleras \n 5- Salir \n\n Ingrese el numero de cual opcion de sea: "
                
                try:
                    menu = int(input(texto))
                    if menu == 1:
                        try:
                            numero = int(input('Ingrese el numero de carteleras que desea agregar: '))
                            for x in range(numero): 
                                nombre = input('Ingrese el nombre del cine al que se va agregar la pelicula: ')
                                nombre2 = input('Ingrese el nombre de la sala al que se va agregar la pelicula: ')
                                nombre3 = input('Ingrese el nombre de la pelicula: ')
                                duracion = input('Ingrese la duracion de la pelicula: ')
                                descripcion = input('Ingrese la descripcion de la pelicula: ')
                                restriccion = input('Ingrese la restricciones de la pelicula: ')
                                cartele = carteleras(nombre3, duracion, descripcion, restriccion)
                                try:
                                    numero2 = int(input('Ingrese el numero de horas que desea agregar en la pelicula ' + nombre3 + ': '))
                                    for y in range(numero2):
                                        nombre4 = input('Ingrese ingrese la hora de inicio para la pelicula ' + nombre3 + ': ')
                                        nombre5 = input('Ingrese ingrese la hora de fin para la pelicula ' + nombre3 + ': ')
                                        hor = horarios(nombre4, nombre5, horario)
                                        hor.set_horarios2(nombre2)
                                    
                                    cartele.set_cartelera(horario, ciness, nombre, nombre2)
                                    horario = {}
                                except ValueError:
                                    print("tiene que ingresar solamente numeros")
                            print(ciness)
                        except ValueError:
                            print("tiene que ingresar solamente numeros")

                    elif menu == 2:

                        texto2 = "\n\n\n Bienvenidos al editar de cartelera \n\n\n 1- Ediccion de nombre de la cartelera \
                            \n 2- Ediccion de la duracion de la cartelera \n 3- Ediccion de la descripcion de la cartelera \
                            \n 4- Ediccion de la restricciones de la cartelera \n\n Ingrese el numero de cual opcion de sea: "

                        menu2 = int(input(texto2))

                        nombrecine = input('Ingrese el nombre del cine que desea editar de la cartelera: ')
                        nombresala = input('Ingrese el nombre de la sala que desea editar de la cartelera: ')
                        nombrepelicula = input('Ingrese el nombre de la pelicula que desea editar de la cartelera: ')
                        if menu2 == 1:
                            nombre = input('Ingrese el nuevo nombre de la pelicula: ')
                            cartele.set_editar_nombre_cartelera(nombrepelicula, nombre, ciness, nombrecine, nombresala)

                        elif menu2 == 2:

                            nombre = input('Ingrese la nueva duracion de la pelicula ' + nombrepelicula + ': ')
                            cartele.set_editar_duracion_cartelera(nombrepelicula, nombre, ciness, nombrecine, nombresala)

                        elif menu2 == 3:

                            nombre = input('Ingrese la nueva descripcion de la pelicula ' + nombrepelicula + ': ')
                            cartele.set_editar_descripcion_cartelera(nombrepelicula, nombre, ciness, nombrecine, nombresala)

                        elif menu2 == 4:
                                
                            nombre = input('Ingrese la nueva restriccion de la pelicula ' + nombrepelicula + ': ')
                            cartele.set_editar_restricciones_cartelera(nombrepelicula, nombre, ciness, nombrecine, nombresala)

                        else:
                            print("Ninguna opcion validad")
                        
                    elif menu == 3:
                        if len(cin.get_cine()) == 0:
                                print(" No existen cines, porfavor agrege 1")
                        else: 
                            nombre = input('Ingrese el nombre del cine al que se va a ver la cartelera: ')
                            nombre2 = input('Ingrese el nombre de la sala al que se va a ver la pelicula: ')
                            cartele.get_cartelera(ciness, nombre, nombre2)

                            texto3 = "\n\n\n Bienvenidos al ver horarios de peliculas \n\n\n 1- Lista de horarios \n 2- Edicion de horarios \
                                \n 3- Borrar de horarios \n \n  Ingrese el numero de cual opcion de sea: "

                            try:
                                menu3 = int(input(texto3))

                                if menu3 == 1:
                                    nombrecine = input('Ingrese el nombre del cine al que desea ver el horario: ')
                                    nombresala = input('Ingrese el nombre de la sala al que desea ver el horario: ')
                                    nombrepelicula = input('Ingrese el nombre de la pelicula que desea ver el horario: ')
                                    hor.get_horarios(ciness, nombrecine, nombresala, nombrepelicula)
                                elif menu3 == 2:

                                    texto4 = "\n\n\n Bienvenidos al editar horario de peliculas \n\n\n 1- Ediccion de hora inicio de la pelicula \
                                        \n 2- Ediccion del hora fin de la pelicula \n 3- Ediccion de la sala de la pelicula \
                                        \n\n Ingrese el numero de cual opcion de sea: "
                                        
                                    try:
                                        menu4 = int(input(texto4))

                                        nombrecine = input('Ingrese el nombre del cine al que se va a editar el horario: ')
                                        nombresala = input('Ingrese el nombre de la sala que se va a editar el horario: ')
                                        nombrepelicula = input('Ingrese el nombre de la pelicula que desea editar el horario: ')
                                        hora = input('Ingrese la hora de la pelicula que desea editar: ')
                                        
                                        if menu4 == 1:
                                            nombre = input('Ingrese la nueva hora de inicio de la pelicula ' + nombrepelicula + ': ')
                                            hor.set_editar_horainicio_pelicula(hora, nombre, ciness, nombrecine, nombresala, nombrepelicula)
                                        elif menu4 == 2:
                                            nombre = input('Ingrese la nueva hora fin de la pelicula ' + nombrepelicula + ': ')
                                            hor.set_editar_horafin_pelicula(hora, nombre, ciness, nombrecine, nombresala, nombrepelicula)
                                        elif menu4 == 3:
                                            nombre = input('Ingrese el nombre de la nueva sala de la pelicula ' + nombrepelicula + ': ')
                                            hor.set_editar_sala_pelicula(hora, nombre, ciness, nombrecine, nombresala, nombrepelicula)
                                        else:
                                            print("Ninguna opcion validad")
                                    
                                    except ValueError:
                                        print("tiene que ingresar solamente numeros")

                                elif menu3 == 3:
                                    nombrecine = input('Ingrese el nombre del cine al que se va a borrar el horario: ')
                                    nombresala = input('Ingrese el nombre de la sala que se va a borrar el horario: ')
                                    nombrepelicula = input('Ingrese el nombre de la pelicula que desea borrar el horario: ')
                                    hora = input('Ingrese la hora de la pelicula que desea borrar: ')
                                    hor.set_borrarhorapelicula(hora, ciness, nombrecine, nombresala, nombrepelicula)
                                else:
                                    print('no hizo ninguna opcion')
                            except ValueError:
                                print("tiene que ingresar solamente numeros")

                    elif menu == 4:
                        nombre = input('Ingrese el nombre del cine que desea borrar la pelicula: ')
                        nombre2 = input('Ingrese el nombre de la sala que desea borrar la pelicula: ')
                        nombre3 = input('Ingrese el nombre la pelicula que desea borrar: ')
                        cartele.set_borrarpeliula(nombre3, ciness, nombre, nombre2)

                    elif menu == 5:
                        print("salio")
                        break

                    else:
                        print("ingrese un numero valido")
                except ValueError:
                    print("tiene que ingresar solamente numeros")
        elif choice == "1":
            print("Bienvenido")
            print("Digite \"Enter\" para continuar: ")
            main()
        elif choice == "0":
            print("Gracias por preferirnos\n")
            exit()
        else:
            print("\nValor ingresado no corresponde a ninguna opcion, por favor intentelo nuevamente\n")
            main()

print("Por favor ingrese sus credenciales para Ingresar al Sistema\n")
usuario = input("Digite su nombre de usuario\n")
passwd = input("Ingrese su password\n")
pwd = Passwd()
u = Usuario()
login(usuario, passwd)
##