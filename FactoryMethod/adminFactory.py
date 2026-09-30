from FactoryMethod.personFactory import PersonFactory
from Model.administrativo import Administrativo


class AdminFactory(PersonFactory):
    """ 
    Fábrica concreta que implementa el contrato definido por
    PersonFactory para la creación de objetos de tipo Administrativo. 
    """

    def createPerson(self, name, age):
        return Administrativo(name, age)
