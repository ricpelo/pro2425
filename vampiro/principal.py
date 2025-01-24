"""
El módulo principal del juego Vampiro.
"""

from mapa import Lugar
from jugador import Jugador

vestibulo = Lugar("VESTÍBULO", "Estás en el vestíbulo del castillo. Bla bla bla...")
pasillo = Lugar("PASILLO", "Te encuentras en medio del pasillo principal de este piso.")
jugador = Jugador(vestibulo)

print(vestibulo.nombre())
print(vestibulo.descripcion())
entrada = input("¿Qué haces ahora?\n> ")
