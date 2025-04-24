# 🚗 Sistema de Caronas para Universitários - FGA

Este é um projeto de terminal desenvolvido em **Python com Programação Orientada a Objetos (POO)**, que simula uma rede de caronas voltada a estudantes da FGA (Faculdade do Gama - UnB).

---

## 🎯 Objetivo

Oferecer uma estrutura básica para que estudantes possam:
- Se cadastrar e autenticar no sistema
- Criar caronas com origem e horário definidos (destino fixo: FGA)
- Consultar caronas disponíveis
- Reservar e cancelar vagas em caronas

---

## 🧱 Estrutura do Projeto

O sistema é composto por três classes principais:

### 🔐 `Usuario`
- Armazena dados do usuário (nome, e-mail e senha)
- Realiza autenticação de senha com hash seguro

### 🚙 `Carona`
- Representa uma carona com origem, horário e controle de vagas
- Permite reservar e cancelar vagas

### 🧠 `SistemaCaronas`
- Gerencia os usuários e caronas
- Controla a lógica de cadastro, login, criação e reserva de caronas

---

## 📌 Regras do Sistema

- O destino de todas as caronas é **sempre a FGA**
- Cada carona tem **4 vagas disponíveis por padrão**
- Um usuário pode **oferecer e receber caronas**
- Senhas são armazenadas com **hash SHA-256** (sem bibliotecas externas)
- Não é utilizada persistência de dados (sem JSON, banco de dados, etc.)

---

## 🚀 Como Executar

1. Clone este repositório
2. Execute o arquivo principal com:
   ```bash
   python app.py
