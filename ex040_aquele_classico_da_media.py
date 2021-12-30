nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('Sua media é {:.2f}.'.format(media))

if 7 > media >= 5:
    print('Voce esta em recuperacao.')
    
elif media < 5:
        print('Voce esta reprovado.')
    
else:
    print('Voce esta aprovado!')
    
print('Tenha um bom dia!')
