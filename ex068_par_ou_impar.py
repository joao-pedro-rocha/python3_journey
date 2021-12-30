from random import randint

v = 0

print('===' * 10)
print('VAMOS JOGAR PAR OU IMPAR')
print('===' * 10)

while True:    
    jogador = int(input('Digite um valor: '))
    impar_par = str(input('Impar ou par [I/P]: ')).strip().lower()
    cpu = randint(0, 10)
    s = jogador + cpu
    
    while impar_par not in 'ip':
        impar_par = str(input('Impar ou par [I/P]: ')).strip().lower()
    
    print('---' * 25)
    
    if impar_par == 'p' and s % 2 == 0:
        print(f'Voce jogou {jogador} e o computador jogou {cpu}. Total de {s}. JOGADOR VENCEU!')
        print('Vamos jogar novamente...')
        
        v += 1
        
    elif impar_par == 'i' and s % 2 == 1:
        print(f'Voce jogou {jogador} e o computador jogou {cpu}. Total de {s}. JOGADOR VENCEU!')
        print('Vamos jogar novamente...')
        
        v += 1
      
    else:
        print(f'Voce jogou {jogador} e o computador jogou {cpu}. Total de {s}. COMPUTADOR VENCEU!')
        break

print('---' * 25)
print(f'GAME OVER! Voce venceu {v} vezes.')
