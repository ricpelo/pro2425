"""
Programa principal.
"""

import xml.etree.ElementTree as ET
import tkinter as tk
import ZODB
import ZODB.FileStorage
from BTrees.OOBTree import BTree
import transaction
from modelo import Empleado, Departamento

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add("*Font", ("Arial", 18))
        self.title("Empresa")
        # self.geometry("600x300")
        self.titulo = tk.Label(text="Departamentos y empleados")
        self.titulo.pack()
        self.listado = tk.Listbox(self, width=40)
        self.listado.pack(fill="both")
        self.boton = tk.Button(self, text="Cerrar", command=self.quit)
        self.boton.pack()

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


app = Aplicacion()
conexion = bd.open()
bd_raiz = conexion.root()
departamentos = bd_raiz["departamentos"]

for d in departamentos.values():
    app.listado.insert(tk.END, f'{d.codigo()} {d.nombre()}:')
    # print(d.codigo(), d.nombre())
    for e in d.empleados():
        app.listado.insert(tk.END, f'- {e.numero()} {e.nombre()} {e.cargo()}')
        # print(e.numero(), e.nombre(), e.cargo())

conexion.close()
bd.close()
app.mainloop()
