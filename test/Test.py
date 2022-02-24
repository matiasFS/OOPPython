from Empleado import Empleado
from Tarea import Tarea
from Sistema import Sistema

sis = Sistema()
sis.agregarEmpleado("Juarez", "Jose", 1091290, 10)
sis.agregarEmpleado("Perez", "Sergio", 292929, 10)
sis.agregarEmpleado("Sanchez", "Juan", 123123, 10)
sis.agregarEmpleado("Juarez", "Jose", 1091290, 10)
sis.agregarEmpleado("Lopez", "Pedro", 232322, 10)

empleado = sis.traerEmpleado(123123)
empleado2 = sis.traerEmpleado(292929)
empleado3 = sis.traerEmpleado(1091290)


sis.agregarTarea("Limpiar", "20/12", "27/12", empleado, True, 10)
sis.agregarTarea("Soldar", "20/12", "27/12", empleado2, False, 9)
sis.agregarTarea("Agujerear", "20/12", "27/12", empleado3, True, 5)

for empleados in sis.listaEmpleado:
    print(empleados.apellido, empleados.nombre, empleados.nroLegajo)

for tareas in sis.listaTarea:
    print(tareas.idTarea, tareas.tarea, tareas.responsable.nroLegajo)

print(sis.traerTarea(2).tarea)