# declaracao de classe
class Gafanhoto:
    def __init__(self):
        # atributos
        self.nome = ''
        self.idade = 0

    # metodos
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.' # self é uma mencao ao proprio objeto
    
    def aniversario(self):
        self.idade += 1


# declaracao de objeto
g1 = Gafanhoto()
g1.nome = 'João'
g1.idade = 23
print(g1.mensagem())
g1.aniversario()
