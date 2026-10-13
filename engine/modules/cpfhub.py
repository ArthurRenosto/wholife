import os
import re
import requests

class CpfHub():

    def execute(self, cpf=None):

        self.cpf = re.sub(r"\D", "", cpf)

        url = f"https://api.cpfhub.io/cpf/{self.cpf}"

        res = requests.get(url, headers={"x-api-key": os.environ["CPFHUB_API_KEY"]})

        data = res.json()

        return self.formatar_saida(data)

    def formatar_saida(self, data):

        pessoa = data.get("data", {})

        genero = {"F": "Feminino", "M": "Masculino"}.get(pessoa.get("gender"), "")

        return (
            f"nome: {pessoa.get('name', '')}\n"
            f"genero: {genero}\n"
            f"nascimento: {pessoa.get('birthDate', '')}"
        )