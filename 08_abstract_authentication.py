from abc import ABC, abstractmethod
class Authentication(ABC):
    @abstractmethod
    def authenticate(self, credential): pass
class PasswordAuthentication(Authentication):
    def __init__(self, password): self.password = password
    def authenticate(self, credential): return credential == self.password
class OTPAuthentication(Authentication):
    def __init__(self, otp): self.otp = str(otp)
    def authenticate(self, credential): return str(credential) == self.otp
class BiometricAuthentication(Authentication):
    def authenticate(self, credential): return credential == "verified"
for auth, value in [(PasswordAuthentication("python123"), "python123"),
                    (OTPAuthentication(123456), "123456"),
                    (BiometricAuthentication(), "verified")]:
    print(type(auth).__name__, auth.authenticate(value))
