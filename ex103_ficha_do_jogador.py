def ficha(jogador='<desconhecido>', gol=0):
	print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


# Programa principal
nome = str(input('Nome do jogador: '))
n_gol = str(input('Número de gols: '))

if n_gol.isnumeric():
	n_gol = int(n_gol)
	
else:
	n_gol = 0
	
if nome.strip() == '':
	ficha(gol=n_gol)
	
else:
	ficha(nome, n_gol)
