from Model.persona import Persona

class Administrativo (Persona):

    def __init__(self, name, age):
        super().__init__(name, age)

    def mostrarRol(self):
        print("\nAdministrativo")

    def mostrarDatosPersonales(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")