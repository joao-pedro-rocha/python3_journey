'''from random import randint
menor = maior = 0
tupla = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]

print(f'Os valores sorteados foram: ', end = '')

for n in tupla:
    print(f'{n}', end = ' ')
    if n == tupla[0]:
        maior = tupla[0]
        menor = tupla[0]
    
    else:    
        if tupla[1] > maior:
            maior = tupla[1]
        
        if tupla[1] < menor:
            menor = tupla[1]
            
        if tupla[2] > maior:
            maior = tupla[2]
            
        if tupla[2] < menor:
            menor = tupla[2]
            
        if tupla[3] > maior:
            maior = tupla[3]
            
        if tupla[3]< menor:
            menor = tupla[3]

print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')'''

### opcao 2
from random import randint
menor = maior = 0
tupla = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]

print(f'Os valores sorteados foram: ', end = '')

for n in tupla:
    print(f'{n}', end = ' ')

print(f'\nO maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')
