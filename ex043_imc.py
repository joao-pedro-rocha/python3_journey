massa = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = massa / (altura ** 2)

if imc < 18.5:
    print('Magreza! Seu imc é {:.1f} Kg por metro ao quadrado. \nProcure um nutricionista para ganhar mais peso e melhorar sua saude.'.format(imc))
    
elif imc >= 18.5 and imc < 24.9:
    print('Normal! Seu imc é {:.1f} Kg por metro ao quadrado. Voce esta bem!'.format(imc))

elif imc >= 24.9 and imc < 30:
    print('Sobrepeso! Seu imc é {:.1f} Kg por metro ao quadrado. \nProcure um nutricionista para perder peso e melhorar sua saude.'.format(imc))
    
else:
    print('Obesidade! Seu imc é {:.1f} Kg por metro ao quadrado. \nProcure um nutricionista para perder peso e melhorar sua saude.'.format(imc))
