class Diario:
    def __init__(self, senha='123'):
        self.__segredos = []
        self. __senha = senha
    
    @property
    def segredos(self):
        return self.__segredos
        
    @segredos.setter
    def segredos(self, segredo):
        if isinstace(segredo, str) and len(segredo) > 0:
            self.__segredos.append(segredo.strip())

    @property
    def senha(self):
        raise PermissionError('Ninguém pode ver a senha!')
    
    def escrever(self, segredo):
        self.segredos.append(segredo)
    
    def ler(self, senha):
        if senha == self.__senha:
            for s in self.segredos:
                print(f'- {s}')
        else:
            raise PermissionError('Senha incorreta!')
        
    
    

    