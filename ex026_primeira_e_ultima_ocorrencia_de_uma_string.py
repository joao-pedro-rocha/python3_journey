frase = str(input('Digite uma frase: ')).strip().lower()

print('A frase tem {} "A" \nO primeiro aparece na posição {} \nO último aparece na posição {}'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))
