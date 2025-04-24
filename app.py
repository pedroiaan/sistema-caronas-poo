from models.carona import  Carona 
from models.usuario import  Usuario

def teste_isolado():
    # 1. Criar um motorista
    motorista = Usuario("João", "senha123", "motorista")

    # 2. Criar uma carona diretamente (origem, destino – sempre "FGA", horário, motorista)
    carona = Carona(origem="Taguatinga", destino="FGA", horario="09:00", motorista=motorista)

    # 3. Verificar estado inicial
    print("Antes de participar:")
    print("Vagas totais:", carona.vagas)
    print("Passageiros:", carona.passageiros)

    # 4. Criar um passageiro e fazê-lo participar
    passageiro = Usuario("Ana", "senha456", "passageiro")
    sucesso = passageiro.participar_carona(carona)

    # 5. Mostrar resultados
    print("\nTentativa de embarque:", "Sucesso" if sucesso else "Falha")
    print("Vagas restantes:", carona.vagas - len(carona.passageiros))
    print("Passageiros agora:", [u.nome for u in carona.passageiros])

if __name__ == "__main__":
    teste_isolado()