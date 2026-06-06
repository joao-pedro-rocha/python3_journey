# classe mae transporte com distacia e frete e met abs calc frete
# classe filha moto fator 0.50, distacia livre
# classe filha caminhao fator 1.20 dist min 50km
# classe filha drone fator 9.50 dist max 10km

from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, dist, frete=0):
        self.dist = dist
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, dist):
        super().__init__(dist)
        
    def calc_frete(self):
        self.frete = self.dist * Moto.fator
        return f'Frete de moto em {self.dist}Km = R${self.frete:.2f}'

class Caminhao(Transporte):
    fator = 1.20
    
    def __init__(self, dist):
        super().__init__(dist)

    def calc_frete(self):
        if self.dist < 50:
            return 'Frete mínimo para caminhão é de 50Km'
        else:
            self.frete = self.dist * Caminhao.fator
            return f'Frete de caminhão em {self.dist}Km = R${self.frete:.2f}'

        
class Drone(Transporte):
    fator  = 9.50

    def __init__(self, dist):
        super().__init__(dist)

    def calc_frete(self):
        if self.dist > 10:
            return 'Frete máximo para drone é de 10Km'
        else:
            self.frete = self.dist * Drone.fator
            return f'Frete de drone em {self.dist}Km = R${self.frete:.2f}'

def main():
    dist = 93
    entrega = Caminhao(dist).calc_frete()

    print(entrega)


main()
