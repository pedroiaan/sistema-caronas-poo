from .carona import Carona
from .usuario import Usuario
from banco.banc import carregar_banco, salvar_banco

class SistemaCaronas:
    def __init__(self):
        banco = carregar_banco()
        self.usuarios = banco["usuarios"]
        self.caronas = [Carona.from_dict(c) for c in banco["caronas"]]
    
    def cadastrar_usuario(self, nome, email, senha):
        if any(usuario["_email"] == email for usuario in self.usuarios):
            return False
        novo_usuario = {
            "_nome": nome,
            "_email": email,
            "_senha_hash": Usuario(nome, email, senha).hash_senhas(senha)
        }
        self.usuarios.append(novo_usuario)
        salvar_banco({"usuarios": self.usuarios, "caronas": [c.to_dict() for c in self.caronas]})
        return True
    
    def login_usuario(self, email, senha):
        for usuario_dict in self.usuarios:
            if usuario_dict["_email"] == email:
                senha_hash = Usuario("", "", "").hash_senhas(senha)
                if senha_hash == usuario_dict["_senha_hash"]:
                    return True
        return False


    def criar_carona(self, origem, data, horario):
        nova_carona = {"origem": origem,
            "data": data,
            "horario": horario }
        self.caronas.append(nova_carona)
        salvar_banco({"usuarios": self.usuarios, "caronas": self.caronas})
        return True

    def listar_caronas(self):
        return self.caronas
        
    def buscar_carona_origem(self, origem):
        caronas_encontradas = [carona for carona in self.caronas if carona.origem.lower() == origem.lower()]
        return caronas_encontradas
    
    def reservar_vagas(self, origem, data, horario, email):
        for carona in self.caronas:
            if carona.origem == origem and carona.data == data and carona.horario == horario:
                return carona.reservar_vagas(email)
        return False

    def cancelar_vaga(self, origem, data, horario, email):
        for carona in self.caronas:
            if carona.origem == origem and carona.data == data and carona.horario == horario:
                return carona.cancelar_vaga(email)
        return False