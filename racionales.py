"""
Módulo de representación y manipulación de números racionales.
"""

import math

def racional(num: int, den: int):
    """
    Construye un racional a partir del numerador y el
    denominador.
    """
    return {'num': num, 'den': den}


def numerador(r):
    """Devuelve el numerador de un racional."""
    return r['num']


def denominador(r):
    """Devuelve el denominador de un racional."""
    return r['den']


def mult_rac(r1, r2):
    """Multiplica dos racionales."""
    n1 = numerador(r1)
    d1 = denominador(r1)
    n2 = numerador(r2)
    d2 = denominador(r2)
    return _simplificar(racional(n1 * n2, d1 * d2))


def suma_rac(r1, r2):
    """Suma dos racionales."""
    n1 = numerador(r1)
    d1 = denominador(r1)
    n2 = numerador(r2)
    d2 = denominador(r2)
    return _simplificar(racional(n1 * d2 + n2 * d1, d1 * d2))


def _simplificar(r):
    """Simplifica un racional."""
    num = numerador(r)
    den = denominador(r)
    mcd = math.gcd(num, den)
    return racional(num // mcd, den // mcd)
