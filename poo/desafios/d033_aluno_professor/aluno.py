from datetime import datetime


class Pessoa:
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nasc = None
        self.nasc = nasc

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nasc(self):
        return self._nasc

    @nasc.setter
    def nasc(self, nasc):
        if 1946 <=nasc <=datetime.now().year:
            self._nasc = nasc
        else:
            raise ValueError('Ano inválido!')

    def idade(self) -> int:
        idade = datetime.now().year - self._nasc

        return idade


class Aluno(Pessoa):
    cursos = ['ADM', 'ADS']
    
    def __init__(self, nome:str, nasc:int, curso:str=None):
        super().__init__(nome, nasc)

        if curso == None:
            self._curso = curso
        elif self.validar_curso(curso):
            self._curso = curso.upper()
        else:
            raise ValueError('Escolha um curso válido ou adicione um novo curso na lista!')

    def validar_curso(self, curso:str) -> bool:
        curso_valido = False
        
        if curso.upper() in Aluno.cursos:
            curso_valido = True

        return curso_valido

    @property
    def curso(self) -> str:
        return self._curso

    @curso.setter
    def curso(self, curso:str):
        if self.validar_curso(curso):
            self._curso = curso.upper()
        else:
            raise ValueError('Escolha um curso válido ou adicione um novo curso na lista!')

    def add_curso(self, curso:str):
        if isinstance(curso, str):
            Aluno.cursos.append(curso.upper())
