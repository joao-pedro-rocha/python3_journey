ficha = []

nome = str(input('Nome: '))
nota1 = float(input('Nota 1: '))
nota2 = float(input('nota 2: '))
media = (nota1 + nota2) / 2
	
ficha.append([nome, [nota1, nota2], media])
	
print(ficha)

