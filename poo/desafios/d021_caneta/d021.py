from rich import print as rprint


class Caneta:
    '''
    Cria uma caneta que pode ser destampada, possui uma cor e pode escrever.
    '''

    def __init__(self, cor='azul'):
        escolha = ''

        match cor.lower().strip():
            case 'azul':
                escolha = 'blue'
            case 'verde':
                escolha = 'green'
            case 'vermelho' | 'vermelha':
                escolha = 'red'
            case _:
                escolha = 'white'

        self.cor = escolha
        self.tampada = True
    
    def destampar(self):
        self.tampada = False

    def escrever(self, texto):
        if self.tampada:
            rprint(f':prohibited: [{self.cor}]Caneta[/{self.cor}] tampada!')
        else:
            rprint(f'[{self.cor}]{texto}[/{self.cor}]', end='')

    def quebrar_linha(self):
        rprint('\n')
    
c1 = Caneta('azul')
c2 = Caneta('verde')
c3 = Caneta('vermelha')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Ola, mundo!')
c1.quebrar_linha()
c2.escrever('testando')
c1.quebrar_linha()
c3.escrever('123')
