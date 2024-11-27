
empleados = [
    ('María', 'González', 1800.23),
    ('Javier', 'Ruiz', 1630.50),
    ('Jesús', 'Pérez', 2100.42),
    ('Rosa', 'Muñoz', 2240.78)
]

suma = 0
for i, emple in enumerate(empleados):
    nombre, apellidos, salario = emple
    salario = round(salario * 1.10, 2)
    empleados[i] = (nombre, apellidos, salario)
    print("Empleado", nombre, apellidos, "con salario", salario)
    suma += salario
print("El salario total es", suma)
print(empleados)
