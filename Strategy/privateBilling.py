from billingStrategy import BillingStrategy

class PrivateBilling(BillingStrategy):
    """
    Estrategia concreta para la facturacion de pacientes particulares
    """

    def calculate_cost(self):
        print(f"Facturacion para pacientes Particular")
    