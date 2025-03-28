"""
El modelo del sistema.
"""

from BTrees.OOBTree import BTree
import persistent

class Empleado(persistent.Persistent):
    """Un empleado de la empresa."""

    def __init__(self, numero: int, nombre: str, cargo: str, departamento: 'Departamento'):
        self.__numero = numero
        self.set_nombre(nombre)
        self.set_cargo(cargo)
        if departamento is None:
            raise ValueError("El empleado tiene que pertenecer a un departamento.")
        self.__departamento = departamento
        departamento.asignar_empleado(self)

    def numero(self) -> int:
        """Devuelve el número del empleado"""
        return self.__numero

    def nombre(self) -> str:
        """Devuelve el nombre del empleado."""
        return self.__nombre

    def cargo(self) -> str:
        """Devuelve el cargo del empleado."""
        return self.__cargo

    def departamento(self) -> 'Departamento':
        """Devuelve el departamento al que pertenece el empleado."""
        return self.__departamento

    def set_nombre(self, nombre: str) -> None:
        """Asigna el nombre del empleado."""
        self.__nombre = nombre

    def set_cargo(self, cargo: str) -> None:
        """Asigna el cargo del empleado."""
        self.__cargo = cargo


class Departamento(persistent.Persistent):
    """Un departamento de la empresa."""

    def __init__(self, codigo: int, nombre: str):
        self.__codigo = codigo
        self.set_nombre(nombre)
        self.__empleados = BTree()

    def codigo(self) -> int:
        """Devuelve el código del departamento."""
        return self.__codigo

    def nombre(self) -> str:
        """Devuelve el nombre del departamento."""
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        """Asigna el nombre del departamento."""
        self.__nombre = nombre

    def asignar_empleado(self, empleado: Empleado) -> None:
        """Asigna un empleado al departamento."""
        self.__empleados[empleado.numero()] = empleado

    def empleados(self):
        return self.__empleados.values()
