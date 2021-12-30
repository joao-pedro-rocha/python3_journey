print('Gerador de P.A.')
print('-=' * 13)

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
c = 0

while c != 10:
    print('{} >>'.format(t), end = ' ')
    t += r
    c += 1

print('Fim')
