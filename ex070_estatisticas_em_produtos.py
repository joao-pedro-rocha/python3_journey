s = prod_1000 = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preco: R$'))
    cont += 1
    s += preco
    
    if preco > 1000:
        prod_1000 += 1
        
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    continuar = ' '
    
    while continuar not in 'sn' or continuar == '':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        
    if continuar == 'n':
        break

print(f'O total da compra foi R${s:.2f}')
print(f'{prod_1000} produtos custaram mais de R$1000.00')
print(f'O prduto mais barato foi {barato} que custa R$ {menor:.2f}')
