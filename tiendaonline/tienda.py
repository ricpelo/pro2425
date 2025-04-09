"""
Tienda online.
"""

import ZODB
import ZODB.FileStorage
import transaction
from persistent import Persistent
from typing import Iterator
from BTrees.OOBTree import BTree # type: ignore

class Articulo(Persistent):
    """Un artículo de la tienda online."""

    def __init__(self, codigo: int, denominacion: str, precio: float):
        self.__codigo = codigo
        self.set_denominacion(denominacion)
        self.set_precio(precio)

    def codigo(self) -> int:
        """El código."""
        return self.__codigo

    def denominacion(self) -> str:
        """La denominación."""
        return self.__denominacion

    def set_denominacion(self, denominacion: str) -> None:
        """Asigna la denominación."""
        self.__denominacion = denominacion

    def precio(self) -> float:
        """El precio."""
        return self.__precio

    def set_precio(self, precio: float) -> None:
        """Asigna el precio."""
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = precio


class Detalle(Persistent):
    """Una línea de detalle del carrito."""

    def __init__(self, articulo: Articulo, cantidad: int = 1):
        self.__articulo = articulo
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.__cantidad = cantidad

    def articulo(self) -> Articulo:
        """El artículo que está en la línea de detalle."""
        return self.__articulo

    def cantidad(self) -> int:
        """La cantidad de ese artículo en la línea de detalle."""
        return self.__cantidad

    def incrementar_cantidad(self, incremento: int = 1) -> None:
        """Incrementa la cantidad del artículo en un incremento."""
        self.__cantidad += incremento

    def decrementar_cantidad(self, decremento: int = 1) -> None:
        """Decrementa la cantidad del artículo en un decremento."""
        if self.__cantidad - decremento <= 0:
            raise ValueError("La cantidad debe ser siempre mayor que cero.")
        self.__cantidad -= decremento


class Carrito(Persistent):
    """Un carrito de la tienda online."""

    def __init__(self):
        self.__detalles = BTree()

    def agregar_detalle(self, articulo: Articulo, cantidad: int):
        """Agrega una línea de detalle al carrito."""
        if articulo.codigo() in self.__detalles:
            detalle = self.__detalles[articulo.codigo()]
            detalle.incrementar_cantidad(cantidad)
        else:
            self.__detalles[articulo.codigo()] = Detalle(articulo, cantidad)

    def detalles(self) -> Iterator[Detalle]:
        """Devuelve un iterador que recorre todas las líneas de detalle del carrito."""
        return self.__detalles.values()


class Usuario(Persistent):
    """Un usuario de la tienda."""

    def __init__(self, dni: str, nombre: str):
        self.__dni = dni
        self.set_nombre(nombre)
        # self.__carrito = Carrito()

    def dni(self) -> str:
        """El DNI del usuario."""
        return self.__dni

    def nombre(self) -> str:
        """El nombre del usuario."""
        return self.__nombre

    # def carrito(self) -> Carrito:
    #     """El carrito del usuario."""
    #     return self.__carrito

    def set_nombre(self, nombre: str) -> None:
        """Asigna nombre del usuario."""
        self.__nombre = nombre

    def __repr__(self):
        return f'{self.__dni} {self.__nombre}'



almacen = ZODB.FileStorage.FileStorage("tiendaonline.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

raiz['usuarios'] = BTree()
pepe = Usuario('123', 'Pepe')
raiz['usuarios'][pepe.dni()] = pepe

# t = Articulo(1, 'Tornillo', 4.00)
# boina = Articulo(2, 'Boina', 30.00)
# c = pepe.carrito()
# c.agregar_detalle(t, 5)
# c.agregar_detalle(boina, 10)
# c.agregar_detalle(boina, 20)

transaction.commit()
conexion.close()
bd.close()

# suma = 0
# for d in c.detalles():
#     cod = d.articulo().codigo()
#     den = d.articulo().denominacion()
#     can = d.cantidad()
#     pre = d.articulo().precio()
#     imp = can * pre
#     suma += imp
#     print(f'{cod} {den} {can} {pre} € = {imp} €')
# print('-' * 30)
# print(f'TOTAL: {suma} €')
