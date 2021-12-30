media_idade = 0
homem_velho = 0
velho_nome = ''
mulheres_novas = 0

for pessoa in range(1, 5):
    print('------{}º pessoa------'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('''Sexo [M/F]:
'''))
    
    media_idade += idade / 4
    
    if pessoa == 1 and sexo in 'Mm':
        homem_velho = idade
        velho_nome = nome
    
    if sexo in 'Mm' and idade > homem_velho:
        homem_velho = idade
        velho_nome = nome

    if sexo in 'Ff' and idade < 20:
        mulheres_novas += 1

print('A media das idades do grupo é {}'.format(media_idade))
print('O homem mais velho tem {} anos e chama {}'.format(homem_velho, velho_nome))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(mulheres_novas))
