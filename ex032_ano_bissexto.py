from calendar import isleap

ano = int(input('Saiba quais anos sao/foram bissextos.\nDigite um ano para analisar: '))

if isleap(ano) == True:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} nao é bissexto.'.format(ano))
