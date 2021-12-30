t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
c = 0
n_termos = 0

while c < 10:
    print('{} >>'.format(t), end = ' ')
    
    c += 1
    t += r
    n_termos += 1
    
    if c == 10:
        print('pausa')
        
        mais_termos = int(input('Quantos termos voce quer a mais? '))
        c = 10 - mais_termos

        if mais_termos == 0:
            print('Ao todo foram mostrados {} termos na tela'.format(n_termos))
                      
print('Fim')
