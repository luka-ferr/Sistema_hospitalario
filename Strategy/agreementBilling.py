from billingStrategy import BillingStrategy

class AgreementBilling(BillingStrategy):
    """
    Estrategia concreta para la facturacion de pacientes con convenio
    """

    def calculate_cost(self):
        print(f"Facturacion para pacientes con convenio institucional")
    