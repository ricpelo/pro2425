"""
6. Escribir un programa que muestre por pantalla la tabla de multiplicar de
un número comprendido entre 0 y 10, introducido por teclado.
"""

"""
while True:
    num = int(input("Introduzca el número de la tabla deseada (entre 0 y 10): "))
    if num in range(0, 11):
        break
    print("El número no está entre los límites solicitados.")

i = 0
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

for i in range(0, 11):
    print(num, "x", i, "=", num * i)
"""

lista = ['a', 'b', 'c']

for i, _ in enumerate(lista):
    lista[i] *= 2

print(lista)
