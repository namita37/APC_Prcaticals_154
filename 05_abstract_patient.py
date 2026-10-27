from abc import ABC, abstractmethod
class Patient(ABC):
    @abstractmethod
    def calculate_bill(self): pass
    @abstractmethod
    def treatment(self): pass
class InPatient(Patient):
    def __init__(self, days, daily_rate): self.days, self.daily_rate = days, daily_rate
    def calculate_bill(self): return self.days * self.daily_rate
    def treatment(self): return "Hospital admission"
class OutPatient(Patient):
    def __init__(self, consultation_fee): self.fee = consultation_fee
    def calculate_bill(self): return self.fee
    def treatment(self): return "Consultation"
class EmergencyPatient(Patient):
    def __init__(self, fee): self.fee = fee
    def calculate_bill(self): return self.fee
    def treatment(self): return "Emergency care"
for p in [InPatient(3, 2000), OutPatient(500), EmergencyPatient(3500)]:
    print(p.treatment(), "| Bill:", p.calculate_bill())
