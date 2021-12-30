soma = 0
cont = 0
for c in range(1, 7):    #conta quantas vezes o usuario dara input
    n = int(input('Digite o {}º numero: '.format(c)))
    
    if n % 2 == 0:   #encontra os pares
        soma += n    #soma cada numero par
        
        cont += 1    #conta quantos pares tem

print('{} sao pares e a soma entre eles é {}.'.format(cont, soma))
