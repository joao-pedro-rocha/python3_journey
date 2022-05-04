def metade(v):
	div = v / 2

	return f'A metade de R$ {v:.2f} é R$ {div:.2f}.'


def dobro(v):
	dob = v * 2

	return f'O dobro de R$ {v:.2f} é R$ {dob:.2f}.'


def aumentar(v):
	porcentagem = v / 100 * 10
	adc = v + porcentagem

	return f'Aumentando 10% o valor fica R$ {adc:.2f}.'


def diminuir(v):
	porcentagem = v / 100 * 10
	dim = v - porcentagem

	return f'Diminuindo 10% o valor fica R$ {dim:.2f}.'
