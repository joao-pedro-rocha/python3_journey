print('==' * 20)
print('{:^40}'.format('BANCO PELADO'))
print('==' * 20)

saque = float(input('Quanto voce deseja sacar? R$'))
total = saque
nota = 50
total_notas = 0
    
while True:
    if total >= nota:
        total -= nota
        total_notas += 1
         
    else:
        if total_notas > 0:
            print(f'{total_notas} notas de R${nota}')
        
        if nota == 50:
            nota = 20
        
        elif nota == 20:
            nota = 10
            
        elif nota == 20:
            nota = 10
            
        elif nota == 10:
            nota = 1
        
        total_notas = 0
            
        if total == 0:
            break
