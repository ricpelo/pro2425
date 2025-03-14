"""
Módulo principal.
"""

from clientes import Cliente
from productos import CuentaCorriente, TarjetaCredito

pepe = Cliente('123123123', 'Pepe Martínez')
c1 = CuentaCorriente(1, pepe)
c1.agregar_movimiento('Ingreso', 2000.00)
c1.agregar_movimiento('Recibo Endesa', -800.00)
c1.agregar_movimiento('Reintegro cajero', -50.00)
c1.mostrar_operaciones()
print(c1.total())
t1 = TarjetaCredito(1000, pepe, '2026-03-14 22:00:00', 456, 1000)
t1.comprar(800)
print(t1.get_credito())
print(t1.total())
