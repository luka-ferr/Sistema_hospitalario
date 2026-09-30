from FactoryMethod.pacienteFactory import PacienteFactory
from Repository.inmemoryRepository import InMemoryPatientRepository
from Observer.cita import Cita
from Observer.email import EmailObserver
from Observer.sms import SMSObserver


class HospitalFacade:

    def __init__(self):
        self.factory = PacienteFactory()
        self.repository = InMemoryPatientRepository()
        self.cita = None

    def registrar_paciente(self, nombre, edad):
        paciente = self.factory.createPerson(nombre, edad)
        self.repository.save(paciente)
        return paciente

    def obtener_pacientes(self):
        pacientes = self.repository.find_all()

        for paciente in pacientes:
            print(paciente.name, paciente.age)

    def agendar_cita(self, paciente, medico, fecha):
        self.cita = Cita(paciente, medico, fecha)

        email = EmailObserver(self.cita)
        sms = SMSObserver(self.cita)
        self.cita.register_observer(email)
        self.cita.register_observer(sms)
        return self.cita

    def confirmar_cita(self):
        self.cita.confirmar()