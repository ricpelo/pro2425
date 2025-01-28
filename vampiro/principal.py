"""
El módulo principal del juego Vampiro.
"""

import mapa as m
import vocabulario as v
from jugador import Jugador

jugador = Jugador(m.vestibulo)

lugar = jugador.lugar()
lugar.describir()

while True:
    entrada = input("¿Qué haces ahora?\n> ")
    # Decodificar la entrada del jugador
    palabras = entrada.split()
    if len(palabras) == 0:
        continue
    verbo = palabras[0]
    # Bucle entre todas las palabras
    if entrada == v.fin.lexema():
        print("Adiós")
        break
    elif entrada == v.norte.lexema():
        salida = m.mapa.salida_hacia(lugar, v.norte)
        if salida is None:
            print("No hay salida en esa dirección.")
        else:
            lugar = salida
            lugar.describir()
    else:
        print("No entiendo lo que dices.")
