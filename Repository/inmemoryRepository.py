"""Guarda los  datos en memoria"""

from .patientRepository import PatientRepository

class InMemoryPatientRepository(PatientRepository):

    def __init__(self):
        self.patients = []

    def save(self, paciente):
        self.patients.append(paciente)

    def find_by_name(self, name):
        for paciente in self.patients:
            if paciente.name == name:
                return paciente
        return None

    def find_all(self):
        return self.patients

    def update(self, paciente):
        for i, existing in enumerate(self.patients):
            if existing.id == paciente.id:
                self.patients[i] = paciente
                return

    def delete(self, name):
        self.patients = [
            paciente for paciente in self.patients
            if paciente.name != name
        ]