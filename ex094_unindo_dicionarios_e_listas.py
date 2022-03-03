pessoa = {}
lista_pessoas = []
soma = media = 0

while True:
	pessoa['nome'] = str(input('Nome: '))
	pessoa['idade'] = int(input('Idade: '))
	pessoa['sexo'] = str(input('Sexo: [M | F] - '))
	
	while pessoa['sexo'] not in 'MmFf':
		pessoa['sexo'] = str(input('Sexo: [M | F] - '))
		
	lista_pessoas.append(pessoa.copy())
	soma += pessoa['idade']
	pessoa.clear()
		
	resp = str(input('Que continuar? [S | N] - '))
	
	while resp not in 'SsNn':
		resp = str(input('Que continuar? [S | N] - '))
		
	if resp in 'Nn':
		break

media = soma / len(lista_pessoas)

print(f'Ao todo temos {len(lista_pessoas)} pessoa(s) cadastrada(s).')

print(f'A média de idade é {media:.2f} anos.')

print(f'As mulheres cadastradas foram: ', end='')
for p in lista_pessoas:
	if p['sexo'] in 'Ff':
		print(f'- {p["nome"]} ', end='')
print('.')

print(f'Pessoas com idade acima da média: ',end='')
for p in lista_pessoas:
	if p['idade'] > media:
		print(f'- {p["nome"]} ({p["idade"]} anos) ', end='')
print('.')
