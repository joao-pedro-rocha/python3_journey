from uteis import multiplicacao_e_divisao, aumento_e_diminuicao

preco = float(input('Digite um valor: R$ '))

print(multiplicacao_e_divisao.metade(preco))
print(multiplicacao_e_divisao.dobro(preco))
print(aumento_e_diminuicao.aumentar(preco, 10))
print(aumento_e_diminuicao.diminuir(preco, 10))
print(aumento_e_diminuicao.aumentar(preco, 50))
print(aumento_e_diminuicao.diminuir(preco, 50))
