from uteis import formatacao_de_moeda

def metade(v=0):
	'''
	-> Calcula a metade de um valor x.
	:param v: valor do qual será calculada a metade.
	:return: retorna a metade de um valor x.
	'''

	preco_metade = v / 2
	preco_formatado = formatacao_de_moeda.formatar_moeda(v)
	metade_formatada = formatacao_de_moeda.formatar_moeda(preco_metade)

	return f'A metade de R$ {preco_formatado} é R$ {metade_formatada}.'


def dobro(v=0):
	'''
	-> Calcula o dobro de um valor x.
	:param v: valor do qual será calculada o dobro.
	:return: retorna o dobro de um valor x.
	'''

	preco_dobro = v * 2
	preco_formatado = formatacao_de_moeda.formatar_moeda(v)
	dobro_formatado = formatacao_de_moeda.formatar_moeda(preco_dobro)

	return f'O dobro de R$ {preco_formatado} é R$ {dobro_formatado}.'
