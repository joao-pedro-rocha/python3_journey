n = (int(input('Digite um numero: ')),
     (int(input('Digite outro numero: '))),
     (int(input('Digite outro numero:'))),
     (int(input('Digite outro numero: '))))

print(f'\nVoce digitou os valores {n}')

if 3 in n:
    print(f'O valor 3 aparece na posicao {n.index(3)+1}')

else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
    
print(f'O valores pares digitados foram: ', end = '')
for p in n:
    if p % 2 == 0:
        print(p, end = ' ')
        
print(f'\nO numero 9 aparece {n.count(9)} vezes')
