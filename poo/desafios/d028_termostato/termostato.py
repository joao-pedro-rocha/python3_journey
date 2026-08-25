
class Termostato:
    __temperatura = 24
    
    @property
    def temperatura(self):
        return f'A temperatura atual é {self.__temperatura}°C'
        
    @temperatura.setter
    def temperatura(self, temp):
        if type(temp) != int and type(temp) != float:
            raise ValueError("Temperatura inválida!")
        if 16 <= temp <= 30:
            self.__temperatura = temp  
        if temp % 1 != 0.5 and temp % 1 != 0:
            raise ValueError("Temperatura inválida!")
