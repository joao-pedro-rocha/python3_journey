# --------------------
# |Funcionario abs   |
# --------------------
# |nome              |
# |sal_bruto         |
# |salario           |
# |sal_min = 1612    |
# |inss = 7.5        |
# --------------------
# |calc_sal() abs    |
# |analisar_sal()    |
# --------------------


# ----------------
# |Horista       |
# ----------------
# |valor_hora    |
# |horas_trab    |
# ----------------
# |calc_sal()    |
# ----------------


# ----------------
# |Mensalista    |
# ----------------
# ----------------
# |calc_sal()    |
# ----------------




from rich import print as rprint
from rich.panel import Panel
from abc import ABC, abstractmethod


class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome='', sal_bruto=0, salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario

    @abstractmethod
    def calc_sal():
        pass

    def analisar_sal(self):
        txt = f'O salário de {self.nome} ({self.__class__.__name__}) é de '
        txt += f'R${self.salario} e corresponde a '
        txt += f'{self.salario / Funcionario.sal_min:.1f} salário(s) mínimo(s).'
        panel = Panel(txt, title='Análise de salário')

        return panel


class Horista(Funcionario):
    def __init__(self, nome, val_hr=7.37, hrs_trab=220):
        super().__init__(nome)
        self.val_hr = val_hr
        self.hrs_trab = hrs_trab
        self.sal_bruto = self.val_hr * self.hrs_trab 

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto=Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)


def main():
    f1 = Horista(nome='joao', val_hr=12, hrs_trab=190)
    f1.calc_sal()
    rprint(f1.analisar_sal())

    f2 = Mensalista(nome='pedro', sal_bruto=8500)
    f2.calc_sal()
    rprint(f2.analisar_sal())


main()
