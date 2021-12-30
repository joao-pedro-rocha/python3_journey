n = ('zero', 'um', 'dois', 'tres', 'quatro',
     'cinco', 'seis', 'sete', 'oito',
     'nove', 'dez','onze', 'doze',
     'treze','catorze', 'quinze','dezesseis',
     'dezesste','dezoito', 'dezenove', 'vinte')

while True:
    valor = int(input('Escolha um numero de 0 a 20 (999 para parar): '))
    
    if valor == 999:
        break
    
    if 0 <= valor <= 20:
        print(f'Voce escolheu o numero {n[valor]}')
    
    else:
        print('Tente novamente.', end = ' ')
      