n = int(input('digite um numero inteiro: '))

print('-' * 15)

for num in range(1, 11):
    tab = num * n
    
    print('{} x {} = {}'.format(n, num, tab))
    
print('-' * 15)
        
