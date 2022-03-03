from time import sleep

def contador(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(c, end=' ')
    sleep(0.5)


def contador_personalizado():
    print('Agora é a sua vez de personalizar o contador.')
    
    inicio = int(input('Defina o início: '))
    fim = int(input('Defina o fim: '))
    passo =int(input('Defina o passo: '))

    for c in range(inicio, fim, passo):
        print(c, end=' ')


# Porgrama principal
contador(1, 11, 1)
print()
contador(10, -1, -2)
print()
contador_personalizado()
