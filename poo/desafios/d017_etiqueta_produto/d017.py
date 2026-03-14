from rich import print as rprint
from rich.panel import Panel


class Produto:
    """
    Cria um produto e exibe sua etiqueta
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiquetar(self) -> str:
        conteudo = f'{self.nome.center(46, ' ')}'
        conteudo += f'{'-' * 46}'
        precof = f'R${self.preco:,.2f}'
        conteudo += f'{precof.center(46, '.')}'
        etiqueta = Panel(conteudo, title='Produto', expand=True, 
                     width=50, height=5)
        
        return etiqueta
    

p1 = Produto('S23FE', 2500)
rprint(p1.etiquetar())