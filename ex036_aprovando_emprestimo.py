print('#' * 30)
print('Financiamento de imoveis!!!')
print('#' * 30)

casa = float(input('Qual o valor da casa que voce quer comprar? R$')) #VALOR DA CASA
salario = float (input('Quanto é o seu salario? R$')) #VALOR DO SALARIO
tempo = float(input('Em quantos anos voce quer pagar? ')) #TEMPO PARA PAGAR
parcela = casa / (tempo * 12) #VALOR DA PARCELA
limitador = salario * (30/100) #30% DO SALARIO

if parcela > limitador:
    print('#' * 30)
    print('Negociacao cancelada! O valor da parcela seria de R${:.2f}, porem nao podemos perimitir \nque o valor das parcelas seja superior a R${:.2f}. \nPor favor, tente outra hora.'.format(parcela, limitador))

else:
    print('#' * 30)
    print('Negocio fechado! Parabens!!! O valor das suas parcelas sera de \nR${:.2f} mensais, que devem ser completamente pagas em {:.0f} anos.'.format(parcela, tempo))

print('Tenha um bom dia!')
