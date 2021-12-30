print('{:=^30}'.format(' STORE '))

compra = float(input('Digite o valor da compra: R$'))

print(' ')

pagamento = int(input('''Escolha a opcao de pagamento:

[1] À VISTA NO DINHEIRO/CHEQUE
[2] À VISTA NO CARTAO
[3] 2X NO CARTAO
[4] 3X OU MAIS NO CARTAO

--> '''))

print(' ')

if pagamento == 1:
    total = compra - (compra * (10/ 100))
    
    print('Voce ganhou 10% de desconto!')
    
elif pagamento == 2:
    total = compra - (compra * (5 / 100))
    
    print('Voce ganhou 5% de desconto!')
    
elif pagamento == 3:
    total = compra
    parcela = total / 2
    
    print('Sua compra sera dividida em 2x de R${:.2f}, sem juros.'.format( parcela))
    
elif pagamento == 4:
    total = compra + (compra * 20 / 100)
    parcela = int(input('Quantas parcelas? '))
    totalparc = total / parcela
    
    print('Sua compra sera dividida em {}x de R${:.2f}, com juros.'.format(parcela, totalparc))
    
else:
    total = compra
    
    print('Opcao invalida! Tente novamente.')

print('Sua compra custara R${:.2f}.'.format(total))
