from datetime import date

cont_jovem = 0
cont_velho = 0
ano_atual = date.today().year

for c in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = ano_atual - nasc
    
    if idade < 18:
        cont_jovem += 1
        
    else:
        cont_velho += 1

print('\nAo todo temos {} maiores de idade \ne {} menores de idade.'.format(cont_velho, cont_jovem))
