
import hashlib


from .mixins import SerializableMixin 

class Usuario(SerializableMixin):
   def __init__(self, nome: str, email: str, senha_plana: str, senha_hash: str = None):
      self._nome = nome
      self._email = email
      if senha_hash:
         self._senha_hash = senha_hash
      else:
         self._senha_hash = self._hash_senha(senha_plana)

   @staticmethod
   def _hash_senha(senha_plana: str) -> str:
      return hashlib.sha256(senha_plana.encode()).hexdigest()

   def verificar_senha(self, senha_plana: str) -> bool:
      return self._senha_hash == self._hash_senha(senha_plana)

   @property
   def nome(self) -> str:
      return self._nome

   @property
   def email(self) -> str:
      return self._email
    
   @property
   def senha_hash(self) -> str:
      return self._senha_hash

   def to_dict(self) -> dict:
      return {
            "_nome": self.nome,
            "_email": self.email,
            "_senha_hash": self.senha_hash 
      }

   @classmethod
   def from_dict(cls, data: dict) -> 'Usuario':
      return cls(
            nome=data["_nome"],
            email=data["_email"],
            senha_plana="", 
            senha_hash=data["_senha_hash"]
      )

   def __repr__(self):
      return f"<Usuario nome='{self.nome}' email='{self.email}'>"