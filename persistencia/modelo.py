"""
Modelo de datos.
"""

from BTrees.OOBTree import BTree # type: ignore

import persistent

class Empleado(persistent.Persistent):
    """Un empleado de la empresa."""

    def __init__(self, dni: str, nombre: str, salario: float):
        self.dni = dni
        self.nombre = nombre
        self.salario = salario

    def __repr__(self):
        return f'Empleado({self.dni!r}, {self.nombre!r}, {self.salario!r})'

class Departamento(persistent.Persistent):
    """Un departamento de la empresa."""

    def __init__(self, numero: int, nombre: str):
        self.numero = numero
        self.nombre = nombre
        self.empleados = BTree()

    def agregar_empleado(self, empleado):
        """Agrega un empleado al departamento."""
        self.empleados[empleado.dni] = empleado

    def get_empleados(self):
        return self.empleados.values()

    def __repr__(self):
        return f'Departamento({self.numero!r}, {self.nombre!r})'
