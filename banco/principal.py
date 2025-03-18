"""
Módulo principal.
"""

from clientes import Cliente
from productos import CuentaCorriente, TarjetaCredito, TarjetaDebito, Monedero

pepe = Cliente('123123123', 'Pepe Martínez')
c1 = CuentaCorriente(1, pepe)
c1.agregar_movimiento('Ingreso', 2000.00)
c1.agregar_movimiento('Recibo Endesa', -800.00)
c1.agregar_movimiento('Reintegro cajero', -50.00)
# c1.mostrar_operaciones()
# print(c1.total())
t1 = TarjetaCredito(1000, pepe, '2026-03-14 22:00:00', 456, 1000)
t1.comprar(800)
# print(t1.get_credito())
# print(t1.total())
td = TarjetaDebito(2000, '2026-03-18 19:00:00', 999, c1)
td.comprar(200)
td.comprar(50)
td.mostrar_operaciones()
print('-' * 30)
m = Monedero(3000, pepe, '2026-03-20 20:00:00', 888)
m.recargar(500.23846584)
m.comprar(300)
print(m.total())
m.mostrar_operaciones()
