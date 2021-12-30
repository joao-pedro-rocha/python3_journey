nome = input('Digite seu nome: ')
nome_c = nome.title()
maiusculo = nome.upper()
minusculo = nome.lower()

novo_nome = nome.split()
nome_junto = ''.join(novo_nome)

tamanho = len(nome_junto)
p_nome = novo_nome[0]
p_tamanho = len(p_nome)

print('Seu nome é {}. \nSeu nome em maiúsculo é: \n{}. \nSeu nome em minúsculo é: \n{}. \nSeu nome tem {} letras. \nSeu primeiro nome é {} e ele tem {} \nletras.'.format(nome_c, maiusculo, minusculo, tamanho, p_nome, p_tamanho))
