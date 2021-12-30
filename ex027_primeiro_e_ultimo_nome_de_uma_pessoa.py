nome = str(input('Digite seu nome completo: ')).strip().lower()
nome2 = nome.split()

print('Prazer em te conhecer! \nSeu primeiro nome é {} \nE seu último nome é {}'.format(nome2[0], nome2[-1]))
