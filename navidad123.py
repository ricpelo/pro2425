"""
123. Dado el documento XML del ejercicio anterior, escribir un
programa que cambie la dirección de todos los socios por
«Avda. de Huelva, s/n» y guarde los cambios en el mismo archivo.
"""

import xml.etree.ElementTree as ET

arbol = ET.parse("club.xml")
raiz = arbol.getroot()

for direccion in raiz.findall("socios/socio/direccion"):
    direccion.text = "Avda. de Huelva, s/n"

arbol.write("club2.xml", encoding="utf-8", xml_declaration=True)
