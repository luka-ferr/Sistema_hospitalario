from inmemoryRepository import InMemoryPatientRepository
from FactoryMethod.pacienteFactory import PacienteFactory

paciente =  PacienteFactory.createPerson("Fer", 30)
reposotory = InMemoryPatientRepository()
reposotory.save(paciente)

reposotory.patients
