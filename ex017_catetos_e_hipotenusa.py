from math import hypot

ca = float(input('Cateto adjacente: '))
co = float(input('Cateto oposto: '))

print('A hipotenusa de {} e {} é {:.2f}.'.format(ca, co, hypot(ca, co)))
