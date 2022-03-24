def leiaInt(msg):
	ok = False
	
	while True:
		n = str(input(msg))
		
		if n.isnumeric():
			n = int(n)
			ok = True
			
			break
			
		else:
			print('ERRO! Digite um número inteiro válido.')
			
	return n
	
	
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')






















