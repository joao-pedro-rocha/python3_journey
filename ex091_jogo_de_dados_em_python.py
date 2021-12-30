from random import randint
from operator import itemgetter

dicionario = {
	'jogador1': randint(1, 6),
	'jogador2': randint(1, 6),
	'jogador3': randint(1, 6),
	'jogador4': randint(1, 6)
}

ranking = ()

for j, n in dicionario.items():
	print(f'{j} tirou {n} no dado.')
	
print('-'*30)

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)

for p, v in enumerate(ranking):
	print(f'{p+1}° lugar: {v[0]} com {v[1]}')
	print(p, v)