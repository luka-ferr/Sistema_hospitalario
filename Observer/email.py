from .observer import Observer

class EmailObserver(Observer):

    def __init__(self, cita):
        self.cita = cita

    def update(self, mensaje):
        print(f"\nEnviando notificacion via Email al Paciente: {self.cita.paciente}: {mensaje}")
        print(f"Enviando notificacion via Email al Médico: {self.cita.medico}: {mensaje}")
