from abc import ABC
from abc import abstractmethod

class BillingStrategy(ABC):
    """
    Interfaz que define el contrato que deben cumplir
    las diferentes estrategias de facturación.
    """

    @abstractmethod
    def calculate_cost(self):
        pass
