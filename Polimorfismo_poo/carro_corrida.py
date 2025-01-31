from carro import Carro 
#recriar o método acelera 
#engenharia de promt olhar depois 
class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    def acelera(self):
        self.velocidade += 5
        print("Aceleração de corrida! A velocidade aumentou em 5 km/h")