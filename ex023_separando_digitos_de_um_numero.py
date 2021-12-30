n = int(input('Digite um número: '))
unidade = n // 1 % 10
dezena  = n // 10 % 10
centena = n // 100 % 10
milhar  = n // 1000 % 10

print('Analisando o número...')
print('Unidade: {} \nDezena:  {} \nCentena: {} \nMilhar:  {}'.format(unidade, dezena, centena, milhar))
