
from .carona import Carona
from .usuario import Usuario 
from banco.banc import carregar_banco, salvar_banco

class SistemaCaronas:
    def __init__(self):
        banco = carregar_banco()
        self.usuarios = [Usuario.from_dict(u_data) for u_data in banco.get("usuarios", [])]
        self.caronas = [Carona.from_dict(c_data) for c_data in banco.get("caronas", [])]
    
    def _salvar_dados(self):
        dados_para_salvar = {
            "usuarios": [u.to_dict() for u in self.usuarios], 
            "caronas": [c.to_dict() for c in self.caronas]   
        }
        salvar_banco(dados_para_salvar)

    def cadastrar_usuario(self, nome: str, email: str, senha_plana: str) -> bool:
        if any(usuario.email == email for usuario in self.usuarios): 
            return False
        
        novo_usuario = Usuario(nome, email, senha_plana) 
        self.usuarios.append(novo_usuario)
        self._salvar_dados() 
        return True
    
    def login_usuario(self, email: str, senha_plana: str) -> bool:
        for usuario in self.usuarios: 
            if usuario.email == email:
                if usuario.verificar_senha(senha_plana): 
                    return True
                else:
                    return False
        return False

    def criar_carona(self, origem: str, data: str, horario: str) -> bool:
        nova_carona = Carona(origem, data, horario)
        self.caronas.append(nova_carona)
        self._salvar_dados()
        return True

    def listar_caronas(self) -> list[Carona]:
        return self.caronas
        
    def buscar_carona_origem(self, origem: str) -> list[Carona]:
        caronas_encontradas = [
            carona for carona in self.caronas if carona.origem.lower() == origem.lower()
        ]
        return caronas_encontradas
    
    def reservar_vagas(self, origem: str, data: str, horario: str, email_passageiro: str) -> bool:
        if not any(u.email == email_passageiro for u in self.usuarios):
            return False

        for carona in self.caronas:
            if carona.origem == origem and carona.data == data and carona.horario == horario:
                if carona.reservar_vagas(email_passageiro): 
                    self._salvar_dados()
                    return True
        return False
    
    def cancelar_vaga(self, origem: str, data: str, horario: str, email_passageiro: str) -> bool:
        for carona in self.caronas:
            if carona.origem == origem and carona.data == data and carona.horario == horario:
                if carona.cancelar_reserva(email_passageiro):
                    self._salvar_dados()
                    return True
        return False