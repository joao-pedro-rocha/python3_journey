from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    
    def preparar(self):
        txt = '--- Iniciando o Preparo ---\n'
        txt += f'1. {self.ferver()}\n'
        txt += f'2. {self.misturar()}\n'
        txt += f'3. {self.servir()}\n'
        txt += '--- Bebida Pronta ---\n'

        return txt 

    def ferver(self):
        return 'Fervendo a água em 100 graus Celcius.'

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
        
    def misturar(self):
        return 'Passando água pressurizada pelo pó de café moído.'

    def servir(self):
        return 'Servindo em xícara pequena.'


class Cha(BebidaQuente):
        
    def misturar(self):
        return 'Mergulhando sache de ervas na água.'

    def servir(self):
        return 'Servindo na caneca de porcelana com limão.'


class Leite(BebidaQuente):
        
    def misturar(self):
        return 'Passando vapor pressurizado pelo bico do leite.'

    def servir(self):
        return 'Servindo na caneca grande, já com café.'


def main():
    b1 = Cafe()
    print(b1.preparar())

    b2 = Cha()
    print(b2.preparar())

    b3 = Leite()
    print(b3.preparar())


if __name__ == '__main__':
    main()
