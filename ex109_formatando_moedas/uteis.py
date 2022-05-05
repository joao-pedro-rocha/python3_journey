def formatar_moeda(v=0):
	return f'{v:.2f}'.replace('.', ',')


def metade(v=0):
	preco_metade = v / 2
	preco_formatado = formatar_moeda(v)
	metade_formatada = formatar_moeda(preco_metade)

	return f'A metade de R$ {preco_formatado} é R$ {metade_formatada}.'


def dobro(v=0):
	preco_dobro = v * 2
	preco_formatado = formatar_moeda(v)
	dobro_formatado = formatar_moeda(preco_dobro)

	return f'O dobro de R$ {preco_formatado} é R$ {dobro_formatado}.'


def aumentar(v=0, percentual=0):
	porcentagem = v / 100 * percentual
	preco_aumentado = v + porcentagem
	aumento_formatado = formatar_moeda(preco_aumentado)

	return f'Aumentando {percentual}% o valor fica R$ {aumento_formatado}.'


def diminuir(v=0, percentual=0):
	porcentagem = v / 100 * percentual
	preco_diminuido = v - porcentagem
	diminuicao_formatada = formatar_moeda(preco_diminuido)

	return f'Diminuindo {percentual}% o valor fica R$ {diminuicao_formatada}.'
