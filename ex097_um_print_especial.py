def escrever(frase):
    tam = len(frase) + 4
    print('~' * tam)
    print(f'  {frase}')
    print('~' * tam)


escrever('Olá')
