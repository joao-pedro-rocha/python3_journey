dicionario = {}

dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f"Média de {dicionario['nome']}: "))

if dicionario['media'] == 0:
	dicionario['situacao'] = 'Reprovado'

elif dicionario['media'] >= 1 and dicionario['media'] <= 4:
	dicionario['situacao'] = 'Reprovado'
	
elif dicionario['media'] >= 5 and dicionario['media'] <= 6:
	dicionario['situacao'] = 'Recuperação'
	
else:
	dicionario['situacao'] = 'Aprovado'

print(f"Nome: {dicionario['nome']}")
print(f"Média: {dicionario['media']:.2f}")
print(f"Situação: {dicionario['situacao']}")
