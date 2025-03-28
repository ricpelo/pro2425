"""
Programa principal.
"""

import ZODB
import ZODB.FileStorage
from BTrees.OOBTree import BTree
import transaction
from modelo import Empleado, Departamento
import xml.etree.ElementTree as ET

# Abre la base de datos ZODB:
almacen = ZODB.FileStorage.FileStorage("basedatos.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
bd_raiz = conexion.root()

if "departamentos" not in bd_raiz:
    bd_raiz["departamentos"] = BTree()

# Abre el documento XML:
arbol = ET.parse("empresa.xml")
arbol_raiz = arbol.getroot()

for departamento in arbol_raiz.findall("departamento"):
    codigo = departamento.get('cod')
    nombre = departamento.find('nombre').text
    dep = Departamento(codigo, nombre)
    bd_raiz["departamentos"][codigo] = dep
    for empleado in departamento.findall("empleados/empleado"):
        numero = empleado.get('num')
        nombre = empleado.find('nombre').text
        cargo = empleado.find('cargo').text
        emp = Empleado(numero, nombre, cargo, dep)

transaction.commit()
conexion.close()
conexion = bd.open()
bd_raiz = conexion.root()

departamentos = bd_raiz["departamentos"]

for d in departamentos.values():
    print(d.codigo(), d.nombre())
    for e in d.empleados():
        print(e.numero(), e.nombre(), e.cargo())




conexion.close()
bd.close()
