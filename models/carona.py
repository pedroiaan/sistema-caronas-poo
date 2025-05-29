
from .mixins import SerializableMixin 

class Carona(SerializableMixin):
    def __init__(self, origem: str, data: str, horario: str, vagas_totais: int = 4, passageiros=None):
        self.origem = origem 
        self.data  = data    
        self.horario = horario 
        self._vagas_totais = vagas_totais
        self._passageiros = passageiros if passageiros is not None else []

    def vagas_disponiveis(self) -> int:
        return self._vagas_totais - len(self._passageiros)

    def reservar_vagas(self, email: str) -> bool: 
        if len(self._passageiros) < self._vagas_totais and email not in self._passageiros:
            self._passageiros.append(email)
            return True
        return False
    
    def cancelar_reserva(self, email: str) -> bool:
        if email in self._passageiros:
            self._passageiros.remove(email)
            return True
        return False
        
    def to_dict(self) -> dict: 
        return {
            "origem": self.origem,
            "data": self.data,
            "horario": self.horario,
            "passageiros": self._passageiros 
        }

    @classmethod
    def from_dict(cls, dados: dict) -> 'Carona':
        return cls(
            origem=dados["origem"],
            data=dados["data"],
            horario=dados["horario"],
            passageiros=dados.get("passageiros", [])
        )

    def __repr__(self):
        return f"<Carona origem='{self.origem}' data='{self.data}' horario='{self.horario}'>"