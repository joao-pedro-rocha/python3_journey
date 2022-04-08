from time import sleep

def ajuda(com):
	help(com)


# Programa principal
while True:
	print('\033[1;42mBem-vindo(a) à ajuda intertiva!')

	comando = str(input('\033[0;0mDigite uma biblioteca ou comando: '))
	
	if comando.upper() == 'SAIR':
		break
		
	else:
		sleep(0.5)

		print(f'\033[1;44mBuscando as informações da biblioteca/comando {comando}\033[0;0m')
		
		sleep(1)

		ajuda(comando)
