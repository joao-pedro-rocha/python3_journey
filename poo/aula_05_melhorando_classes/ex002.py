# declaracao de classe
class Gafanhoto:
    """
    Esta classe cria um gafanhoto, que é uma pessoa com nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome='', idade=0):
        # atributos
        self.nome = nome
        self.idade = idade

    # metodos
    def __str__(self):
        # retorna esta frase ao imprimir o objeto
        # self é uma mencao ao proprio objeto
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'
    
    def aniversario(self):
        self.idade += 1

    def __getstate__(self):
        return f'Estado: nome = {self.nome}, idade = {self.idade}'


# declaracao de objeto
g1 = Gafanhoto('joao', 24)
print(g1)
g1.aniversario()

g2 = Gafanhoto()
print(g2)
g2.aniversario()

# exibe a docstring da classe
print(Gafanhoto.__doc__)

# exibe o objeto em formato de dicionario
print(g1.__dict__)

# por padrao exibe o objeto em forma de dicionario mas, por ser um metodo, pode
# ser sobrescrito
print(g1.__getstate__())

# mostra o nome da classe do objeto
print(g1.__class__)