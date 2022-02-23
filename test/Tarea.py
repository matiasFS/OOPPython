class Tarea:
    idTarea = 0
    def __init__(self, tarea, fechaIncio, fechaFin, responsable, habil, cantHorasDiarias):
        self.tarea = tarea
        self.fechaInicio = fechaIncio
        self.fechaFin = fechaFin
        self.responsable = responsable
        self.habil = habil
        self.cantHorasDiarias = cantHorasDiarias

    def calcularJornal(self, habil):
        if(habil):
            jornal = self.cantHorasDiarias * self.responsable.valorHora -30
        return jornal