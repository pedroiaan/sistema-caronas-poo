# 🚗 Sistema de Caronas para Universitários - FGA

Um sistema simples de caronas com interface gráfica usando **Python** e **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** e **JSON** para persistência de dados.

---

## 🎯 Objetivo

Oferecer uma estrutura básica para que estudantes possam:
- Se cadastrar e autenticar no sistema
- Criar caronas com origem e horário definidos (destino fixo: FGA)
- Consultar caronas disponíveis
- Reservar e cancelar vagas em caronas

---

## ✅ Funcionalidades

- ✅ Registro e login de usuários
- ✅ Criação de caronas (origem, data, horário)
- ✅ Reserva e cancelamento de vagas
- ✅ Listagem de caronas disponíveis
- ✅ Busca de caronas por origem
- ✅ Interface gráfica moderna com **CustomTkinter**
- Persistir dados utilizando **JSON**, garantindo que as informações das caronas e usuários sejam mantidas entre execuções

---

## 🗂 Estrutura do Projeto

```
projeto-caronas/
├── main.py                  # Interface gráfica (CustomTkinter)
├── README.md                # Arquivo de documentação
└── models/
    ├── sistemacaronas.py    # Lógica principal do sistema de caronas
    └── carona.py            # Classe que representa uma carona
└── dados/
     ├──  banc.py            # Manipulação do arquivo JSON (carregamento e salvamento)
     └── banco.json          # Arquivo onde os dados de usuários e caronas são armazenados
```

---

## 🚀 Como Executar

1. Instale o Python 3.10 ou superior.
2. Clone este repositório ou baixe os arquivos.
3. Instale a biblioteca necessária:

```bash
pip install customtkinter
```

4. Execute o programa principal:

```bash
python main.py
```

---

## 🖼 Interface

### Tela Inicial

- [x] Login
- [x] Registro

### Menu Principal

- [x] Criar Carona
- [x] Reservar Vaga
- [x] Listar Caronas
- [x] Buscar por Origem
- [x] Cancelar Reserva
- [x] Voltar (logout)

---

## 📦 Requisitos

- Python 3.10+
- Biblioteca [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)

---

## 👤 Autor

**Pedro**  
Estudante de Engenharia de Software - FGA  
Projeto acadêmico de prática com Python, POO, manipulação de JSON e GUI.

---

## 📄 Licença

Este projeto é livre para fins acadêmicos e educacionais.
