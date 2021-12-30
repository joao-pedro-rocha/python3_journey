n = int(input('Digite um numero: '))
div = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;92m', end = ' ')

        div += 1

    else:
        print('\033[1;91m', end = ' ')
        
    print('{}'.format(c), end = ' ')

print('\n\033[mO numero {} foi divisivel {} vezes.'.format(n, div ))

if div == 2:
    print('Portanto ele É PRIMO!')
    
else:
    print('Portanto ele NAO É PRIMO')
    