class Patient:
    def __init__(self, patient_id, first_name, last_name, date_of_birth, gender, contact_number, address):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_number = contact_number
        self.address = address

    def __str__(self):
        return (f"Patient[ID={self.patient_id}, First Name={self.first_name}, Last Name={self.last_name}, "
                f"Date of Birth={self.date_of_birth}, Gender={self.gender}, "
                f"Contact Number={self.contact_number}, Address={self.address}]")