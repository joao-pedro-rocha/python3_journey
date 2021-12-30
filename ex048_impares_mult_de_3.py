soma = 0    #acumulador
cont = 0    #contador

for multiplo in range(1, 501, 2):    #contagem dos numeros de 3 em 3 ate 500
    if multiplo % 3 == 0:    #para saber se o numero é multiplo de 3
        cont = cont + 1
        soma = soma + multiplo    #soma mais o valor das iteracoes
        
print('A soma dos {} valores solicitados é: {}'.format(cont, soma))
