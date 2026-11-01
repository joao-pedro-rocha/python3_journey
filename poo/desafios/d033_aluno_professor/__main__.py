from aluno import Aluno


def main():
    a1 = Aluno('joao', 2022)
    a1.nome = 'pedro'
    # a1.nasc = 1999
    # a1.add_curso('engenharia')
    # a1.curso = 'engenharia'
    # a1.curso = 'ads'

    print(a1.__dict__)


if __name__ == '__main__':
    main()
    