import os
from pathlib import Path
from dotenv import set_key

ENV_FILE = Path(__file__).parent / ".env"

CHAVES = {
    "cpfhub": "CPFHUB_API_KEY",
}

def salvar_chave(servico, valor):
    nome = CHAVES.get(servico)
    if nome is None:
        raise ValueError("serviço desconhecido")

    set_key(str(ENV_FILE), nome, valor)
    os.environ[nome] = valor