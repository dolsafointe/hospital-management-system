class Patient:
    def __init__(self, name: str, age: int, blood_type: str, allergies: list):
        self.name = name
        self.age = age
        self.blood_type = blood_type
        self.allergies = allergies
        self.medical_records = []

    def add_medical_record(self, record: str):
        self.medical_records.append(record)