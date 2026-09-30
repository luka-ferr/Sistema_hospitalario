from abc import ABC, abstractmethod


class PersonFactory(ABC):
    """
    Clase abstracta que define el método para crear personas.
    """
    
    @abstractmethod
    def createPerson(self):
        """
        Método que deben implementar las clases concretas
        para crear un tipo específico de persona 
        (Paciente, Medico o Administrativo).
        """
        pass