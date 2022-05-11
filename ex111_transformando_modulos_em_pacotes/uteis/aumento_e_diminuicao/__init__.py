from uteis import formatacao_de_moeda

def aumentar(v=0, percentual=0):
	'''
	-> Aumenta x porcento de um valor y.
	:param v: opcional. Valor do qual será calculado o percentual.
	:param percentual: opcional. Determina a porcentagem que será calculada do valor x para fazer a
					   adição.
	:return: retorna um valor x aumentado em y porcento.
	'''

	porcentagem = v / 100 * percentual
	preco_aumentado = v + porcentagem
	aumento_formatado = formatacao_de_moeda.formatar_moeda(preco_aumentado)

	return f'Aumentando {percentual}% o valor fica R$ {aumento_formatado}.'


def diminuir(v=0, percentual=0):
	'''
	-> Diminui x porcento de um valor y.
	:param v: opcional. Valor do qual será calculado o percentual.
	:param percentual: opcional. Determina a porcentagem que será calculada do valor x para fazer a
					   subtração.
	:return: retorna um valor x diminuído em y porcento.
	'''

	porcentagem = v / 100 * percentual
	preco_diminuido = v - porcentagem
	diminuicao_formatada = formatacao_de_moeda.formatar_moeda(preco_diminuido)

	return f'Diminuindo {percentual}% o valor fica R$ {diminuicao_formatada}.'
