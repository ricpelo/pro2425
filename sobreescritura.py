class Trabajador:
    def __init__(self, nombre: str):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return f'Mi nombre es {self.get_nombre()}'


class Docente(Trabajador):
    def __init__(self, nombre: str, especialidad: str):
        super().__init__(nombre)
        self.__especialidad = especialidad

    def get_especialidad(self):
        return self.__especialidad

    def __str__(self):
        return super().__str__() + f' y mi especialidad es {self.get_especialidad()}'


t = Trabajador('Manolo')
d = Docente('Pepe', 'Informática')
print(d.get_nombre())
print(d.get_especialidad())
print(d)
