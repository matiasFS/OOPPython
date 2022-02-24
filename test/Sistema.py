from Empleado import Empleado
from Tarea import Tarea

class Sistema:
    listaEmpleado = []
    listaTarea = []

    def agregarEmpleado(self, apellido, nombre, nroLegajo, valorHora):
        empleado = Empleado(apellido,nombre,nroLegajo,valorHora)
        self.listaEmpleado.append(empleado)
        return 0
    
    def agregarTarea(self, tarea, fechaInicio, fechaFin, responsable, habil, cantHorasDiarias):
        idNuevo = 0
        tarea = Tarea(idNuevo, tarea, fechaInicio, fechaFin, responsable, habil, cantHorasDiarias)
        if(len(self.listaTarea) == 0):
            tarea.set_idTarea(1)
            self.listaTarea.append(tarea)
        else:
            idNuevo = len(self.listaTarea)+1
            tarea.set_idTarea(idNuevo)
            self.listaTarea.append(tarea)
        return 0

    def traerTarea(self, idTarea):
        for tarea in self.listaTarea:
            if(tarea.idTarea == idTarea):
                tareaTraida = tarea
        return tareaTraida
        
    def traerEmpleado(self, nroLegajo):

        for empleados in self.listaEmpleado:
            if(empleados.nroLegajo == nroLegajo):
                emple = empleados

        return emple