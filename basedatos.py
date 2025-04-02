"""
Base de datos.
"""

import xml.etree.ElementTree as ET

arbol = ET.parse("basedatos.xml")
raiz = arbol.getroot()

res = ''

for tabla in raiz.findall("tabla"):
    nombre_tabla = tabla.get('nombre')
    lista_cols = []
    for columna in tabla.findall("columna"):
        nombre_col = columna.find('nombre').text
        tipo_col = columna.find('tipo').text
        col = f'{nombre_col} {tipo_col}'
        if 'pk' in columna.attrib:
            col += ' PRIMARY KEY'
        if 'fk' in columna.attrib:
            ft = columna.get('ft')
            fpk = columna.get('fpk')
            col += f' REFERENCES {ft} ({fpk})'
        lista_cols.append(col)
    cols = ", ".join(lista_cols)
    res += f'CREATE TABLE {nombre_tabla} ({cols});\n'

print(res)
