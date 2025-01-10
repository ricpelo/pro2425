"""
127. Dado el documento XML del ejercicio anterior, escribir un
programa que muestre el nombre de los socios por orden
cronológico según su fecha de alta, de más antiguo a más reciente.
"""

import xml.etree.ElementTree as ET

arbol = ET.parse("club.xml")
raiz = arbol.getroot()

lista = []
for nodo in raiz.findall('socio/socios'):
    nombre = nodo.find("nombre").text     # type: ignore
    alta = nodo.find("alta").text         # type: ignore
    lista.append((alta, nombre))

lista.sort()

for t in lista:
    print(t[1])
