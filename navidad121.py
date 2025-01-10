import xml.etree.ElementTree as ET

arbol = ET.parse("club.xml")
raiz = arbol.getroot()
for nodo in raiz.findall("socios/socio"):
    ident = nodo.get('id')
    nombre = nodo.find("nombre").text  # type: ignore
    print(f"[{ident}] {nombre}")
