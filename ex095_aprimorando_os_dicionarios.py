jogador = {}
n_gols = []
time = []
soma = 0

while True:
	jogador.clear()
	jogador['nome'] = str(input('Nome do jogador: '))
	jogador['n_partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
	
	for partida in range(jogador['n_partidas']):
		n_gols.append(int(input(f'Quantos gols na partida {partida+1}? ')))
		
	jogador['n_gols'] = n_gols[:]
	jogador['s_gols'] = sum(n_gols)
		
	time.append(jogador.copy())
	n_gols.clear()
		
	sair = str(input('Quer continuar? [S/N] ')).upper()
		
	while sair not in 'SN':
		sair = str(input('Quer continuar? [S/N] ')).upper()
		
	if sair in 'N': # Resposta para "continuar?" (s/n)
		break
		
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
	print(f'{i:<15}', end='')

print()
print('--'*30)
	
for k, v in enumerate(time):
	print(f'{k:>3} ', end='')
	
	for d in v.values():
		print(f'{str(d):<15}', end='')
	
	print()

while True:
	dados = int(input('Quer mostrar dados de qual jogador? (999 para parar) '))

	if dados == 999:
		break
		
	if dados >= len(time):
		print(f'Não existe jogador com código {dados}!')
		
	else:
		print()
		print(f'          ---DADOS DO JOGADOR {time[dados]["nome"]}---')
		print()
		
		for i, g in enumerate(time[dados]['n_gols']):
			print(f'No jogo {i+1} fez {g} gols.')
			
	print('--'*30)
print()
print('Goodbye!')		
