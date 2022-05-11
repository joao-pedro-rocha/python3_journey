def formatar_moeda(v=0):
	'''
	-> Realiza a formatação do valor para o formato do real brasileiro.
	:param v: valor que será formatado.
	:return: retorna um valor com a formatação correta do real brasileiro.
	'''

	return f'{v:.2f}'.replace('.', ',')
