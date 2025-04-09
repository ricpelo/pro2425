"""
Ejercicio 1.
"""

from abc import ABC, abstractmethod
import ZODB
import ZODB.FileStorage
import transaction
from persistent import Persistent
from BTrees.OOBTree import BTree # type: ignore

class Vehiculo(ABC):
    """Un vehículo."""

    def __init__(self, marca: str, modelo: str, anyo: int, matricula: str):
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_anyo(anyo)
        self.set_matricula(matricula)

    def marca(self) -> str:
        """Una marca."""
        return self.__marca

    def modelo(self) -> str:
        """Una modelo."""
        return self.__modelo

    def anyo(self) -> int:
        """Una año."""
        return self.__anyo

    def matricula(self) -> str:
        """Una matrícula."""
        return self.__matricula

    def set_marca(self, marca):
        """Asigna la marca."""
        self.__marca = marca

    def set_modelo(self, modelo):
        """Asigna el modelo."""
        self.__modelo = modelo

    def set_anyo(self, anyo):
        """Asigna el año."""
        self.__anyo = anyo

    def set_matricula(self, matricula):
        """Asigna la matrícula."""
        self.__matricula = matricula

    @abstractmethod
    def calcular_precio_alquiler(self):
        """Calcula el precio del alquiler."""
        ...


class Coche(Vehiculo, Persistent):
    """Un coche."""

    def __init__(self, marca, modelo, anyo, matricula, color: str):
        super().__init__(marca, modelo, anyo, matricula)
        self.set_color(color)

    def color(self) -> str:
        """Devuelve el color."""
        return self.__color

    def set_color(self, color):
        """Asigna el color."""
        self.__color = color

    def calcular_precio_alquiler(self):
        return 200 if self.marca() == 'BMW' else 150


class Moto(Vehiculo, Persistent):
    """Un coche."""

    def __init__(self, marca, modelo, anyo, matricula, cilindrada: int):
        super().__init__(marca, modelo, anyo, matricula)
        self.set_cilindrada(cilindrada)

    def cilindrada(self) -> int:
        """Devuelve la cilindrada."""
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        """Asigna el cilindrada."""
        self.__cilindrada = cilindrada

    def calcular_precio_alquiler(self):
        return 400 if self.cilindrada() >= 250 else 300


class Flota:
    """Una flota de vehículos."""

    ultima_flota_creada = 0

    def __init__(self):
        self.__vehiculos = BTree()
        Flota.ultima_flota_creada += 1
        self.__numero = Flota.ultima_flota_creada

    def numero(self) -> int:
        """Devuelve el número de la flota."""
        return self.__numero

    def agregar(self, vehiculo: Vehiculo) -> None:
        """Agrega un vehículo a la flota."""
        self.__vehiculos[vehiculo.matricula()] = vehiculo

    def buscar(self, matricula: str) -> Vehiculo | None:
        """Busca un vehículo por su matrícula."""
        return self.__vehiculos.get(matricula)

    # def vehiculos(self):
    #     """Devuelve un iterador con los vehículos de la flota."""
    #     return self.__vehiculos.values()


c1 = Coche('Audi', 'A5', 2022, '4455JJJ', 'Blanco')
c2 = Coche('BMW', 'Serie 2', 2024, '9999KKK', 'Gris')
m1 = Moto('Vespino', 'GL', 1970, 'C123123', 500)
f = Flota()
f.agregar(c1)
f.agregar(c2)
f.agregar(m1)

# Abre la base de datos ZODB:
almacen = ZODB.FileStorage.FileStorage("vehiculos.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
bd_raiz = conexion.root()

bd_raiz['flotas'] = BTree()
bd_raiz['flotas'][f.numero()] = f

transaction.commit()
conexion.close()
bd.close()

"""
# Comprobación:
almacen = ZODB.FileStorage.FileStorage("vehiculos.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
bd_raiz = conexion.root()

for flota in bd_raiz['flotas'].values():
    for vehiculo in flota.vehiculos():
        print(f'{vehiculo.marca()} {vehiculo.modelo()} {vehiculo.matricula()}')
"""
