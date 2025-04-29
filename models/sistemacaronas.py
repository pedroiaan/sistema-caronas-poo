from .carona import Carona
from .usuario import Usuario

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

    def criar_carona(self, origem, data, horario):
        nova_carona = Carona(origem, data, horario)
        self.caronas.append(nova_carona)
    
    def listar_caronas(self):
        if not self.caronas:
            print("Não há caronas registradas")
        else:
            for carona in self.caronas:
                print(f"Origem: {carona.origem}, Data: {carona.data}, Horario: {carona.horario}, Vagas Disponíveis: {carona.vagas_disponiveis()}")

    def buscar_carona_origem(self, origem):
        if not self.caronas:
            print("Não há caronas registradas para esse ponto de partida")
            return
    
        lista_encotradas = []
        for carona in self.caronas:
            if carona.origem == origem:
                lista_encotradas.append(Carona)
        
        if not lista_encotradas:
            print("Não há caronas registradas para esse ponto de partida")
            return
        
        print("As caronas para esse ponto de partida são:")
        for carona in self.caronas:
            if origem == carona.origem:
                print(f"No dia {carona.data}, às {carona.horario}")

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