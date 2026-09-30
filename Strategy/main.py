from contexto import BillingProcessor
from billingStrategy import BillingStrategy
from iInsuranceBilling import InsuranceBilling
from privateBilling import PrivateBilling
from agreementBilling import AgreementBilling

def main():
    
    processor = BillingProcessor(InsuranceBilling())
    processor.billing_process()

    processor2 = BillingProcessor(PrivateBilling())
    processor2.billing_process()

    processor3 = BillingProcessor(AgreementBilling())
    processor3.billing_process()

    
if __name__ == "__main__":
    main()