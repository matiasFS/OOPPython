from Empleado import Empleado


class Sistema:
    listaEmpleado = []
    listaTarea = []

    def agregarEmpleado(self, apellido, nombre, nroLegajo, valorHora):
        empleado = Empleado(apellido,nombre,nroLegajo,valorHora)
        self.listaEmpleado.append(empleado)
        return 0
    
    def traerEmpleado(self, nroLegajo):

        for empleados in self.listaEmpleado:
            if(empleados.nroLegajo == nroLegajo):
                emple = empleados

        return emple