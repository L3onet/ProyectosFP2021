"""
>>> conv = convertidor(80, 20)
>>> conv.get_yardas()
94.18869856750992
>>> conv.get_metros()
86.09570252971655
>>> conv.get_millas()
138527.98537031392
>>> conv.get_pulgadas()
3389.5878085949403

Dada una cantidad expresada en pies y otra en metros, determinar la
suma pero convertida a pulgadas, a yardas, a metros y a millas por
separado

Autor: Alejandro Vidal Perez
"""

class convertidor:
    __yardas = float(0)
    __metros = float(0)
    __millas = float(0)
    __pulgadas = float(0)

    def __init__(self, metros, pies):
        #Se realizará la sumatoria de todos los métodos
        piesConvertidos = pies / 3.281
        self.__metros = metros + piesConvertidos
        self.__convertirMetrosPulgadas(metros)
        self.__convertirMetrosPulgadas(piesConvertidos)
        self.__convertirMetrosYardas(metros)
        self.__convertirMetrosYardas(piesConvertidos)
        self.__convertirMetrosMillas(metros)
        self.__convertirMetrosMillas(piesConvertidos)

    #Getters
    def get_yardas(self):
        return self.__yardas

    def get_metros(self):
        return self.__metros

    def get_millas(self):
        return self.__millas

    def get_pulgadas(self):
        return self.__pulgadas

    def __convertirMetrosPulgadas(self, metros):
        #El programa realizará la conversión de metros a pulgadas

        self.__pulgadas += metros * 39.37

    def __convertirMetrosYardas(self, metros):
        #El programa realizará la conversión de metros a yardas.
        self.__yardas += metros * 1.094

    def __convertirMetrosMillas(self, metros):
        #El programa realizará la conversión de metros a millas.
        self.__millas += metros * 1609

if __name__ == "__main__":
    import doctest
    doctest.testmod()