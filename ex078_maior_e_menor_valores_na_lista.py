valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {cont}: ')))

print('=-' * 20)
print(f'\nVoce digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posicoes ', end = '')

for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end = ' ' )
        
print(f'\nO menor valor digitado foi {min(valores)} nas posicoes', end = ' ')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end = ' ')
