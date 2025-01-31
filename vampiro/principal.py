"""
El módulo principal del juego Vampiro.
"""

import mapa as m
import vocabulario as v
from jugador import Jugador

jugador = Jugador(m.vestibulo)
jugador.lugar().describir()

while True:
    entrada = input("¿Qué haces ahora?\n> ")
    verbo, nombre = v.decodificar_entrada(entrada)
    if verbo is None:
        continue
    # Si se llega hasta aquí, es que al menos tenemos un verbo.
    # Responder al jugador:
    if verbo == v.fin:
        print("Adiós")
        break
    elif verbo in [v.norte, v.sur, v.este, v.oeste]:
        jugador.intentar_mover(verbo)
