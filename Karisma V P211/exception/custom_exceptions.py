# custom_exceptions.py

class PatientNumberNotFoundException(Exception):
    def __init__(self, patient_id):
        self.message = f"Patient number not found Exception for Patient ID: {patient_id}"
        super().__init__(self.message)



