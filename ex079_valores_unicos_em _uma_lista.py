lista = []

while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in lista:
        lista.append(valor)
        print('Adicionado com sucesso...')
        
    else:
        print(f'O valor {valor} ja foi adicionado anteriormente. Tente outro valor.')

    confirmacao = ' '
    
    while confirmacao not in 'SsNn':
        confirmacao = str(input('Deseja continuar? [S/N] '))
        
    if confirmacao in 'Nn':
        break

lista.sort()
print(f'Os valores digitados foram {lista}.')
