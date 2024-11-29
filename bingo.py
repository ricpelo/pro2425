"""
El bingo.
"""

from random import randrange

bombo = list(range(100))

while len(bombo) > 0:
    i = randrange(len(bombo))
    n = bombo.pop(i)
    print(n, end=' ')
