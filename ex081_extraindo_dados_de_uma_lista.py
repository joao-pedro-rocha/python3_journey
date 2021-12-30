lista = []
c = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    c += 1
    r = ' '
    
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip()
        
    if r in 'Nn':
        break
    
lista.sort(reverse = True)
print('-=' * 40)
print(f'Voce digitou {c} elementos.')
print(f'Os valores em ordem decrescente sao {lista}.')

if 5 in lista:
    print('O valor 5 esta na lista.')
    
else:
    print('O valor 5 nao foi encontrado na lista.')
