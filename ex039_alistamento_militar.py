from datetime import date

nas = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nas

if idade < 18:
    print('Seu alistamento sera em {}.'.format(nas + 18))

elif idade ==  18:
    print('Seu alistamento é em {}. ALISTE-SE IMEDIATAMENTE!'.format(ano))

else:
    print('Seu alistamento foi em {}.'.format(ano - (idade - 18)))

print('Tenha um bom dia!')
