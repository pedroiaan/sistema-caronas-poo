class Carona:
    def __init__(self, origem: str, data: str, horario: str, vagas_totais: int = 4):
        self._vagas_totais = vagas_totais
        self._passageiros = []
        self.origem = origem
        self.data  = data
        self.horario = horario

    def vagas_disponiveis(self):
        return self._vagas_totais - len(self._passageiros)

    def reservar_vagas(self, email):
        if len(self._passageiros) < self._vagas_totais:
            self._passageiros.append(email)
            return True
        return False
    
    def cancelar_reserva(self, email):
        if email in self._passageiros:
            self._passageiros.remove(email)
            return True
        return False
        
