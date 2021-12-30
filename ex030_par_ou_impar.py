n = int(input('Digite um numero inteiro: '))
n2 = n % 2

if n2 == 0:
    print('Voce digitou {}; {} é um numero par.'.format(n, n))
else:
    print('Voce digitou {}; {} é um numero impar.'.format(n, n))
