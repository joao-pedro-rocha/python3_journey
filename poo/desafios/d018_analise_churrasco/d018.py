from rich import print as rprint
from rich.panel import Panel


class Churrasco:
    '''
    Cria uma churrasco e faz sua analise
    '''
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    consumo:float = 0.400
    preco:float = 82.40

    def analise(self):
        custo_total:float = (Churrasco.consumo * self.quant) * Churrasco.preco
        qtd_carne:float = Churrasco.consumo * self.quant
        custo_individual:float = custo_total / self.quant

        conteudo = f'Analisando [green]{self.titulo}[/green] com [blue]{self.quant} convidados[/blue].\n'
        conteudo += f'Cada convidado comerá {Churrasco.consumo} Kg e cada Kg custa R${Churrasco.preco:.2f}.\n'
        conteudo += f'Recomendo comprar [blue]{qtd_carne:.3f} Kg[/blue] de carne.\n'
        conteudo += f'O custo total será de [green]R${custo_total:.2f}[/green].\n'
        conteudo += f'Cada pessoa pagará [yellow]R${custo_individual:.2f}[/yellow] para participar.'

        return Panel(conteudo, title=self.titulo, width=80, height=7)


c1 = Churrasco('Churras dos amigos', 15)
rprint(c1.analise())
