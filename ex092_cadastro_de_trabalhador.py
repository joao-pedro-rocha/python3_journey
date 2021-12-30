from datetime import datetime

trabalhador = {}
data_atual = datetime.now().year

trabalhador['nome'] = str(input('Nome: '))
trabalhador['nasc'] = int(input('Ano de nascimento: '))
trabalhador['idade'] = data_atual-trabalhador['nasc']
trabalhador['clt'] = int(input('Carteira de trabalho (0 nao tem): '))

if trabalhador['clt'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade']+(trabalhador['contratacao']+35)-data_atual

print('-='*20)

for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')
