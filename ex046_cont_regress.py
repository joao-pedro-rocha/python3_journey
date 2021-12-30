from time import sleep
i = str(input('''
[ s ] --> Sim
[ n ] --> Nao

Comecar contagem regressiva? '''))

print('\n')

if i == 's':
    for contagem in range(10, -1, -1):
        sleep(1)
        print(contagem)
        
    print('***' * 5)
    print('***' * 5)
    print('***' * 5)
    print('***' * 5)
    
elif i == 'n':
    print('\nContagem cancelada.')
    
else:
    print('\nERRO!')
