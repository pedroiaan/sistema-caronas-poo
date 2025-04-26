from carona import Carona
from usuario import Usuario

class SistemaCaronas:
    def __init__(self):
        self.usuarios = {}
        self.caronas = []
    
    def cadastrar_usuario(self, nome, email, senha):
        if email in self.usuarios:
            return False
        else:
            print("cadastro concluido")
            novo_usuario = Usuario(nome, email, senha)
            self.usuarios[email] = novo_usuario
    
    def login_usuario(self, email, senha):
        if email in self.usuarios:
            usuario = self.usuarios[email]

            if usuario.autenticar(senha):
                return True
        return False

    def criar_carona(self, origem, data_hora):
        nova_carona = Carona(origem, data_hora)
        self.caronas.append(nova_carona)
    
    def listar_caronas(self):
        if not self.caronas:
            print("Não há caronas registradas")
        else:
            for carona in self.caronas:
                print(f"Origem: {carona.origem}, Data e Hora: {carona.data_hora}, Vagas Disponíveis: {carona.vagas_disponiveis()}")

