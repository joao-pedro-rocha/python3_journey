prod = float(input('Qual o valor do produto? '))
desc = 5 / 100 * prod

print('O produto de R${}, com o desconto de 5%, \nfica R${}'.format(prod, prod - desc))