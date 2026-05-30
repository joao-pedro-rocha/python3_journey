from rich import print as rprint
from rich import inspect
from abc import ABC, abstractmethod # permite classes abstratas


class Pessoa(ABC):
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self): # metodos abstratos sao definidos apenas nas classes filhas
        pass           # e sao obrigatorios

    
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        pass

    def estudar(self):
        print(f'{self.nome} está estudando {self.curso}.')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass

    def estudar(self):
        print(f'{self.nome} está estudando {self.especialidade}.')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        pass

    def estudar(self):
        print(f'{self.nome} está estudando para exercer o cargo {self.cargo}.')




def main():
    a1 = Aluno(nome='jose', idade=27, curso='ads', turma='001')
    a1.fazer_aniversario()
    a1.estudar()
    inspect(a1, methods=True)

    p1 = Professor(nome='joao', idade=42, especialidade='História',
                nivel='Doutorado')
    p1.estudar()
    inspect(p1, methods=True)
    

    f1 = Funcionario(nome='rayane', idade=19, cargo='coodenadora', setor='EAD')
    f1.estudar()
    inspect(f1, methods=True)
    

if __name__ == '__main__':
    main()