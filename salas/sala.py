'''from cines import cines'''

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
                    

'''if __name__ == "__main__":
    
    salass = {}
    sala = salas("sala 1", "paseo de las flores", 10, 10, salass)


    sala = salas("sala 1", "paseo de las flores", 10, 10)
    print(sala.get_nombre())
    sala.set_salas({"pelicula 1" : [{'pancho': []}]})
    print(sala.get_salas())
    sala.set_editar_salas_nombre("sala 1", "sala 2")
    print(sala.get_salas())
    sala.set_editar_salas_cine("sala 2", "paseo")
    print(sala.get_salas())
    sala.set_editar_salas_capacidadT("sala 2", 28)
    print(sala.get_salas())
    sala.set_borrarcine("sala 2")
    print(sala.get_salas())'''

