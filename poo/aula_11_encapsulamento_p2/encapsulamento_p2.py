class Avaliacao:
    
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # def set_nota(self, nota):
    #     if 0 <= nota <= 10:
    #         self._nota = nota
    #     else:
    #         print('Nota inválida!')

    # def get_nota(self):
    #     return self._nota
    
    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print('Nota inválida!')

    @nota.deleter
    def nota(self):
        pass