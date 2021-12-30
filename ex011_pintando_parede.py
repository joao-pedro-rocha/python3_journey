altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura

print('Você precisará de {}L de tinta para pintar a parede. '.format(area / 2))