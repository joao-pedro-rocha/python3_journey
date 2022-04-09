from time import sleep

c = [
	'\033[0;0m',  # 0 --> Sem cor
	'\033[1;44m', # 1 --> Azul
	'\033[1;42m', # 2 --> Verde
	'\033[1;41m'  # 3 --> Vermelho
]

def ajuda(com):
	sleep(0.5)

	cores(f'Buscando o manual da biblioteca ou função {com}', 1)

	sleep(1)

	help(com)


def cores(msg, cor=0):
	tam = len(msg)

	print(c[cor])
	print('=' * tam)
	print(f'{msg}')
	print('=' * tam)
	print(c[0])


# Programa principal
cores('Bem-vindo(a) à ajuda intertiva!', 2)

while True:
	comando = str(input('Digite uma biblioteca ou função: '))
	
	if comando.upper() == 'SAIR':
		sleep(0.5)

		cores('GOOD BYE', 3)
		sleep(0.5)
		break
		
	else:
		ajuda(comando)
