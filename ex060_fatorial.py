#from math import factorial # funcao para fatoriais

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
#fat = factorial(n)

print('Calculando {}! = '.format(n), end = '')

while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    
    f *= c
    c -= 1
        
print(f)
