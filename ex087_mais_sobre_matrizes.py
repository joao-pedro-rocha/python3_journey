matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sompar = somimp = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    
print('-='*22)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
        
        if matriz[l][c] % 2 == 0:
            sompar += matriz[l][c]
            
        else:
            somimp += matriz[l][c]
            
    print()

print('-='*22)

print(f'A soma dos valores pares é {sompar}.')
print(f'A soma dos valores impares é {somimp}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
