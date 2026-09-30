class Subject:
    """ 
    Clase que representa al Subject (sujeto) del patrón Observer.
    Se encarga de administrar los observadores registrados
    y de notificarles cuando ocurre un evento o cambio.
    """
    
    def __init__(self):
        #Inicializa la lista de observadores.
        self._observers = []
        
    def register_observer(self, observer):
        self._observers.append(observer)
        
    def remove_observer(self, observer):
        self._observers.remove(observer)
        
    def notify_observers(self, mensaje):
        for observer in self._observers:
            observer.update(mensaje)
