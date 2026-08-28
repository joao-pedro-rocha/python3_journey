import diario


def main():
    d = diario.Diario()
    d.escrever('teste')
    d.escrever('deu certo')
    try:
        d.ler('123')
    except Exception as e:
        print(e)
    
main()