from abc import ABC, abstractmethod
from random import randint, choice

# from rich import print as rprint


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        ataque = choice(self.golpes)
        print(f'{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com {ataque} de força {forca}.')
        dano = randint(0, forca)
        alvo.receber_dano(dano)
        print(f'{alvo.nome}({alvo.vida}) recebeu dano de {dano}')

    def receber_dano(self, dano):
        self.vida -= dano

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Golpe de machado', 'Pulo giratório', 'Soco']
    
    def curar(self):
        cura = randint(0, 100)
        print(f'{self.nome}({self.vida}) fez um curativo nos ferimentos e recuperou {cura} pontos de vida')
        self.vida += cura
        


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Abracadabra', 'Bola de fogo', 'Raio']
        
    def curar(self):
        cura = randint(0, 100)
        print(f'{self.nome}({self.vida}) fez uma magia de cura e recuperou {cura} pontos de vida')
        self.vida += cura


def main():
    p1 = Guerreiro(nome='toderolex', vida=200)
    p2 = Mago(nome='shierk', vida=150)

    p2.atacar(p1, 100)
    p1.curar()


if __name__ == '__main__':
    main()