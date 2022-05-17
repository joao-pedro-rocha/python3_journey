def leia_int(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('erro')

            continue

        else:
            return n


def leia_real(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('erro')

            continue

        else:
            return n


# Programa principal
n1 = leia_int('Digite um número inteiro: ')
n2 = leia_real('Digite um número real: ')

print(f'O número inteiro digitado foi {n1}.')
print(f'O número real digitado foi {n2:.1f}')
