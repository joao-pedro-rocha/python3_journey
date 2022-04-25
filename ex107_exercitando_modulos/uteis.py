def metade(v):
	div = v / 2

	return f'A metade de R$ {v:.2f} é R$ {div:.2f}.'


def dobro(v):
	dob = v * 2

	return f'O dobro de R$ {v:.2f} é R$ {dob:.2f}.'


def porcentagem(v):
	pc = v / 100 * 10
	adc = v + pc

	return f'Aumentando 10% o valor fica R$ {adc:.2f}.'
