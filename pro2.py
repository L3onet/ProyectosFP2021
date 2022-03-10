"""
>>> hx = Hexágono()
>>> hx.calcularApotema(6)
5.196152422706632
>>> hx.calcularPerimetro(6)
36
>>> hx.calcularArea(5.19,36)
93.42
"""

import math as raiz

"""
Desarrolle un algoritmo que dadas las longitudes de un hexágono
regular, calcule el área del polígono y calcular la apotema y el perímetro de
un hexágono regular inscrito en una circunferencia de un radio dado.
 
 Autor: Jonathan Matias Matias
"""

class Hexágono: 
    """
    Esta clase calculara el perimetro, apotema y el área de un hexagono regular
    """
    __cateto = float(0.0)
    __apotema = float(0.0)
    __perimetro = float (0.0)
    __apotema = float(0.0)
    __area = (0.0)

    def calcularPerimetro(self, cateto,): 
        """
        El sistema calculará el perímetro del hexágono a
        partir del valor dado

        Parámetros de entrada:
               cateto: Es el valor de uno de los lados del hexágono

             Salida:
             El valor del perímetro
         """
        self.__cateto = cateto
        self.__perimetro = self.__cateto * 6
        return self.__perimetro

    
    def calcularApotema(self, cateto):
        """
      el sistema calculará el valor de la apotema dado el valor de un cateto del hexágono
      Parámetros de entrada:
               cateto: Es el valor de uno de los lados del hexagono

             Salida:
             El valor del apotema
      """
        self.__cateto = cateto
        self.__apotema = (raiz.sqrt((self.__cateto * self.__cateto)-((self.__cateto/2)* (self.__cateto/2))))
        return self.__apotema
  

    def calcularArea(self, perimetro, apotema):
        """
        El sistema calculará el área del hexagono
        Parámetros de entrada:
               perímetro: Es el valor obtenido en el método
               apotema: el valor obtenido en el método calcularApotema 
         

             Salida:
             El valor del apotema
        """
        self.__perimetro = perimetro 
        self.__apotema= apotema
        self.__area = (self.__perimetro * self.__apotema) / 2
        return self.__area
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()