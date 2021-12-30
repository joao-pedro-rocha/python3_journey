from math import sin, cos, tan, radians

a = int(input('Digite o ângulo: '))
sen = sin(radians(a))
co = cos(radians(a))
tang = tan(radians(a))

print('O seno de {} é: {:.2f} \nO cosseno é: {:.2f} \nE a tangente é: {:.2f}'.format(a, sen, co, tang))
