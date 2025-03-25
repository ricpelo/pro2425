"""
Ejemplo de uso del módulo pickle
"""

import pickle

class Empleado:
    """Un empleado de la empresa."""

    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.salario = salario

    def __repr__(self):
        return f'Empleado({self.nombre!r}, {self.salario!r})'

class Departamento:
    """Un departamento de la empresa."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        """Agrega un empleado al departamento."""
        self.empleados.append(empleado)

    def get_empleados(self):
        return self.empleados

    def __repr__(self):
        return f'Departamento({self.nombre!r})'

def guardar_datos(archivo, objeto):
    """Guarda el objeto en un archivo."""
    with open(archivo, "wb") as f:
        pickle.dump(objeto, f)

def cargar_datos(archivo):
    with open(archivo, "rb") as f:
        return pickle.load(f)

e1 = Empleado('Juan Pérez', 30000.00)
e2 = Empleado('María López', 35000.00)

d1 = Departamento('Informática')
d1.agregar_empleado(e1)
d1.agregar_empleado(e2)

e3 = Empleado('José Martínez', 15000.00)

d2 = Departamento('Inglés')
d2.agregar_empleado(e3)

deps = [d1, d2]
guardar_datos('departamento.pickle', deps)

deps_cargados = cargar_datos('departamento.pickle')
for dep in deps_cargados:
    print(dep.nombre, dep.get_empleados())
print(id(e3))
print(id(deps_cargados[1].get_empleados()[0]))
print(e3.nombre)
print(deps_cargados[1].get_empleados()[0].nombre)
