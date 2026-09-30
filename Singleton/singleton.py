#primero

class Singleton():
    """
    Clase base que implementa el patrón de diseño Singleton.
    """
    
    # Diccionario utilizado para almacenar las instancias creadas.
    _instance = {}
    
    def __new__(cls, *args,  **kwargs):
        """
        Controla la creación de nuevas instancias. 
        Antes de crear un objeto, verifica si ya existe una instancia 
        de la clase. Si no existe, crea una nueva y la almacena.
        Si ya existe, retorna la instancia que había sido creada.
        """

        # Verifica si la clase actual todavía no tiene una instancia.
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
            
        # Retorna la instancia existente o la recién creada.
        return cls._instance[cls]
