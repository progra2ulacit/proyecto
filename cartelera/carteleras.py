class carteleras():
    def __init__(self, nombre, duracion, descripcion, restriccion):
        self.nombres = nombre
        self.duraciones = duracion
        self.descripciones = descripcion
        self.restricciones = restriccion
        self.carteleras = {}
        self.horarios = {}

        '''funcion que retorna el nombre de la cartelera'''
    def get_nombre(self):
        return self.nombres

    '''funcion que retorna la duracion de la cartelera'''
    def get_duracion(self):
        return self.duraciones

    '''funcion que retorna la descripcion de la cartelera'''
    def get_descripcion(self):
        return self.descripciones

    '''funcion que retorna la restriccion de la cartelera'''
    def get_restriccion(self):
        return self.restricciones

    '''funcion que retorna todos las llaves de la carteleras'''
    def get_cartelera(self, cines, nombrecine, nombresala):
        if len(cines) != 0:
            for x in cines.keys():
                if x == nombrecine:
                    for y in cines[nombrecine][4]:
                        for z in y.keys():
                            if z == nombresala:
                                for t in y[nombresala][4]:
                                    for a in t.keys():
                                        print(t[a][0])
        
    '''funcion que crea la cartelera'''
    def set_cartelera(self, horario, cines, nombrecine, nombresala):
        self.horarios = horario
        datos = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    va = t[a]
                                    self.carteleras.setdefault(a, va)
                            y[nombresala][4].pop(0)
                            
                            datos.append(self.nombres)
                            datos.append(self.duraciones)
                            datos.append(self.descripciones)
                            datos.append(self.restricciones)
                            datos.append(self.horarios)
                            self.carteleras.setdefault(self.nombres, datos)
                            y[nombresala][4].append(self.carteleras)
                            
    '''funcion que edita el nombre de la cartelera'''   
    def set_editar_nombre_cartelera(self, nombrepeli, editado, cines, nombrecine, nombresala):
        datos = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepeli:
                                        valor = t.pop(nombrepeli) 
                                        datos.append(editado)
                                        datos.append(valor[1])
                                        datos.append(valor[2])
                                        datos.append(valor[3])
                                        datos.append(valor[4])
                                        t.setdefault(editado, datos)

    '''funcion que edita la duracion de la cartelera'''
    def set_editar_duracion_cartelera(self, nombrepeli, editado, cines, nombrecine, nombresala):
        datos = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepeli:
                                        valor = t.pop(nombrepeli) 
                                        datos.append(valor[0])
                                        datos.append(editado)
                                        datos.append(valor[2])
                                        datos.append(valor[3])
                                        datos.append(valor[4])
                                        
                                        t.setdefault(nombrepeli, datos)

    '''funcion que edita la descripcion de la cartelera'''
    def set_editar_descripcion_cartelera(self, nombrepeli, editado, cines, nombrecine, nombresala):
        datos = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepeli:
                                        valor = t.pop(nombrepeli) 
                                        datos.append(valor[0])
                                        datos.append(valor[1])
                                        datos.append(editado)
                                        datos.append(valor[3])
                                        datos.append(valor[4])
                                        
                                        t.setdefault(nombrepeli, datos)
    
    '''funcion que edita la restriccion de la cartelera'''
    def set_editar_restricciones_cartelera(self, nombrepeli, editado, cines, nombrecine, nombresala):
        datos = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepeli:
                                        valor = t.pop(nombrepeli) 
                                        datos.append(valor[0])
                                        datos.append(valor[1])
                                        datos.append(valor[2])
                                        datos.append(editado)
                                        datos.append(valor[4])
                                        
                                        t.setdefault(nombrepeli, datos)
    
    '''funcion que borra la cartelera'''
    def set_borrarpeliula(self, nombrepeli, cines, nombrecine, nombresala):
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepeli:
                                        del(t[nombrepeli])
                                        break
