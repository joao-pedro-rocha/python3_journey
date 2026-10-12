from hashlib import sha256


class ContaBancaria:
    def __init__(self, id:int, nome:str, saldo:float=0, chave:str=None):
        self.__id = id
        self.__nome = nome
        self.__saldo = saldo
        
        if chave is None:
            chave = self.pede_senha()
            
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()

    def pede_senha(self) -> str:
        while True:
            chave = str(input('Senha: ')).strip()
            if len(chave) >= 6:
                break

        return chave
        
    def validar_senha(self, chave) -> bool:
        resultado = None
        if sha256(chave.encode('utf-8')).hexdigest() == self.__hash:
            resultado = True
        else:
            resultado = False

        return resultado
    
    def depositar(self, valor, chave:str=None):
        if valor > 0:
            if chave is None:
                chave = self.pede_senha()
        
            if self.validar_senha(chave):
                self.__saldo += valor
                print(f'Depósito no valor de {valor} realizado com sucesso!')
            else:
                print('Senha incorreta!')
        else:
            print('Erro na operação!')
    
    def sacar(self, valor, chave:str=None):
        if valor > 0 and valor <= self.__saldo:
            if chave is None:
                chave = self.pede_senha()
                
            if self.validar_senha(chave):
                self.__saldo -= valor
                print(f'Saque no valor de {valor} realizado com sucesso!')
            else:
                print('Senha incorreta!')
        else:
            print('Erro na operação!')
    
    def __str__(self):
        return f'Conta bancária {self.__id} de {self.__nome} com saldo de R${self.__saldo}.'
