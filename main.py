from FactoryMethod.pacienteFactory import PacienteFactory
from FactoryMethod.medicoFactory import MedicoFactory
from FactoryMethod.adminFactory import AdminFactory
from Singleton.hospitalConfig import HospitalConfig
from Repository.inmemoryRepository import InMemoryPatientRepository
from Facade.hospitalFacade import HospitalFacade


if __name__ == "__main__":
    hospital = HospitalFacade()
    hospital.registrar_paciente("Juanita", 24)
    hospital.registrar_paciente("Juan", 28)
    hospital.registrar_paciente("Fer", 29)
    hospital.registrar_paciente("Ana", 28)

    config1 = HospitalConfig()
    config2 = HospitalConfig()

    config1.mostrarConfiguracion()
    
    config2.mostrarConfiguracion()

    print("\n¿Las instancias de HospitalConfig son la misma?", config1 is config2)

    hospital.obtener_pacientes()

    hospital.agendar_cita("Luis", "Orlando", "20-2026")
    hospital.confirmar_cita()
