class Retangulo:
    def __init__(self, base:float=1, altura:float=1):
        self._base = None
        self._altura = None
        self._area = None
        
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base:float):
        if type(base) != float and type(base) != int:
            raise TypeError('Valor para base inválido deve ser inteiro ou real!')
        if base < 0:
            raise ValueError('Valor para base inválido deve ser maior que zero!')
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura:float):
        if type(altura) != float and type(altura) != int:
            raise TypeError('Valor para altura deve ser inteiro ou real!')
        if altura < 0:
            raise ValueError('Valor para altura deve ser maior que zero!')
        else:
            self._altura = altura

    @property
    def area(self):
        self._area = self._base * self._altura

        return self._area

    @area.setter
    def area(self):
        return PermissionError('Área não pode ser configurada desta maneira')

    @property
    def medidas(self) -> str:
        txt = ''
        txt += f'O valor da base é {self._base}\n'
        txt += f'O valor da altura é{self._altura}\n'
        txt += f'O valor da área é {self._area}'

        return txt

    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError('Os valores numéricos devem ser passados dentro de uma tupla!')
        if len(valores) != 2:
            raise ValueError('Informe uma tupla com dois valores numéricos!')

        self.base = valores[0]
        self.altura = valores[1]
            
        
        