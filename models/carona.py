class Carona:
    def __init__(self, origem: str, data_hora: str, vagas_totais: int = 4):
        self._vagas_totais = vagas_totais
        self._vagas_ocupadas = 0
        self.origem = origem
        self.data_hora = data_hora

    def vagas_disponiveis(self):
        return self._vagas_totais - self._vagas_ocupadas

    def reservar_vagas(self):
        if self._vagas_ocupadas < self._vagas_totais:
            self._vagas_ocupadas += 1
            return True
        else:
            return False
    
    def cancelar_reserva(self):
        if self._vagas_ocupadas >= 1:
            self._vagas_ocupadas -= 1
            return True
        return False
        
