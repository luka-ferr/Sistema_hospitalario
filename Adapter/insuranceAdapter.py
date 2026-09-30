from externalAPI import ExternalInsuranceAPI


class InsuranceAdapter:

    def __init__(self, external_api: ExternalInsuranceAPI):
        self.external_api = external_api

    def check_insurance(self, patient_id):
        return self.external_api.verify_policy(patient_id)