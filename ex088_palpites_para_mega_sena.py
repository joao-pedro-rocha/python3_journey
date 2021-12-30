from random import randint
from time import sleep

print('-'*35)
print('{:^35}'.format('MEGA SENA'))
print('-'*35)

jogo = []
n_jogo = int(input('Quantos jogos voce quer que eu sorteie? '))

print(f'\n------- SORTEANDO {n_jogo} JOGOS-------')

for j in range(1, n_jogo+1):
    sleep(1)
    
    for n in range(0, 6):
        sort = randint(1, 60)

        while sort in jogo:
            sort = randint(1, 60)

        jogo.append(sort)
        
    print(f'Jogo {j}: {jogo}')
    
    jogo.clear()
    
print('---------- BOA SORTE! ----------')
