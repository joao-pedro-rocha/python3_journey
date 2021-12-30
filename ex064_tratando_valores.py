n = int(input('Digite um numero (999 para parar): '))
s = c = 0

while n != 999:
    s += n
    c += 1
    n = int(input('Digite um numero (999 para parar): '))

print('\nVoce digitou {} numeros e a soma entre eles vale {}.'.format(c, s))
