# Importa la clase Singleton, que controla la creación 
# de una única instancia de la configuración.

from Singleton.singleton import Singleton

class HospitalConfig (Singleton):
    """
    Clase que representa la configuración general del hospital.
    """

    def __init__(self):
        self.nombre = "Hospital el Moridero"
        self.horario = "24/7"
        self.politicas = "Solo se atienden moribundos"

    def mostrarConfiguracion(self):
        print("\nNombre:", self.nombre)
        print("Horarios de atención:", self.horario)
        print("Politicas Internas:", self.politicas)

