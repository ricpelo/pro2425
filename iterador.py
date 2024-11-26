"""
Ejemplo de iterador
"""

for elem in filter(lambda x: x % 3 == 0, range(10)):
    print(elem)
    
for elem in range(10):
    if elem % 3 == 0:
        print(elem)
    
