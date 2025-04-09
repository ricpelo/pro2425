"""
Ejercicio 2.
"""

import xml.etree.ElementTree as ET

arbol = ET.parse('biblioteca.xml')
raiz = arbol.getroot()

ia = ET.SubElement(raiz, 'categoria', {'nombre': 'Inteligencia artificial'})
libro = ET.SubElement(ia, 'libro')
ET.SubElement(libro, 'titulo').text = 'Deep Learning con Python'
ET.SubElement(libro, 'autor').text = 'Alice Johnson'
ET.SubElement(libro, 'anyo').text = '2023'

arbol.write('biblioteca.xml', encoding='utf-8')

autor = input('Introduzca el autor: ')

for libro in raiz.findall('categoria/libro'):
    if libro.find('autor').text == autor:
        print(libro.find('titulo').text)
