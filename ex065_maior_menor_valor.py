p = 'S'
c = m = s = maior = menor = 0

while p in 'Ss':
    n = int(input('Digite um numero: '))
    p = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    c += 1
    s += n
    
    if c == 1:
        maior = menor = n
        
    else:
        if n > maior:
            maior = n
            
        if n < menor:
            menor = n
            
m = s / c

print('\nVoce digitou {} valores'.format(c))
print('A media dos valores digitados é {}'.format(m))
print('O maior numero foi {} e o menor numero foi {}'.format(maior, menor))
