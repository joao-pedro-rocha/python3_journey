from rich import print as rprint
from rich import inspect
from abc import ABC, abstractmethod
from math import pow, pi, tan

class Poligono(ABC):
    def __init__(self, qtd_lados:int):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lado:float=2):
        self.lado: float  = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return pow(self.lado, 2)


class Circulo(Poligono):
    def __init__(self, raio:float=2):
        self.raio:float = raio

    def perimetro(self):
        return 2 * pi * self.raio
        
    def area(self):
        return pi * pow(self.raio, 2)


class Outro(Poligono):
    def __init__(self, qtd_lados, lado:float=2):
        super().__init__(qtd_lados) # necessario para instaciar o atributo da classe mae
        self.lado = lado

    def perimetro(self):
        return self.qtd_lados * self.lado

    def area(self):
        return (self.qtd_lados * pow(self.lado, 2)) / (4 * tan(pi/self.qtd_lados))
        
def main():
    p1 = Quadrado(lado=4)
    inspect(p1, methods=True)
    print(f'O perímetro de um quadrado com lado {p1.lado} é {p1.perimetro()}')
    print(f'A área de um quadrado com lado {p1.lado} é {p1.area()}\n')

    p2 = Circulo(4)
    inspect(p2, methods=True)
    print(f'O perímetro de um círculo com raio {p2.raio} é {round(p2.perimetro(), 2)}')
    print(f'A área de um círculo com raio {p2.raio} é {round(p2.area(), 2)}')

    p3 = Outro(qtd_lados=10, lado=5)
    inspect(p3, methods=True)
    print(f'O perímetro de um polígono com {p3.qtd_lados} lados e cada lado medindo {p3.lado} é {round(p3.perimetro(), 2)}')
    print(f'A área de um polígono com {p3.qtd_lados} lados e cada lado medindo {p3.lado} é {round(p3.area(), 2)}')

if __name__ == '__main__':
    main()
