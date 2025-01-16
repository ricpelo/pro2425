"""
Módulo de gestión de clientes.
"""

class Cliente:
    def __init__(self, dni, nombre, apellidos, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad


class ContenedorClientes:
    def __init__(self):
        self.contenedor = {}

    def meter_cliente(self, c: Cliente):
        """Mete un cliente en el contenedor."""
        self.contenedor[c.dni] = c

    def sacar_cliente(self, c: Cliente):
        """Saca un cliente del contenedor."""
        del self.contenedor[c.dni]

    def sacar_cliente_por_dni(self, dni: str):
        """Saca un cliente del contenedor a partir de su DNI."""
        del self.contenedor[dni]

    def buscar_cliente_por_dni(self, dni: str):
        """
        Busca un cliente dentro del contenedor por su DNI,
        y lo devuelve si existe.
        """
        return self.contenedor[dni]
