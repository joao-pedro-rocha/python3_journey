from hashlib import sha256


class Credencial:
    def __init__(self, senha=''):
        self.__senha = senha
        
    @property
    def senha(self):
        return self.__senha
        
    @senha.setter
    def senha(self, senha):
        if len(senha) > 0:
            self.__senha = sha256(senha.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Senha inválida')
    