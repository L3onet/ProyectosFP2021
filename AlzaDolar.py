#Esta clase es para iniciar en el mundo de la programacion
"""
>>> MAD=MayorAlzaDelDolar()
>>> MAD.Resta1(20, 10)
>>> MAD.Resta2(30, 15)
>>> MAD.diferencia()
15
 
"""

"""
Un analista financiero lleva un registro del precio del dólar día a día. Y desea saber 
cuál fue la mayor de las alzas en el precio diario a lo largo de ese periodo. 
Escriba un programa que pida al usuario ingresar el número n de días, y luego el precio
del dólar para cada uno de los n días.  El programa debe entregar como salida cuál fue la mayor
de las alzas de un día para el otro.Si en ningún día el precio subió, la salida debe decir: No hubo alzas.

Autor: Paola Sanchez Miranda
"""

class MayorAlzaDelDolar:
    """
    Esta clase calcula la mayor de la alza 
    del dólar de un periodo de dia a dia.
    """

    #declarar atributos
    #sintaxis es:
    #_nombreAtributo=tipo (valor)

    
    __Dia1 = float(0.0)
    __Dia2 = float(0.0)
    __Dia3 = float(0.0)
    __Dia4 = float (0.0)
    __Rest1 = float(0.0)
    __Rest2 = float(0.0)
    __difer = float(0.0)


    #declarar metodos
    #sintaxis es:
    #    def nombredelmetodo(self,parametro)

    

    def Resta1(self, Dia1, Dia2):
        #Se realizara la resta del dia 1 con el dia 2
        self.__Dia1 = Dia1
        self.__Dia2 = Dia2

        self.__Rest1=self.__Dia1-self.__Dia2

    def Resta2(self, Dia3, Dia4):
        #Se realizara la resta del dia 3 con el dia 4
        self.__Dia3 = Dia3
        self.__Dia4 = Dia4
        self.__Rest2 = self.__Dia3 - self.__Dia4

    def diferencia(self):
        if self.__Rest1 > self.__Rest2:
            return self.__Rest1

        elif self.__Rest2 > self.__Rest1:
            return self.__Rest2

if __name__ == '__main__':
      import doctest
      doctest.testmod()
