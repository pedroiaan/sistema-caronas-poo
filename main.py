from models.carona import Carona
from models.usuario import Usuario
from models.sistemacaronas import SistemaCaronas

def menu_login():
        print("\n")
        print("Bem-Vindo a página de login/registro do sistema de caronas da FGA.")
        print("----------------------------------------------")
        print("Por favor selecione o numero da opção desejada")
        print("----------------------------------------------")
        print("1. Se registrar")
        print("2. Realizar login")
        print("3. Sair")
        print("----------------------------------------------")
        choice = int(input("Digite sua escolha: "))
        return choice

def menu_inicial():
    print("Bem Vindo ao sistema de caronas da FGA. ")
    print("\n")
    print("Por favor selecione o numero da opção desejada")
    print("----------------------------------------------")
    print("1. Criar Carona")
    print("2. Reservar Vaga")
    print("3. Listar Caronas")
    print("4. Buscar Carona por Origem")
    print("5. Cancelar Reserva")
    print("6. Voltar")
    choice_2 = int(input("digite sua escolha: "))
    return choice_2

def app():
    sistema = SistemaCaronas()
    while True:
        choice = menu_login()
        
        
        if choice == 1:
            print("\n")
            print("Digite seus dados abaixo para se cadastrar.")
            print("------------------------------------------")
            nome = input("Digite seu nome: ")
            email = input("digite seu email: ")
            senha = input("digite sua senha: ")
            sistema.cadastrar_usuario(nome, email, senha)
        
        elif choice == 2:
            print("\n")
            print("Digite seus dados abaixo para realizar seu login.")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            if sistema.login_usuario(email, senha):
                while True:
                    choice_2 = menu_inicial()
                    
                    if choice_2 == 1:
                        origem = input("Qual é a origem? ")
                        data = input ("Qual é a data? ")
                        horario = input("Qual é o horario? ")
                        sistema.criar_carona(origem, data, horario)
                    
                    elif choice_2 == 2:
                        origem = input("Qual é a origem? ")
                        data = input ("Qual é a data? ")
                        horario = input("Qual é o horario? ")
                        email = input("E digite seu email para cadastrar: ")
                        sistema.reservar_vagas(origem, data, horario, email)
                    
                    elif choice_2 == 3:
                        print("Essas são as viagens registradas no sistema")
                        print("-------------------------------------------")
                        sistema.listar_caronas()

                    elif choice_2 == 4:
                        origem = input("Digite a origem da carona, para ter os horários e datas registradas.")
                        print("-----------------------------------------------------------------------------")
                        sistema.buscar_carona_origem(origem)
                    
                    elif choice_2 == 5:
                        print("Para conseguir cancelar a siga essas instruções.")
                        print("------------------------------------------------")
                        origem = input("Qual é a origem? ")
                        data = input ("Qual é a data? ")
                        horario = input("Qual é o horario? ")
                        email = input("Digite seu email: ")
                        sistema.cancelar_vaga(origem, data, horario, email)
                    
                    elif choice_2 == 6:
                        print("Voltando para o menu inicial...")
                        break
            else:
                print("Senha ou email incorreto.")
            
        elif choice == 3:
            print("sistema encerrado.")
            break

if __name__ == "__main__":
    app()

