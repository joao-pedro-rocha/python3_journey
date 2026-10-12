import banco_senha


def main():
    cc = banco_senha.ContaBancaria(000, 'João', 100, '123456')
    # cc.depositar(1000)
    cc.sacar(50)
    # print(cc)
    # print(cc.__dict__)

if __name__ == '__main__':
    main()
