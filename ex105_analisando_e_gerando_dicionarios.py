# Nao ha uma grande necessidade de 
# usar tantas variaveis para depois
# coloca-las no dicionario.

def notas(*notas, sit=False):
	"""
	-->Esta funcao recebe uma ou mais notas
	e retorna um dicionario com a quantidade
	de notas, a maior nota, a menor nota,
	a media e a situacao do aluno.
	:param notas: recebe quantas notas forem necessarias.
	:param sit: (opcional) use True para saber se a situacao e boa ou ruim. Padrao: False.
	:return: dicionario com informacoes das notas recebidas.
	"""
	
	dic_notas = {}
	
	tam = len(notas)
	media = sum(notas) / tam
	maior = max(notas)
	menor = min(notas)
	
	for nota in notas:
		dic_notas['total'] = tam
		dic_notas['média'] = media
		dic_notas['maior'] = maior
		dic_notas['menor'] = menor
	
	if media <= 6:
		situacao = 'ruim'
	
	else:
		situacao = 'boa'
	
	if sit == False:
		return dic_notas
		
	else:
		dic_notas['situacao'] = situacao
		
		return dic_notas


# Programa principal
print(notas(10, 0, 5))
help(notas)
