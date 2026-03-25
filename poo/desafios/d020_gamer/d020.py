from rich import print as rprint
from rich.panel import Panel


class Gamer:
    '''
    Cria uma classe Gamer que possibilita adicionar jogos favoritos e lista-los
    '''

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, nome_jogo):
        self.jogos_favoritos.append(nome_jogo)
        self.jogos_favoritos.sort()

    def ficha(self):
        conteudo = f'Nome real: [black on blue] {self.nome} [/black on blue]\n'
        conteudo += 'Jogos favoritos:\n'
        
        for jogo in self.jogos_favoritos:
            conteudo += f':video_game: [blue]{jogo}[/blue]\n'
        
        ficha = Panel(conteudo, title=f'Jogador <{self.nick}>', width=40)

        return ficha

j1 = Gamer('Joao', 'toderolex')
j1.add_favoritos('Mario')
j1.add_favoritos('Apex')
rprint(j1.ficha())
