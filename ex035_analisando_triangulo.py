print('ANALISADOR DE TRIANGULOS')

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if b + c > a and a + c > b and a + b > c:
    print('Os segmentos digitados PODEM formar um triangulo.')

else:
    print('Os segmentos digitados NAO PODEM formar um triangulo.')
