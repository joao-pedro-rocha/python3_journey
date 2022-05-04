def formatar_moeda(v=0):
	return f'{v:.2f}'.replace('.', ',')


def metade(v=0):
	div = v / 2
	preco_formatado = formatar_moeda(v)
	metade_moeda = formatar_moeda(div)

	return f'A metade de R$ {preco_formatado} é R$ {metade_moeda}.'


def dobro(v=0):
	dob = v * 2
	preco_formatado = formatar_moeda(v)
	dobro_moeda = formatar_moeda(dob)

	return f'O dobro de R$ {preco_formatado} é R$ {dobro_moeda}.'


def aumentar(v=0):
	porcentagem = v / 100 * 10
	adc = v + porcentagem
	adc_moeda = formatar_moeda(adc)

	return f'Aumentando 10% o valor fica R$ {adc_moeda}.'


def diminuir(v=0):
	porcentagem = v / 100 * 10
	dim = v - porcentagem
	dim_moeda = formatar_moeda(dim)

	return f'Diminuindo 10% o valor fica R$ {dim_moeda}.'
