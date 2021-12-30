s = str(input('Informe seu sexo [M/F]:')).upper().strip()[0]

while s not in 'MmFf':
    print('Opcao invalida!')
    s = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
    
print('Sexo {} registrado com sucesso!'.format(s))
