salario = float(input('Quanto é o seu salario? '))

if salario <= 1250:
    print('Quem recebe R${:.2f} recebera, agora, R${:.2f}.'.format(salario, (salario * 15 / 100) + salario))

else:
    print('Quem recebe R${:.2f} recebera, agora, R${:.2f}.'.format(salario, salario * (10 / 100) + salario))

print('Tenha um bom dia!!')
