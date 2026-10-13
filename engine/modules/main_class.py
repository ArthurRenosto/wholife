from .sherlock import Sherlock
from .xposed import Xposed
from .cpfhub import CpfHub

class Main:
    def __init__ (self, username=None, email=None, cpf=None):
        self.username = username
        self.email = email
        self.cpf = cpf

    def execute(self):
        
        resultados = {}

        if self.username:
            resultados["sherlock"] = self.sherlock()

        if self.email:
            resultados["xposed"] = self.xposed()

        if self.cpf:
            resultados["cpfhub"] = self.cpfhub()


        return resultados

    def sherlock(self):
        sherlock = Sherlock()
        return sherlock.execute(self.username)

    def xposed(self):
        xposed = Xposed()
        return xposed.execute(self.email)

    def cpfhub(self):
        cpfhub = CpfHub()
        return cpfhub.execute(self.cpf)