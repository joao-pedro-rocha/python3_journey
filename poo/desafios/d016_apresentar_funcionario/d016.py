# crie uma classe Funcionario(), onde podemos cadastrar nome, setor e cargo.
# crie tambem um metodo que permita ao funcionario se apresentar.
from rich import print, inspect

class Funcionario:
    """
    Cria um funcionario e permite que ele se apresente
    """
    empresa = 'Curso em vídeo' # um atributo fora do construtor define um valor
                               # que sera comum para todas a todos os objetos

    def __init__(self, nome, setor, cargo):
        self.nome = nome    # atributos de instancia definem dados que
                            # pertencerao particularmente a cada objeto
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self) -> str:
        return f':handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} na empresa {Funcionario.empresa}.'


f1 = Funcionario('João', 'TI','Programador')
print(f1.apresentacao())

inspect(f1, methods=True)
