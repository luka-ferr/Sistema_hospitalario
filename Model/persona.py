from abc import ABC, abstractmethod

#Fabrica de personas

class Persona(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def mostrarRol(self):
        pass

    @abstractmethod
    def mostrarDatosPersonales(self):
        pass
