print('==' * 10)
print('CADASTRE UMA PESSOA')
print('==' * 10)

mais_dezoito = total_homens = mulheres_vinte = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    
    while sexo not in 'mf' or sexo == '':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()
    
    verificar = ' '
        
    while verificar not in 'sn' or verificar == '':
        verificar = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    
    if idade > 18:
        mais_dezoito += 1
        
    if sexo == 'm':
        total_homens += 1
        
    if sexo == 'f' and idade > 20:
        mulheres_vinte += 1
        
    if verificar == 'n':
        break
    
    print('--' * 15)

print('--' * 26)
print(f'Total de pessoas cadastradas com mais de 18 anos: {mais_dezoito}')
print(f'Total de homens cadstrados: {total_homens}')
print(f'Total de mulheres com mais de 20 anos: {mulheres_vinte}')
