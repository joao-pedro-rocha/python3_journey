matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Alimentar a matriz:
# Criar um laco for para as linhas (l) que ira repetir
# o laco for das colunas (c) 3 vezes alimentando os valores
# das colunas na respectiva linha e entao o laco for da linha
# ira se repetir 3 vezes.
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
print('-='*22)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        
    print()
    