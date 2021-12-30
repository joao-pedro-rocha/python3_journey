from random import randint
bot = randint(0, 10)
n = int(input('Escolhi um numero de 0 a 10. Tente adivinhar qual é. '))
tent = 1

while n != bot:
    tent += 1
    
    if n < bot:
        print('\n***Mais***')
        
    if n > bot:
        print('\n***Menos***')
        
    n = int(input('Tente novamente. Digite um numero de 0 a 10: '))

print('\nO numero escolhido foi {}.'.format(bot))
print('Voce acertou na {}º tentativa.'.format(tent))
