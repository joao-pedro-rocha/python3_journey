from rich import print as rprint, inspect
from classes import Aluno, Professor, Funcionario


def main():
    a1 = Aluno(nome='jose', idade=27, curso='ads', turma='001')
    a1.fazer_aniversario()
    inspect(a1, methods=True)

    p1 = Professor(nome='joao', idade=42, especialidade='História',
                nivel='Doutorado')
    inspect(p1, methods=True)

    f1 = Funcionario(nome='rayane', idade=19, cargo='coodenadora', setor='EAD')
    inspect(f1, methods=True)


if __name__ == '__main__':
    main()
