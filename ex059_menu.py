from time import sleep

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))

opc = 0

while opc != 5:     
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa''')

    opc = int(input('>>>Escolha uma opcao: '))
    
    if opc == 1:
        print('A soma entre {} e {} é {}.'.format(v1, v2, v1 + v2))
        
    elif opc == 2:
        print('A multiplicacao entre {} e {} é {}.'.format(v1, v2, v1 * v2))
        
    elif opc == 3:
        if v1 > v2:
            print('O maior valor é {}.'.format(v1))
            
        else:
            print('O maior valor é {}.'.format(v2))
            
    elif opc == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    
    elif opc == 5:
        print('Finalizando...')
    
    else:
        print('Opcao invalida!')
    
    sleep(1)
    print('=-=' * 11)

print('Fim do programa')
