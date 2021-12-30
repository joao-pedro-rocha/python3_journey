n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

print('Os valores digitados foram, respectivamente, {} e {}.'.format(n1, n2))

if n1 > n2:
    print('O primeiro valor é maior.')

elif n2 > n1:
    print('O segundo valor é maior.')

else:
    print('Os valores digitados sao iguais.')
