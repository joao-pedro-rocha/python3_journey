s = c = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    
    if n == 999:
        break
    
    s += n
    c += 1
    
print(f'A soma dos {c} valores vale {s}')
