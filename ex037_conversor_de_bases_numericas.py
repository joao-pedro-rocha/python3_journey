print('*' * 30)
print('Conversor de Bases Numericas!')
print('*' * 30)

n = int(input('Digite um numero inteiro: '))

print('=' * 30)

base = int(input('''1 - Binaria
2 - Octal
3 - Hexadecimal
Escolha UMA das bases numericas: '''))

print('=' * 39)

if base == 1:
    print('{} na base BINARIA é igual a {}.'.format(n, bin(n)[2:]))
    
elif base == 2:
    print('{} na base OCTAL é igual a {}'.format(n, oct(n)[2:]))
    
else:
    print('{} na base HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))

print('=' * 39)
print('Obrigado pela preferencia!')
