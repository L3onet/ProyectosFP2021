"""
>>> latidos = latidosDelCorazon()
>>> latidos.calcularNumeroDePulsaciones(56)
164
"""
# calcular el numero de pulsaciones de una persona por minuto 

"""
se ha establecido que el numero de latidos por minuto que cualquier persona puede alcanzar sin correr riesgos de salud
es igual a 220 menos la edad de la persona en años asociaciones medicas recomiendan mantener el numero de latidos por 
minuto durante ua sesion de ejercicio fisico en un rango seguro que esta entre el 50 y el 85% del numero maximo 
mencionado calcular el rango seguro de latidos por minuto usando la edad de una persona como dato de entrada 

Autor: Alexander Alcantar Arana 
"""

class LatidosDelCorazon: 
    """
    El sistema calculara el rango seguro de pulsaciones por minuto usando la edad de una persona como dato de entarda.
    """

    __pulsaciones = int(0)                 
    __edad = int(0)
    __totalpulsaciones = int(0)

    def calcularNumeroDeLatidoss(self, edad):  
       
        """
        El metodo calculara el numero de pulsaciones de una persona con su edad en años como dato de entrada.

        Parametros de entrada:
            Numero de pulsaciones: conocer el numero maximo de pulsaciones 
            Edad: conocer su edad 
        
        Salida: 
            el total de pulsaciones obtenidas. 
        """
        self.__pulsaciones = 220 
        self.__edad = edad 
        self.__totalpulsaciones = self.__pulsaciones - self.__edad
        return self.__totalpulsaciones

if __name__== '__main__':
    import doctest
    doctest.testmod()