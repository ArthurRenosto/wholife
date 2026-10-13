import subprocess
import tempfile
from pathlib import Path

class Sherlock:

    def execute(self, username):

        self.username = username

        lista_sites = [
            "GitHub", "Twitter", "YouTube", "Instagram",
            "TryHackMe", "HackTheBox", "Reddit",
            "LinkedIn", "Discord", "TikTok",  "Steam", "xHamster", "Pinterest"
        ]

        with tempfile.TemporaryDirectory() as temp_dir:

            resultado_execucao = Path(temp_dir) / "sherlock_result.txt" # Definindo diretorio temporario para output do sherlock

            comando = [".venv/bin/sherlock", self.username, "--txt", "--output", str(resultado_execucao)]

            for site in lista_sites:
                comando.extend(["--site", site]) # Concatenando lista de sites ao comando

            subprocess.run(comando)

            if resultado_execucao.exists():
                conteudo = resultado_execucao.read_text(encoding="utf-8")
            else:
                conteudo = ""

        return self.formatar_saida(conteudo)

    def formatar_saida(self, conteudo):
        conteudo_formatado = conteudo.splitlines()
        return "\n".join(conteudo_formatado[:-1])


