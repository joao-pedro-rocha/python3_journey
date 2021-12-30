jogador = {}
n_gols = []

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for partida in range(0, jogador['partidas']):
    n_gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {partida+1}? ')))

jogador['gols'] = n_gols
jogador['total'] = sum(n_gols)

print('-='*40)

print(jogador)

print('=-'*40)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('=-'*40)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for partida, gols in enumerate(n_gols):
    print(f'Na partida {partida+1}, fez {gols} gols.')
