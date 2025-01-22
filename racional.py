"""
Números racionales.
"""

from math import gcd

class Racional:
    """
    Implementa números racionales.

    Invariantes:
      - El denominador no puede ser cero.
      - El racional está siempre totalmente simplificado.
    """
    def __init__(self, num, den):
        self.__set_numerador(num)
        self.__set_denominador(den)
        assert num == self.numerador()
        assert den == self.denominador()
        self.__simplificar()
        assert num * self.denominador() == den * self.numerador()

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.numerador() == otro.numerador() and \
               self.denominador() == otro.denominador()

    def __str__(self):
        num = self.numerador()
        den = self.denominador()
        return f"{num}/{den}"

    def numerador(self):
        """Devuelve el numerador del racional."""
        return self.__numer

    def denominador(self):
        """Devuelve el denominador del racional."""
        return self.__denom

    def __set_numerador(self, num):
        self.__numer = num
        assert self.numerador() == num

    def __set_denominador(self, den):
        if den == 0:                      # Precondición
            raise ValueError("El denominador no puede ser cero.")
        self.__denom = den
        assert self.denominador() == den  # Postcondición

    def mult(self, otro):
        """Multiplica dos racionales y devuelve el racional resultante."""
        n = self.numerador() * otro.numerador()
        d = self.denominador() * otro.denominador()
        return Racional(n, d)

    def __simplificar(self):
        """Simplifica el racional."""
        mcd = gcd(self.numerador(), self.denominador())
        num_antes = self.numerador()
        den_antes = self.denominador()
        self.__set_numerador(self.numerador() // mcd)
        self.__set_denominador(self.denominador() // mcd)
        num_despues = self.numerador()
        den_despues = self.denominador()
        assert num_antes * den_despues == num_despues * den_antes
