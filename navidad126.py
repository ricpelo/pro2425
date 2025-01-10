"""
126. Dado el documento XML del ejercicio anterior, escribir un
programa que añada el teléfono del socio cuyo id sea 1 creándole
al socio un nodo hijo que sea <telefono>666555444</telefono> y
guarde los cambios en el mismo archivo.
"""

import xml.etree.ElementTree as ET

arbol = ET.parse("club.xml")
raiz = arbol.getroot()

socio = raiz.find("socios/socio[@id='1']")
if socio is not None:
    telefono = ET.SubElement(socio, 'telefono')   # type: ignore
    telefono.text = "666555444"

arbol.write("club2.xml", encoding="utf-8", xml_declaration=True)
