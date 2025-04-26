import hashlib


class Usuario:
   def __init__(self, nome: str, email: str, senha:str):
      self._nome = nome
      self._email = email
      self._senha_hash = self.hash_senhas(senha)

   def hash_senhas(self, senha):
      return hashlib.sha256(senha.encode()).hexdigest()
   
   def autenticar(self, senha):
      if self._senha_hash == self.hash_senhas(senha):
         return True
      return False
