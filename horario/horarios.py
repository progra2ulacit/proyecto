class horarios():
    def __init__(self, horainicio, horafin, horario):
        self.horaini = horainicio
        self.horafini = horafin
        self.horarios = horario

    '''funcion que retorna la hora de inicio de los horarios'''
    def get_horainicio(self):
        return self.horaini

    '''funcion que retorna la hora de fin de los horarios'''
    def get_horafin(self):
        return self.horafini

    '''funcion que retorna todos las llaves de los horarios'''
    def get_horarios(self, cines, nombrecine, nombresala, nombrepelicula):
        if len(cines) != 0:
            for x in cines.keys():
                if x == nombrecine:
                    for y in cines[nombrecine][4]:
                        for z in y.keys():
                            if z == nombresala:
                                for t in y[nombresala][4]:
                                    for a in t.keys():
                                        if a == nombrepelicula:
                                            for b in t[nombrepelicula][4]:
                                                for c in b.keys():
                                                    print(c)
        
    '''funcion que crea los horarios'''
    def set_horarios(self, nombresala):
        datos = []
        datos.append(self.horaini)
        datos.append(self.horafini)
        datos.append(nombresala)
        self.horarios.setdefault(self.horaini, datos)
                                                                   
    '''funcion que edita el hora inicio de la pelicula'''   
    def set_editar_horainicio_pelicula(self, hora, editado, cines, nombrecine, nombresala, nombrepelicula):
        datos = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepelicula:
                                        for b in t[nombrepelicula][4]:
                                            for c in b.keys():
                                                if c == hora:
                                                    valor = b.pop(hora) 
                                                    datos.append(editado)
                                                    datos.append(valor[1])
                                                    datos.append(valor[2])
                                                    b.setdefault(editado, datos)

    '''funcion que edita la hora fin de la pelicula'''
    def set_editar_horafin_pelicula(self, hora, editado, cines, nombrecine, nombresala, nombrepelicula):
        datos = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepelicula:
                                        for b in t[nombrepelicula][4]:
                                            for c in b.keys():
                                                if c == hora:
                                                    valor = b.pop(hora) 
                                                    datos.append(valor[0])
                                                    datos.append(editado)
                                                    datos.append(valor[2])
                                                    b.setdefault(hora, datos)

    '''funcion que edita la sala de la pelicula'''
    def set_editar_sala_pelicula(self, hora, editado, cines, nombrecine, nombresala, nombrepelicula):
        datos = []
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepelicula:
                                        for b in t[nombrepelicula][4]:
                                            for c in b.keys():
                                                if c == hora:
                                                    valor = b.pop(hora) 
                                                    datos.append(valor[0])
                                                    datos.append(valor[0])
                                                    datos.append(editado)
                                                    b.setdefault(hora, datos)
    
    '''funcion que borra la hora de la pelicula'''
    def set_borrarhorapelicula(self, hora, cines, nombrecine, nombresala, nombrepelicula):
        for x in cines.keys():
            if x == nombrecine:
                for y in cines[nombrecine][4]:
                    for z in y.keys():
                        if z == nombresala:
                            for t in y[nombresala][4]:
                                for a in t.keys():
                                    if a == nombrepelicula:
                                        for b in t[nombrepelicula][4]:
                                            for c in b.keys():
                                                if c == hora:
                                                    del(b[hora])
                                                    break


