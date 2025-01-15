"""
Números racionales.
"""

class Racional:
    def __init__(self, num, den):
        self.numer = num
        self.denom = den

    def numerador(self):
        return self.numer

    def denominador(self):
        return self.denom

    def mult(self, otro):
        n = self.numerador() * otro.numerador()
        d = self.denominador() * otro.denominador()
        return Racional(n, d)
