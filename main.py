import tkinter as tk
from tkinter import messagebox, simpledialog
from models.sistemacaronas import SistemaCaronas

sistema = SistemaCaronas()

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Caronas - Login")

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack()

        self.exibir_opcoes_iniciais()

    def exibir_opcoes_iniciais(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.titulo_label = tk.Label(self.frame, text="Bem-vindo ao sistema de caronas da FGA", font=("Arial", 14))
        self.titulo_label.pack(pady=10)

        self.opcao = tk.StringVar()
        self.opcao.set("")

        self.login_button = tk.Button(self.frame, text="Login", command=lambda: self.exibir_formulario("login"))
        self.login_button.pack(pady=5)

        self.registro_button = tk.Button(self.frame, text="Registrar", command=lambda: self.exibir_formulario("registrar"))
        self.registro_button.pack(pady=5)

    def exibir_formulario(self, tipo):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.opcao.set(tipo)

        if tipo == "registrar":
            tk.Label(self.frame, text="Nome:").pack()
            self.nome_entry = tk.Entry(self.frame)
            self.nome_entry.pack()

        tk.Label(self.frame, text="Email:").pack()
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack()

        tk.Label(self.frame, text="Senha:").pack()
        self.senha_entry = tk.Entry(self.frame, show="*")
        self.senha_entry.pack()

        acao_texto = "Registrar" if tipo == "registrar" else "Login"
        self.acao_button = tk.Button(self.frame, text=acao_texto, command=self.executar_acao)
        self.acao_button.pack(pady=10)

        self.voltar_button = tk.Button(self.frame, text="Voltar", command=self.voltar_login)
        self.voltar_button.pack(pady=5)

    def executar_acao(self):
        if self.opcao.get() == "login":
            self.login()
        else:
            self.registrar()

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        if sistema.login_usuario(email, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.abrir_menu()
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos.")

    def registrar(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        sistema.cadastrar_usuario(nome, email, senha)
        messagebox.showinfo("Registro", "Usuário registrado com sucesso! Agora faça o login.")
        self.exibir_opcoes_iniciais()

    def abrir_menu(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        tk.Label(self.frame, text="Menu do Sistema de Caronas", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.frame, text="Criar Carona", command=self.criar_carona).pack(pady=5)
        tk.Button(self.frame, text="Reservar Vaga", command=self.reservar_vaga).pack(pady=5)
        tk.Button(self.frame, text="Listar Caronas", command=self.listar_caronas).pack(pady=5)
        tk.Button(self.frame, text="Buscar por Origem", command=self.buscar_por_origem).pack(pady=5)
        tk.Button(self.frame, text="Cancelar Reserva", command=self.cancelar_reserva).pack(pady=5)

        # Adicionando o botão "Voltar" para voltar ao login
        tk.Button(self.frame, text="Voltar ao Login", command=self.voltar_login).pack(pady=10)

    def voltar_login(self):
        # Voltar para a tela de login
        self.exibir_opcoes_iniciais()

    def criar_carona(self):
        origem = self.input_dialog("Origem da carona:")
        data = self.input_dialog("Data da carona:")
        horario = self.input_dialog("Horário da carona:")
        sistema.criar_carona(origem, data, horario)
        messagebox.showinfo("Sucesso", "Carona criada com sucesso!")

    def reservar_vaga(self):
        origem = self.input_dialog("Origem da carona:")
        data = self.input_dialog("Data da carona:")
        horario = self.input_dialog("Horário da carona:")
        email = self.input_dialog("Seu email:")
        sistema.reservar_vagas(origem, data, horario, email)
        messagebox.showinfo("Sucesso", "Vaga reservada com sucesso!")

    def listar_caronas(self):
        caronas = sistema.listar_caronas()
        if caronas:
            texto = "\n".join([f"Origem: {c.origem}, Data: {c.data}, Horário: {c.horario}, Vagas disponíveis: {c.vagas_disponiveis()}" for c in caronas])
            messagebox.showinfo("Caronas", texto)
        else:
            messagebox.showinfo("Caronas", "Nenhuma carona encontrada.")

    def buscar_por_origem(self):
        origem = self.input_dialog("Digite a origem:")
        caronas = sistema.buscar_carona_origem(origem)
        if not caronas:
            messagebox.showinfo("Busca por Origem", "Nenhuma carona encontrada para a origem informada.")
        else:
            texto = "\n".join([f"Origem: {c.origem}, Data: {c.data}, Horário: {c.horario}, Vagas disponíveis: {c.vagas_disponiveis()}" for c in caronas])
            messagebox.showinfo("Caronas encontradas", texto)

    def cancelar_reserva(self):
        origem = self.input_dialog("Origem da carona:")
        data = self.input_dialog("Data da carona:")
        horario = self.input_dialog("Horário da carona:")
        email = self.input_dialog("Seu email:")
        sistema.cancelar_vaga(origem, data, horario, email)
        messagebox.showinfo("Cancelado", "Reserva cancelada com sucesso!")

    def input_dialog(self, prompt):
        return simpledialog.askstring("Entrada", prompt)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
