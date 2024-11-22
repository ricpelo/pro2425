DIEZ = 10

from functools import reduce

digitos = lambda n: 1 if n < DIEZ else 1 + digitos(n // 10)

suma_digitos = lambda n: n if n < 10 else (n % 10) + suma_digitos(n // 10)

longitud = lambda s: 0 if s == "" else 1 + longitud(s[1:])

es_vocal = lambda s: s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or \
                     s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U'

cuantas_vocales = lambda s: 0 if s == '' else (1 if es_vocal(s[0]) else 0) + \
                                              cuantas_vocales(s[1:])

# suma = lambda t: 0 if t == () else t[0] + suma(t[1:])
suma = lambda t: reduce(lambda x, y: x + y, t, 0)

mitad = lambda t: () if t == () else (t[0] / 2,) + mitad(t[1:])

redondear = lambda t: () if t == () else (round(t[0]),) + redondear(t[1:])

# intervalo = lambda i, j: () if i > j else (i,) + intervalo(i + 1, j)
intervalo = lambda i, j: tuple(range(i, j + 1))

cuadrados = lambda t: tuple(map(lambda x: x ** 2, t))

suma_cuadrados = lambda i, j: suma(cuadrados(intervalo(i, j)))

producto = lambda x, y: x * y

from operator import mul

potencia = lambda a, b: reduce(mul, (a,) * b, 1)

max2 = lambda x, y: x if x > y else y
mayor = lambda t: reduce(max2, t)

es_primo = lambda n: all(n % x != 0 for x in range(2, n))

divisores = lambda n: tuple(x for x in range(1, n + 1) if n % x == 0)

es_primo = lambda n: len(divisores(n)) == 2

# es_primo = lambda n: not any(n % x == 0 for x in range(2, n))
