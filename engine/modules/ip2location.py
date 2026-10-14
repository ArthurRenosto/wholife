import requests
import os

class ip2Location:

    def execute(self, ip=None):

        self.ip = ip

        url = " https://api.ip2location.io/?chave=", os.environ["IP2LOCATION_API_KEY"], f"&ip={self.ip}"

        res = requests.get(url)

        data = res.json()

        return self.formatar_saida(data)

    def formatar_saida(self, data):
