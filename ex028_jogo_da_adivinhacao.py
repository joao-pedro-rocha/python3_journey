from random import randint

jogador = int(input(('Vou pensar em um numero de 0 a 5. Adivinha aí! ')))

jota = randint(0,5)

if jota != jogador:
	print('Eu pensei no numero {}, nao no numero {}. Você errou!!!'.format(jota, jogador))
else:
	print('Eu pensei no numero {}, e você também. Você acertou!!'.format(jota))
