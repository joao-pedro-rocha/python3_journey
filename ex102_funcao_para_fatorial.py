def fatorial(n, show=False):
	"""
	->Calcula o fatorial de um numero.
	:param n: numero a ser calculado.
	:param show: (opcional) mostrar ou nao a conta.
	:return: o valor do fatorial de um numero n.
	"""
	
	f = 1
	for c in range(n ,0, -1):
		if show:
			print(c, end='')
			
			if c > 1:
				print(' x ', end='')
				
			else:
				print(' = ', end='')
				
		f *= c
		
	return f
	
	
# Programa principal
print(fatorial(5, show=True))
print(fatorial(5))
# help(fatorial)
