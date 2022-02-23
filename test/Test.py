from Empleado import Empleado
from Tarea import Tarea
from Sistema import Sistema

sis = Sistema()
sis.agregarEmpleado("Peres", "Juan", 292929, 10)
sis.agregarEmpleado("Peres", "Juan", 123123, 10)
sis.agregarEmpleado("Peres", "jorrrrge", 232322, 10)
sis.agregarEmpleado("Peres", "Juan", 1091290, 10)

print(sis.listaEmpleado[0].nroLegajo)
print(sis.traerEmpleado(232322).nombre)