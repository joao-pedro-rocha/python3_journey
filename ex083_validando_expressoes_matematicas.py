expressao = str(input('Digite uma expressao: '))
pilha = []

for simb in expressao: # para cada caractere da string
    if simb == '(': # verifica-se se há algum parentese abrindo e adiciona um parentese na lista PILHA
        pilha.append('(')
        
    elif simb == ')':       # se houver um parentese de fechamento
        if len(pilha) > 0: # verifica-se se existe algun item na lista PILHA
            pilha.pop()     # caso haja parentese de fechamento, retira-se o item da lista PILHA 
            
        else:
            pilha.append(')') # caso falte fechar algum parentese, adiciona-se um parentese de fechamento na lista PILHA
            break
        
# cada parentese aberto aidciona um item na lista PILHA
# de forma q se você fechar todos os parenteses a lista PILHA fica vazia
# caso a lista PILHA esteja vazia o programa aceita sua expressão numérica
if len(pilha) == 0: 
    print('Sua exressão está válida!')
    
else:
    print('Sua expressão está inválida!')
