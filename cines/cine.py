
class cine():
    def __init__(self, nombre, pais, ciudad, direccion, cines):
        self.nombres = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.direccion = direccion
        self.cines = cines
        self.sala = {}
    '''funcion que retorna el nombre del cine'''
    def get_nombre(self):
        return self.nombres

    '''funcion que retorna la sala del cine'''
    def get_pais(self):
        return self.pais

    '''funcion que retorna la ciudad del cine'''
    def get_ciudad(self):
        return self.ciudad

    '''funcion que retorna la direccion del cine'''
    def get_direccion(self):
        return self.direccion

    '''funcion que retorna todos las llaves de los cines'''
    def get_cine(self):
        string = ""
        if len(self.cines) != 0:
            for x in self.cines.keys():
                string += x + "\n" 
        return string

    '''funcion que retorna la lista de los cines con salas incluidas y peliculas y horarios'''
    def get_cineCompleto(self): 
        return self.cines

    '''funcion que crea el cine y la sala'''
    def set_cine(self, sala):
        self.sala = sala
        datos = []
        datos.append(self.nombres)
        datos.append(self.pais)
        datos.append(self.ciudad)
        datos.append(self.direccion)
        datos.append(self.sala)
        self.cines.setdefault(self.nombres, datos)

    '''funcion que edita el nombre del cine'''   
    def set_editar_nombre_cines(self, nombrecine, editado):
        datos = []
        for x in self.cines.keys():
            if x == nombrecine:
                valor = self.cines.pop(nombrecine) 
                datos.append(editado)
                datos.append(valor[1])
                datos.append(valor[2])
                datos.append(valor[3])
                datos.append(valor[4])
                self.cines.setdefault(editado, datos)

    '''funcion que edita el pais del cine'''
    def set_editar_pais_cines(self, nombrecine, editado):
        datos = []
        for x in self.cines.keys():
            if x == nombrecine:
                valor = self.cines.pop(nombrecine) 
                datos.append(valor[0])
                datos.append(editado)
                datos.append(valor[2])
                datos.append(valor[3])
                datos.append(valor[4])
                self.cines.setdefault(nombrecine, datos)
                break

    '''funcion que edita la ciudad del cine'''
    def set_editar_ciudad_cines(self, nombrecine, editado):
        datos = []
        for x in self.cines.keys():
            if x == nombrecine:
                valor = self.cines.pop(nombrecine) 
                datos.append(valor[0])
                datos.append(valor[1])
                datos.append(editado)
                datos.append(valor[3])
                datos.append(valor[4])
                self.cines.setdefault(nombrecine, datos)
                break
    
    '''funcion que edita la direccion del cine'''
    def set_editar_direccion_cines(self, nombrecine, editado):
        datos = []
        vas = 0
        for x in self.cines.keys():
            if x == nombrecine:
                valor = self.cines.pop(nombrecine) 
                datos.append(valor[0])
                datos.append(valor[1])
                datos.append(valor[2])
                datos.append(editado)
                datos.append(valor[4])
                self.cines.setdefault(nombrecine, datos)
                break
    
    '''funcion que borra el cine'''
    def set_borrarcine(self, nombre):
        for x in self.cines.keys():
            if x == nombre:
                del(self.cines[nombre]) 
                break
            else:
                print('no existe') 


if __name__ == "__main__":

    ciness = {}
    salass = {}
    cine = cine("", "", "", "", ciness)
    sala = sala("", "", "", "", salass)
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
                        cine = cines(nombre, pais, ciudad, direccion, ciness)
                        try:
                            numero2 = int(input('Ingrese el numero de salas que desea agregar en el cine ' + nombre + ': '))
                            for y in range(numero2):
                                nombre2 = input('Ingrese el nombre de la sala: ')
                                total = input('Ingrese la capacidad total de la sala: ')
                                disponibles = input('Ingrese la capacidad disponibles de la sala: ')
                                sala = salas(nombre2, nombre, total, disponibles, salass)
                                sala.set_salas({})
                            cine.set_cine(salass)
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
                    cine.set_editar_nombre_cines(nombrecine, nombre)

                elif menu2 == 2:

                    nombre = input('Ingrese el pais del cine: ')
                    cine.set_editar_pais_cines(nombrecine, nombre)

                elif menu2 == 3:

                    nombre = input('Ingrese la ciudad del cine: ')
                    cine.set_editar_nombre_cines(nombrecine, nombre)

                elif menu2 == 4:
                    
                    nombre = input('Ingrese la nueva direccion del cine: ')
                    cine.set_editar_nombre_cines(nombrecine, nombre)

                else:
                    print("Ninguna opcion validad")
            
            elif menu == 3:

                if len(cine.get_cine()) == 0:
                    print(" No existen cines, porfavor agrege 1")
                else: 
                    print(cine.get_cine())

                    texto3 = "\n\n\n Bienvenidos al ver salas de cines \n\n\n 1- Lista de salas \n 2- Edicion de salas \
                    \n 3- Borrar de salas \n \n  Ingrese el numero de cual opcion de sea: "

                    try:
                        menu3 = int(input(texto3))

                        if menu3 == 1:
                            nombre = input('Ingrese el nombre del cine al que desea ver las salas: ')
                            print(sala.get_salas(ciness, nombre))
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
                                    sala.set_editar_salas_nombre(nombresala, nombre, ciness, nombrecine)
                                elif menu4 == 2:
                                    nombre = input('Ingrese el nombre del cine de la sala: ')
                                    sala.set_editar_salas_cine(nombresala, nombre, ciness, nombrecine)
                                elif menu4 == 3:
                                    num = int(input('Ingrese la capacidad total de la sala: '))
                                    sala.set_editar_salas_capacidadT(nombresala, num, ciness, nombrecine)
                                elif menu4 == 4:
                                    num = int(input('Ingrese la capacidad disponible de la sala: '))
                                    sala.set_editar_salas_capacidadD(nombresala, num, ciness, nombrecine)
                                else:
                                    print("Ninguna opcion validad")
                            
                            except ValueError:
                                print("tiene que ingresar solamente numeros")

                        elif menu3 == 3:
                            nombrecine = input('Ingrese el nombre del cine al que se va a borrar: ')
                            nombre = input('Ingrese el nombre de la sala que desea borrar: ')
                            sala.set_borrarsalascine(nombre, ciness, nombrecine)
                        else:
                            print('no hizo ninguna opcion')
                    except ValueError:
                        print("tiene que ingresar solamente numeros")

            elif menu == 4:
                nombre = input('Ingrese el nombre del cine que desea borrar: ')
                cine.set_borrarcine(nombre)

            elif menu == 5:
                print("salio")
                break

            else:
                print("ingrese un numero valido")
        except ValueError:
            print("tiene que ingresar solamente numeros")

