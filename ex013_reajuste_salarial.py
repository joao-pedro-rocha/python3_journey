sal = float(input('Qual é o salário do funcionário? '))
aum = sal + (15 / 100 * sal)

print('O novo salário com 15% de aumento é R${:.2f}.'.format(aum))