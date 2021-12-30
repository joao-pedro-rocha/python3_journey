palavras = ['aprender', 'programar',
            'linguagem', 'python',
            'curso', 'gratis',
            'estudar', 'praticar',
            'trabalho', 'mercado',
            'programador', 'futuro']

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end = '')
    
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')




'''palavras = ['APRENDER', 'PROGRAMAR',
            'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO']

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end = '')
    
    if 'A' in p:
        print('a', end = ' ')
    
    if 'E' in p:
        print('e', end = ' ')
        
    if 'I' in p:
        print('i', end = ' ')
        
    if 'O' in p:
        print('o', end = ' ')
        
    if 'U' in p:
        print('u', end = ' ')'''
        