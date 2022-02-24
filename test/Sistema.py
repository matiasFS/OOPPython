from asyncio.windows_events import NULL
from Empleado import Empleado
from Tarea import Tarea

class Sistema:
    listaEmpleado = []
    listaTarea = []

    def traerEmpleado(self, nroLegajo):
        encontre = True
        i = 0
        emple = NULL
        while i < len(self.listaEmpleado) and encontre:
            if(self.listaEmpleado[i].nroLegajo == nroLegajo):
                emple = self.listaEmpleado[i]
                encontre = False
            i = i + 1
        return emple

    def agregarEmpleado(self, apellido, nombre, nroLegajo, valorHora): 
        empleadoExiste = self.traerEmpleado(nroLegajo)
        if(empleadoExiste):
            print("Error ya existe el empleado")
        else:
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
        encontre = True
        i = 0
        tarea = NULL
        while i < len(self.listaEmpleado) and encontre:
            if(self.listaTarea[i].idTarea == idTarea):
                tarea = self.listaTarea[i]
                encontre = False
            i = i + 1
        return tarea
        
   