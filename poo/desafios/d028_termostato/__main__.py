from termostato import Termostato


def main():
    t = Termostato()
    print(t.temperatura)
    try:
        t.temperatura = 31.3
        print(t.temperatura)
    except ValueError:
        print('Temperatura inválida!')

if __name__ == '__main__':
    main()
