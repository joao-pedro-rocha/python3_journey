from datetime import date

print('***' * 16)

nas = int(input('Digite seu ano de nascimento para \nsaber sua categoria de natacao: '))

print('***' * 16)

idade = date.today().year - nas

if idade <= 9:
    print('Com {} anos de idade voce esta na categoria Mirim.'.format(idade))
    
elif  idade <= 14:
    print('Com {} anos de idade voce esta na categoria Infantil.'.format(idade))
    
elif  idade<= 19:
    print('Com {} anos de idade voce esta na categoria Junior.'.format(idade))
    
elif idade <= 25:
    print('Com {} anos de idade voce esta na categoria Senior.'.format(idade))
    
else:
    print('Com {} anos de idade voce esta na categoria Master.'.format(idade))
