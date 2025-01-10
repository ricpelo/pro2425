"""
125. Dado el documento XML del ejercicio anterior, escribir un
programa que elimine al socio cuyo id sea 51 y guarde los
cambios en el mismo archivo.
"""

import xml.etree.ElementTree as ET

arbol = ET.parse("club.xml")
raiz = arbol.getroot()

socios = raiz.find("socios")
socio = socios.find("socio[@id='51']")    # type: ignore
if socio is not None:
    socios.remove(socio)                  # type: ignore

arbol.write("club2.xml", encoding="utf-8", xml_declaration=True)
