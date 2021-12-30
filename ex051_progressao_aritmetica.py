ptermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = ptermo + 10 * razao    # o 10 equivale a quantidade de termos desejados

for c in range(ptermo, decimo, razao):   
    print(c, end = ' ➡ ')
    
print('ACABOU')    # cuidado para nao colocar alguns prints e etc. na identacao errada
    