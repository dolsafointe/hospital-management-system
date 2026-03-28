class DoctorProfile:
    def __init__(self, name, specialization, hospital):
        self.name = name
        self.specialization = specialization
        self.hospital = hospital

    def __str__(self):
        return f'Dr. {self.name}, Specialization: {self.specialization}, Hospital: {self.hospital}'