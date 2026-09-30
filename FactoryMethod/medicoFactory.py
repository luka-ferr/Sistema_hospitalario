from FactoryMethod.personFactory import PersonFactory
from Model.medico import Medico


class MedicoFactory(PersonFactory):
    """ 
    Fábrica concreta que implementa el contrato definido por
    PersonFactory para la creación de objetos de tipo Médico. 
    """

    def createPerson(self, name, age):
        return Medico(name, age)
