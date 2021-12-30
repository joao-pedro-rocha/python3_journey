pessoas = []
cadastro = []
maior = menor = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    
    if len(cadastro) == 0:
        maior = menor = pessoas[1]
        nome_mai = nome_men = pessoas[0]
        
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
            
        if pessoas[1] < menor:
            menor = pessoas[1]
            
    cadastro.append(pessoas[:])
    pessoas.clear()
    
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper()
        
    if resp in 'Nn':
        break

print('=-' * 25)
print(f'Ao todo você cadastrou {len(cadastro)} pessoas(s)')
print(f'O maior peso digitado foi {maior:.1f}Kg de ', end = '')
for p in cadastro:
    if p[1] == maior:
        print(f'[{p[0]}] ', end = '')
        
print(f'\nO menor peso digitado foi {menor:.1f}Kg de ', end = '')
for p in cadastro:
    if p[1] == menor:
        print(f'[{p[0]}] ', end = '')
