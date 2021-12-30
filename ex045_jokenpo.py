# OBS TEM UMA FORMA MAIS FACIL DE FAZER

from random import randint
from time import sleep

cpu = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura') #LISTA COM ELEMENTOS 
pedra = 0
papel = 1
tesoura = 2

print('{:=^17}'.format('JOKENPO'))   

player = int(input('''
[0] --> Pedra
[1] --> Papel
[2] --> Tesoura

Sua jogada: '''))

print('{:->20} '.format(' '))

print ('JO')
sleep(0.5)

print('KEN')
sleep(0.5)

print('PO!')
sleep(0.3)
print('{:->20}'.format(' '))

#SE CPU JOGA PEDRA

if cpu == player:
    print('Empate!')
    
elif cpu == pedra and player == papel:
    print('Voce venceu!')

elif cpu == pedra and player == tesoura:
    print('Cpu venceu!')
    
#SE CPU JOGAR PAPEL

elif cpu == papel and player == pedra:
    print('Cpu venceu!')
    
elif cpu == papel and player == tesoura:
    print('Voce venceu!')
        
#SE CPU JOGAR TESOURA
        
elif cpu == tesoura and player == pedra:
    print('Voce venceu!')
        
elif cpu == tesoura and player == papel:
    print('Cpu venceu!')
    
print('{:*>30}'.format(' '))
    
print('CPU jogou {}.'.format(itens[cpu])) #RESGATE DO ELEMENTO DA LISTA
print('Voce jogou {}.'.format(itens[player]))

print('{:*>30}'.format(' '))
