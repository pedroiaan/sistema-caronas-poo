import json
import os

CAMINHO_BANCO = os.path.join("banco", "banco.json")

def carregar_banco():
    if not os.path.exists(CAMINHO_BANCO):
        return {
            "usuarios": [],
            "caronas": []
        }

    try:
        with open(CAMINHO_BANCO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {
            "usuarios": [],
            "caronas": []
        }

def salvar_banco(dados):
    with open(CAMINHO_BANCO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
