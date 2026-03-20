from rich import print as rprint
from time import sleep

class Livro:
    def __init__(self, titulo, quant_pag):
        self.titulo = titulo
        self.quant_pag = quant_pag
        self.pag_atual = 1

        print(f"Você abriu o livro '{self.titulo}' que tem {self.quant_pag}páginas no total. Você está agora na página {self.pag_atual}.")

    def fim_livro(self):
        return True if self.pag_atual == self.quant_pag else False

    def avancar_pagina(self, quant_avancar):
        
        cont = 0
        for _ in range(quant_avancar):
            if not self.fim_livro():
                self.pag_atual += 1
                cont += 1
                sleep(0.3)
                rprint(f'pag{self.pag_atual} :arrow_forward: ', end='')

        rprint(f'Você avançou {cont} páginas e está agora na página {self.pag_atual}.')

        if self.fim_livro():
            rprint(f"Você chegou ao final do livro '{self.titulo}'.")



l1 = Livro('Sonhos na casa da bruxa', 10)
l1.avancar_pagina(5)
l1.avancar_pagina(2)
l1.avancar_pagina(3)
l1.avancar_pagina(2)

