"""
Módulo principal de la tienda online.
"""

from cliente import Cliente, ContenedorClientes

clientes = ContenedorClientes()

clientes.meter_cliente(Cliente("48484848A", "Pepe", "Gómez Gil", 43))
clientes.meter_cliente(Cliente("99887766J", "María", "Morales Mora", 27))

pepe = clientes.buscar_cliente_por_dni("48484848A")
print(pepe.edad)
