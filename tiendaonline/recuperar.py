import ZODB
import ZODB.FileStorage
import transaction
from persistent import Persistent
from typing import Iterator
from BTrees.OOBTree import BTree # type: ignore

almacen = ZODB.FileStorage.FileStorage("tiendaonline.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

pepe = raiz['usuarios']['123']
print(pepe.dni())
