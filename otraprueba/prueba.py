
class Pila:
    """Una pila."""

    def __init__(self):
        self.__elementos = ()

    def elementos(self):
        """Devuelve los elementos de la pila."""
        return self.__elementos

p = Pila()
elem = p.elementos()
print(elem)

for e in p.elementos():
    print(e)
