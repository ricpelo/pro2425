import xml.etree.ElementTree as ET

arbol = ET.parse("club.xml")
raiz = arbol.getroot()
print(len(raiz.findall("socios/socio")))
