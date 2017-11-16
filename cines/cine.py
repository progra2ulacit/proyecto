from salas import salas
class cines():
    def __init__(self, nombre, pais, ciudad, direccion, cines):
        self.nombres = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.direccion = direccion
        self.cines = cines
        self.sala = {}

    def get_nombre(self):
        return self.nombres

    def get_pais(self):
        return self.pais

    def get_ciudad(self):
        return self.ciudad

    def get_direccion(self):
        return self.direccion

    def get_cine(self):
        string = ""
        if len(self.cines) != 0:
            for x in self.cines.keys():
                string += x + "\n" 
        return string

    def get_cineCompleto(self): 
        return self.cines

    def set_cine(self, sala):
        self.sala = sala
        datos = []
        datos.append(self.nombres)
        datos.append(self.pais)
        datos.append(self.ciudad)
        datos.append(self.direccion)
        datos.append(self.sala)
        self.cines.setdefault(self.nombres, datos)
        
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
                
    def set_borrarcine(self, nombre):
        for x in self.cines.keys():
            if x == nombre:
                del(self.cines[nombre]) 
                break
            else:
                print('no existe') 
'''
class salas():
    def __init__(self, nombre, cine, capacidadtotal, capacidaddisponible, lista):
        self.nombres = nombre
        self.cine = cine
        self.capacidadT = capacidadtotal
        self.capacidadD = capacidaddisponible
        self.sala = lista
        self.peliculas = {}

    def get_nombre(self):
        return self.nombres

    def get_cine(self):
        return self.cine

    def get_capacidad_total(self):
        return self.capacidadT

    def get_capacidad_disponible(self):
        return self.capacidadD

    def get_salas(self, cine, nombrecine):
        string = ""
        if len(cine) != 0:
            for x in cine.keys():
                if x == nombrecine:
                    for y in cine[nombrecine][4]:
                        string += y + "\n" 
        else:
            string = "tiene que agregar un cine y sus salas"
        
        return string

    def get_salasCompletas(self): 
        return (self.sala)

    def set_salas(self, peliculas):
        self.peliculas = peliculas
        datos = []
        datos.append(self.nombres)
        datos.append(self.cine)
        datos.append(self.capacidadT)
        datos.append(self.capacidadD)
        datos.append(self.peliculas)
        self.sala.setdefault(self.nombres, datos)

    def set_editar_salas_cine(self, nombresala, editado, cines, nombrecine):
        dato = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[x][4]:
                    if y == nombresala:
                        valor = cines[x][4].pop(nombresala) 
                        dato.append(valor[0])
                        dato.append(editado)
                        dato.append(valor[2])
                        dato.append(valor[3])
                        dato.append(valor[4])
                        cines[x][4].setdefault(nombresala, dato)

    def set_editar_salas_capacidadT(self, nombresala, editado, cines, nombrecine):
        dato = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[x][4]:
                    if y == nombresala:
                        valor = cines[x][4].pop(nombresala) 
                        dato.append(valor[0])
                        dato.append(valor[1])
                        dato.append(editado)
                        dato.append(valor[3])
                        dato.append(valor[4])
                        cines[x][4].setdefault(nombresala, dato)

    def set_editar_salas_capacidadD(self, nombresala, editado, cines, nombrecine):
        dato = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[x][4]:
                    if y == nombresala:
                        valor = cines[x][4].pop(nombresala) 
                        dato.append(valor[0])
                        dato.append(valor[1])
                        dato.append(valor[2])
                        dato.append(editado)
                        dato.append(valor[4])
                        cines[x][4].setdefault(nombresala, dato)
        
    def set_editar_salas_nombre(self, nombresala, editado, cines, nombrecine):
        dato = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[x][4]:
                    if y == nombresala:
                        valor = cines[x][4].pop(nombresala) 
                        dato.append(editado)
                        dato.append(valor[1])
                        dato.append(valor[2])
                        dato.append(valor[3])
                        dato.append(valor[4])
                        
                        cines[x][4].setdefault(editado, dato)
                
    def set_borrarsalascine(self, nombre, cines, nombrecine):
        for x in cines.keys():
            if x == nombrecine:
                for x in cines[nombrecine][4]:
                    if x == nombre:
                        del(cines[nombrecine][4][nombre]) 
                        break
            break
                    
  '''      
if __name__ == "__main__":
    '''cine = cines("paseo", "costa rica", 'heredia', 'frente a la universidad latina de heredia')
    print(cine.get_nombre() + ' '+ cine.get_pais())
    cine.set_cine({'sala 1': {'pelicula': []}, "sala 2": {"pelicula": []}})
    print(cine.get_cine())
    cine.set_editar_nombre_cines("paseo", "paseo de las flores")
    print(cine.get_cine())
    cine.set_editar_ciudad_cines("paseo de las flores", "San Jose")
    print(cine.get_cine())
    cine.set_borrarcine("paseo de las flores")
    print(cine.get_cine())'''

    ciness = {}
    salass = {}
    cine = cines("", "", "", "", ciness)
    sala = salas("", "", "", "", salass)
    while True:
        texto = "\n\n\n Bienvenidos al complejo de cines \n\n\n 1- Creacion de cines \
        \n 2- Edicion de cines \n 3- Lista de cines \
        \n 4- Eliminacion de cines \n 5- Carteleras \n 6- Salir \n\n Ingrese el numero de cual opcion de sea: "
    
        try:
            menu = int(input(texto))
            if menu == 1:
                try:
                    numero = int(input('Ingrese el numero de cines que desea agregar: '))
                    for x in range(numero): 
                        nombre = input('Ingrese el nombre del cine: ')
                        cine = cines(nombre, "costa rica", 'heredia', 'frente a la universidad latina de heredia', ciness)
                        try:
                            numero2 = int(input('Ingrese el numero de salas que desea agregar en el cine ' + nombre + ': '))
                            for y in range(numero2):
                                nombre2 = input('Ingrese el nombre de la sala: ')
                                sala = salas(nombre2, nombre, 20, 10, salass)
                                sala.set_salas({})
                            cine.set_cine(salass)
                        except ValueError:
                            print("tiene que ingresar solamente numeros")
                    print(cine.get_cine())
                except ValueError:
                    print("tiene que ingresar solamente numeros")

            elif menu == 2:
                nombrecine = input('Ingrese el nombre del cine que desea editar: ')
                nombre = input('Ingrese el nuevo nombre del cine: ')
                cine.set_editar_nombre_cines(nombrecine, nombre)
            
            elif menu == 3:

                if len(cine.get_cine()) == 0:
                    print(" No existen cines, porfavor agrege 1")
                else: 
                    print(cine.get_cine())

                    texto2 = "\n\n\n 1- Lista de salas \n 2- Edicion de salas \
                    \n 3- Borrar de salas \n \n  Ingrese el numero de cual opcion de sea: "

                    try:
                        menu2 = int(input(texto2))

                        if menu2 == 1:
                            nombre = input('Ingrese el nuevo nombre del cine al que desea ver las salas: ')
                            print(sala.get_salas(ciness, nombre))
                        elif menu2 == 2:
                            nombrecine = input('Ingrese el nombre del cine al que se va a editar: ')
                            nombresala = input('Ingrese el nombre de la sala que desea editar: ')
                            nombre = input('Ingrese el nuevo nombre de la sala: ')
                            sala.set_editar_salas_nombre(nombresala, nombre, ciness, nombrecine)
                        elif menu2 == 3:
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

                break
            elif menu == 6:
                print("salio")
                break

            else:
                print("ingrese un numero valido")
        except ValueError:
            print("tiene que ingresar solamente numeros")

