class sala():
    def __init__(self, nombre, cine, capacidadtotal, capacidaddisponible, lista):
        self.nombres = nombre
        self.cine = cine
        self.capacidadT = capacidadtotal
        self.capacidadD = capacidaddisponible
        self.sala = lista
        self.peliculas = {}

    '''funcion que retorna el nombre de la sala'''
    def get_nombre(self):
        return self.nombres

    '''funcion que retorna el nombre del cine en la sala'''
    def get_cine(self):
        return self.cine

    '''funcion que retorna la capacidad total de la sala'''
    def get_capacidad_total(self):
        return self.capacidadT

    '''funcion que retorna la capacidad disponible de la sala'''
    def get_capacidad_disponible(self):
        return self.capacidadD

    '''funcion que retorna el nombre de las llaves de la sala por cines'''
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

    '''funcion que retorna las sala por diccionario'''
    def get_salasCompletas(self): 
        return (self.sala)

    '''funcion que crea las sala'''
    def set_salas(self, peliculas):
        self.peliculas = peliculas
        datos = []
        datos.append(self.nombres)
        datos.append(self.cine)
        datos.append(self.capacidadT)
        datos.append(self.capacidadD)
        datos.append(self.peliculas)
        self.sala.setdefault(self.nombres, datos)

    '''funcion que edita el nombre del cine de la sala'''
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

    '''funcion que edita la capacidad total de la sala'''
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

    '''funcion que edita la capacidad disponible de la sala'''
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
        
    '''funcion que edita el nombre de la sala'''
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

    '''funcion que borra la sala'''      
    def set_borrarsalascine(self, nombre, cines, nombrecine):
        for x in cines.keys():
            if x == nombrecine:
                for x in cines[nombrecine][4]:
                    if x == nombre:
                        del(cines[nombrecine][4][nombre]) 
                        break
            break
  