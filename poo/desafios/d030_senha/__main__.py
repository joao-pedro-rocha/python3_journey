from senha import Credencial


def main():
    c = Credencial()
    c.senha = str(input('Digite sua senha: '))
    print(c.senha)

if __name__ == '__main__':
    main()
