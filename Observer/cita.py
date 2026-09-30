from .subject import Subject


class Cita(Subject):

    def __init__(self, paciente, medico, fecha):
        super().__init__()
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha

    def confirmar(self):
        mensaje = f"Cita confirmada para el día {self.fecha}"
        print("Cita confirmada")
        self.notify_observers(mensaje)