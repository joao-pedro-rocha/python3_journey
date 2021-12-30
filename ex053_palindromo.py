import unidecode
from time import sleep

texto = str(input('Digite uma palavra ou uma frase: ').lower().replace(' ', ''))
texto_final = unidecode.unidecode(texto)
txt_inverso = ''

for letra in range(len(texto_final)- 1, -1, -1):
    txt_inverso += texto_final[letra]

print('O inverso de {} é {}.'.format(texto_final, txt_inverso))
print('Portanto', end = '')

for pontinhos in range(1, 4):
    print('.', end = '')
    sleep(0.8)

if texto_final == txt_inverso:
    print('\nÉ UM PALINDROMO.')
    
else:
    print('\nNAO É UM PALIDROMO.')
