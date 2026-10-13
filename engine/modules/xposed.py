import requests

class Xposed:

    def execute(self, email=None):

        self.email = email

        url = f"https://api.xposedornot.com/v1/check-email/{self.email}"

        res = requests.get(url)

        data = res.json()

        return self.formatar_saida(data)

    def formatar_saida(self, data):

        nomes = data.get("breaches", [[]])[0]

        return "\n".join(nomes)