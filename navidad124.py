"""
124. Dado el documento XML del ejercicio anterior, escribir un
programa que cambie la dirección del socio cuyo id sea 1 por
«Calle Ancha, 35» y guarde los cambios en el mismo archivo.
"""

import xml.etree.ElementTree as ET

arbol = ET.parse("club.xml")
raiz = arbol.getroot()

direccion = raiz.find("socios/socio[@id='1']/direccion")
if direccion is not None:
    direccion.text = "Calle Ancha, 35"   # type: ignore

arbol.write("club2.xml", encoding="utf-8", xml_declaration=True)
