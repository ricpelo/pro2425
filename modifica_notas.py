import xml.etree.ElementTree as ET

arbol = ET.parse("archivo.xml")
raiz = arbol.getroot()

for alumno in raiz.findall('alumno'):
    nota = alumno.find('nota')
    nueva_nota = int(nota.text) + 1      # type: ignore
    nota.text = str(nueva_nota)          # type: ignore
    nota.set('modificado', 'si')         # type: ignore
    nombre = alumno.find('nombre/propio')
    nombre.text = nombre.text + ' María' # type: ignore

madre = raiz.find('madre')
nombre = ET.Element('nombre')
nombre.text = 'Juana González'
madre.append(nombre)                     # type: ignore

alumno = ET.SubElement(raiz, 'alumno')
alumno.set('id', '18')
dni = ET.SubElement(alumno, 'dni')
dni.text = '83828738'
nombre = ET.SubElement(alumno, 'nombre')
propio = ET.SubElement(nombre, 'propio')
propio.text = 'Antonia'
apellidos = ET.SubElement(nombre, 'apellidos')
apellidos.text = 'Roldán Roldán'
telefono = ET.SubElement(alumno, 'telefono')
telefono.text = '9569569569634345'
nota = ET.SubElement(alumno, 'nota')
nota.text = '9.5'

raiz.remove(madre)                    # type: ignore


arbol.write('salida.xml', encoding='utf-8', xml_declaration=True)
