from random import randint
from time import sleep

numeros = []
pares = []

def sortear():
	print('Sorteando valores...', end=' ')
	for numero in range(0, 5):
		sleep(0.5)
		numero = randint(0, 10)
		print(numero, flush=True, end=' ')
		numeros.append(numero)
	sleep(0.5)
	print('PRONTO!')
		
		
def somar_pares():
	for valor in numeros:
		if valor % 2 == 0:
			pares.append(valor)
			
	print(f'\nOs valores pares sao {pares}.')
	print(f'A soma dos valores pares é igual a {sum(pares)}.')


# Programa principal
sortear()

somar_pares()
