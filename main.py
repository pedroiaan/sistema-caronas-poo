# main.py
from customtkinter import *
from tkinter import messagebox, simpledialog
from models.sistemacaronas import SistemaCaronas
import re 

set_appearance_mode("dark")
set_default_color_theme("blue")

sistema = SistemaCaronas()

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Caronas - Login")
        self.root.geometry("400x500")

        self.frame = CTkFrame(root, corner_radius=20)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.exibir_opcoes_iniciais()

    def exibir_opcoes_iniciais(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        CTkLabel(self.frame, text="Bem-vindo ao sistema de caronas da FGA", font=CTkFont(size=16, weight="bold")).pack(pady=10)

        self.opcao = StringVar(value="")

        CTkButton(self.frame, text="Login", command=lambda: self.exibir_formulario("login")).pack(pady=10)
        CTkButton(self.frame, text="Registrar", command=lambda: self.exibir_formulario("registrar")).pack(pady=10)

    def exibir_formulario(self, tipo):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.opcao.set(tipo)

        if tipo == "registrar":
            CTkLabel(self.frame, text="Nome:").pack()
            self.nome_entry = CTkEntry(self.frame)
            self.nome_entry.pack(pady=5)

        CTkLabel(self.frame, text="Email:").pack()
        self.email_entry = CTkEntry(self.frame)
        self.email_entry.pack(pady=5)

        CTkLabel(self.frame, text="Senha:").pack()
        self.senha_entry = CTkEntry(self.frame, show="*")
        self.senha_entry.pack(pady=5)

        acao_texto = "Registrar" if tipo == "registrar" else "Login"
        CTkButton(self.frame, text=acao_texto, command=self.executar_acao).pack(pady=10)
        CTkButton(self.frame, text="Voltar", command=self.voltar_login).pack(pady=5)

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
        if sistema.cadastrar_usuario(nome, email, senha): # Adicionado if para checar retorno
            messagebox.showinfo("Registro", "Usuário registrado com sucesso! Agora faça o login.")
            self.exibir_opcoes_iniciais()
        else:
            messagebox.showerror("Erro", "Não foi possível registrar o usuário. Email já pode estar em uso.")


    def abrir_menu(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        CTkLabel(self.frame, text="Menu do Sistema de Caronas", font=CTkFont(size=16, weight="bold")).pack(pady=10)

        CTkButton(self.frame, text="Criar Carona", command=self.criar_carona).pack(pady=5)
        CTkButton(self.frame, text="Reservar Vaga", command=self.reservar_vaga).pack(pady=5)
        CTkButton(self.frame, text="Listar Caronas", command=self.listar_caronas).pack(pady=5)
        CTkButton(self.frame, text="Buscar por Ponto de Partida", command=self.buscar_por_origem).pack(pady=5)
        CTkButton(self.frame, text="Cancelar Reserva", command=self.cancelar_reserva).pack(pady=5)
        CTkButton(self.frame, text="Voltar ao Login", command=self.voltar_login).pack(pady=10)

    def voltar_login(self):
        self.exibir_opcoes_iniciais()

    def input_dialog(self, prompt_text: str, title: str = "Entrada") -> str | None:
        """Caixa de diálogo para entrada de texto simples."""
        return simpledialog.askstring(title, prompt_text, parent=self.root)

    def get_validated_input(self, prompt_text: str, regex_pattern: str, 
                            error_empty_msg: str, error_pattern_msg: str, 
                            title: str = "Entrada") -> str | None:
       
        while True:
            value = simpledialog.askstring(title, prompt_text, parent=self.root)
            if value is None: 
                return None
            
            value_stripped = value.strip() 

            if not value_stripped: 
                messagebox.showerror("Erro de Entrada", error_empty_msg, parent=self.root)
                continue 

            if not re.fullmatch(regex_pattern, value_stripped):
                messagebox.showerror("Erro de Entrada", error_pattern_msg, parent=self.root)
                continue  
            
            return value_stripped 

    def criar_carona(self):
        origem = self.input_dialog("Ponto de Partida da carona:")
        if origem is None or not origem.strip(): 
            messagebox.showwarning("Entrada Inválida", "O ponto de partida não pode ser vazio.", parent=self.root)
            return

        data = self.get_validated_input(
            prompt_text="Data da carona (DD/MM):",
            regex_pattern=r"^\d{2}/\d{2}$",
            error_empty_msg="A data não pode ser vazia.",
            error_pattern_msg="Formato de data inválido. Use DD/MM (ex: 29/05)."
        )
        if data is None: return # Usuário cancelou

        horario = self.get_validated_input(
            prompt_text="Horário da carona (HH:MM):",
            regex_pattern=r"^\d{2}:\d{2}$",
            error_empty_msg="O horário não pode ser vazio.",
            error_pattern_msg="Formato de horário inválido. Use HH:MM (ex: 14:30)."
        )
        if horario is None: return 
        try:
            dia, mes = map(int, data.split('/'))
            hora, minuto = map(int, horario.split(':'))
            if not (1 <= dia <= 31 and 1 <= mes <= 12):
                messagebox.showerror("Data Inválida", "Dia ou mês inválido.", parent=self.root)
                return
            if not (0 <= hora <= 23 and 0 <= minuto <= 59):
                messagebox.showerror("Horário Inválido", "Hora ou minuto inválido.", parent=self.root)
                return
        except ValueError:
            messagebox.showerror("Erro de Formato", "Data ou Horário contém caracteres não numéricos onde esperado.", parent=self.root)
            return

        if sistema.criar_carona(origem.strip(), data, horario):
            messagebox.showinfo("Sucesso", "Carona criada com sucesso!", parent=self.root)
        else:
            messagebox.showerror("Erro", "Não foi possível criar a carona.", parent=self.root)


    def reservar_vaga(self):
        origem = self.input_dialog("Ponto de Partida da carona para reservar:")
        if origem is None or not origem.strip():
            messagebox.showwarning("Entrada Inválida", "O ponto de partida não pode ser vazio.", parent=self.root)
            return

        data = self.get_validated_input(
            prompt_text="Data da carona (DD/MM):",
            regex_pattern=r"^\d{2}/\d{2}$",
            error_empty_msg="A data não pode ser vazia.",
            error_pattern_msg="Formato de data inválido. Use DD/MM."
        )
        if data is None: return

        horario = self.get_validated_input(
            prompt_text="Horário da carona (HH:MM):",
            regex_pattern=r"^\d{2}:\d{2}$",
            error_empty_msg="O horário não pode ser vazio.",
            error_pattern_msg="Formato de horário inválido. Use HH:MM."
        )
        if horario is None: return

        email = self.input_dialog("Seu email para reserva:")
        if email is None or not email.strip():
            messagebox.showwarning("Entrada Inválida", "O email não pode ser vazio.", parent=self.root)
            return

        if sistema.reservar_vagas(origem.strip(), data, horario, email.strip()):
            messagebox.showinfo("Sucesso", "Vaga reservada com sucesso!", parent=self.root)
        else:
            messagebox.showerror("Erro", "Não foi possível reservar a vaga. Verifique os dados da carona ou se há vagas disponíveis.", parent=self.root)

    def listar_caronas(self):
        caronas = sistema.listar_caronas()
        if caronas:
            texto_caronas = []
            for c in caronas:
                num_passageiros = len(c._passageiros) if c._passageiros else 0
                vagas_disp = c._vagas_totais - num_passageiros
                texto_caronas.append(f"Ponto de partida: {c.origem}, Data: {c.data}, Horário: {c.horario}, Vagas disponíveis: {vagas_disp}")
            
            texto_final = "\n".join(texto_caronas)
            messagebox.showinfo("Caronas", texto_final if texto_final else "Nenhuma carona encontrada.", parent=self.root)
        else:
            messagebox.showinfo("Caronas", "Nenhuma carona encontrada.", parent=self.root)


    def buscar_por_origem(self):
        origem = self.input_dialog("Digite a origem para buscar:")
        if origem is None or not origem.strip():
            messagebox.showwarning("Entrada Inválida", "A origem para busca não pode ser vazia.", parent=self.root)
            return
            
        caronas = sistema.buscar_carona_origem(origem.strip())
        if not caronas:
            messagebox.showinfo("Busca por Origem", "Nenhuma carona encontrada para a origem informada.", parent=self.root)
        else:
            texto_caronas = []
            for c in caronas:
                num_passageiros = len(c._passageiros) if c._passageiros else 0
                vagas_disp = c._vagas_totais - num_passageiros
                texto_caronas.append(f"Ponto de Partida: {c.origem}, Data: {c.data}, Horário: {c.horario}, Vagas disponíveis: {vagas_disp}")
            
            texto_final = "\n".join(texto_caronas)
            messagebox.showinfo("Caronas encontradas", texto_final, parent=self.root)


    def cancelar_reserva(self):
        origem = self.input_dialog("Ponto de Partida da carona para cancelar reserva:")
        if origem is None or not origem.strip():
            messagebox.showwarning("Entrada Inválida", "O ponto de partida não pode ser vazio.", parent=self.root)
            return

        data = self.get_validated_input(
            prompt_text="Data da carona (DD/MM):",
            regex_pattern=r"^\d{2}/\d{2}$",
            error_empty_msg="A data não pode ser vazia.",
            error_pattern_msg="Formato de data inválido. Use DD/MM."
        )
        if data is None: return

        horario = self.get_validated_input(
            prompt_text="Horário da carona (HH:MM):",
            regex_pattern=r"^\d{2}:\d{2}$",
            error_empty_msg="O horário não pode ser vazio.",
            error_pattern_msg="Formato de horário inválido. Use HH:MM."
        )
        if horario is None: return

        email = self.input_dialog("Seu email para cancelar a reserva:")
        if email is None or not email.strip(): 
            messagebox.showwarning("Entrada Inválida", "O email não pode ser vazio.", parent=self.root)
            return

        if sistema.cancelar_vaga(origem.strip(), data, horario, email.strip()):
            messagebox.showinfo("Cancelado", "Reserva cancelada com sucesso!", parent=self.root)
        else:
            messagebox.showerror("Erro", "Não foi possível cancelar a reserva. Verifique os dados da carona ou se você realmente tinha uma reserva.", parent=self.root)


if __name__ == "__main__":
    app = CTk()
    LoginApp(app)
    app.mainloop()