import subprocess
import tempfile
from pathlib import Path

class Sherlock:

    def execute(self, username):

        self.username = username

        lista_sites = [
            "GitHub", "Twitter", "YouTube", "Instagram",
            "TryHackMe", "HackTheBox", "Reddit",
            "LinkedIn", "Discord"
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

        return self.formatar_saida(conteudo) # Devolvendo resultado formatado

    def formatar_saida(self, conteudo):
        return conteudo


