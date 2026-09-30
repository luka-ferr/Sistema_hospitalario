from FactoryMethod.personFactory import PersonFactory
from Model.paciente import Paciente


class PacienteFactory(PersonFactory):
    """ 
    Fábrica concreta que implementa el contrato definido por
    PersonFactory para la creación de objetos de tipo Paciente. 
    """

    def createPerson(self, name, age):
        return Paciente(name, age)
