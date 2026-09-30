from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Clase abstracta que representa el Observer del patrón Observer.
    Define el método que deben implementar todos los observadores concretos
    que quieran recibir notificaciones del Subject.
    """

    @abstractmethod
    def update(self, mensaje):
        pass