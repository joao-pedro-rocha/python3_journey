print('#' * 23)

print('ANALISADOR DE TRIANGULOS')

print('#' * 23)

a = int(input('Digite o primeiro segmento: '))
b = int(input('Digite o segundo segento: '))
c = int(input('Digite o terceiro segmento: '))

if a + b > c and b + c > a and c + a > b:
    if a == b  == c:
        print('Os segmentos podem FORMAR um triangulo EQUILATERO.')
        
    elif a != b != c != a:
        print('Os segmentos podem FORMAR um triangulo ESCALENO.')
        
    else:
        print('Os segmentos podem FORMAR um triangulo ISOCELES.')
        
else:
    print('Os segmentos NAO PODEM FORMAR um triangulo.')
