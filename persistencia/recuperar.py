import ZODB
import ZODB.FileStorage
import persistent
import transaction
from basedatos import Empleado, Departamento

almacen = ZODB.FileStorage.FileStorage("departamento.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

d1 = raiz["departamentos"][1]
d2 = raiz["departamentos"][2]

print(d1)
print(d2)
print(list(d1.get_empleados()))
print(list(d2.get_empleados()))

# d2.agregar_empleado(Empleado('444', 'José Ruiz', 80000.00))
# transaction.commit()

conexion.close()
bd.close()
