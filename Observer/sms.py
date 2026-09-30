from .observer import Observer

class SMSObserver(Observer):

    def __init__(self, cita):
            self.cita = cita

    def update(self, mensaje):
        print(f"\nEnviando notificacion via SMS al Paciente: {self.cita.paciente}: {mensaje}")
        print(f"Enviando notificacion via SMS al Médico: {self.cita.medico}: {mensaje}")
