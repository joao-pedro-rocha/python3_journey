from encapsulamento_p2 import Avaliacao

from rich import inspect
from rich import print as rprint


def main():
    av1 = Avaliacao('Joao', 'Matemática')
    inspect(av1, methods=True, private=True)
    av1.nota = 10
    print(f'O aluno {av1.nome} tirou {av1.nota} na disciplina {av1.disciplina}.')


if __name__ == '__main__':
    main()
