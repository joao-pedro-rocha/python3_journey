def area():
    print('-----Controle de terrenos-----')
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    a = l * c

    print(f'A área de um terreno {l:.1f}x{c:.1f} é igual a {a:.1f} metros quadrados.')


area()
