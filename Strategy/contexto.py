class BillingProcessor:
    """
    Clase encargada de procesar la facturacion 
    utilizando una estrategia de calculo
    """

    def __init__(self, estrategy):
        """
        Inicializa el procesador de facturación.
        Parámetros:
        strategy: estrategia de facturación que se utilizará
        para calcular el costo.
        """
        self.strategy = estrategy


    def billing_process(self):
        """
        Procesa la facturación utilizando la estrategia seleccionada.
        Retorna un mensaje con el tipo de paciente que se esta facturando
        """
        return self.strategy.calculate_cost()
