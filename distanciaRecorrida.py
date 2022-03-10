"""
>>> resultado = movimientoRectilineoUniforme()
>>> resultado.calcularDistanciaRecorrida (120,12)
1440
"""

#  Crear la clase Calculo de la distancia recorrida por un móvil 

"""
El usuario desea calcular la distancia que recorre un automóvil,
el usuario solo conoce la velocidad a la que el móvil de desplaza y 
el tiempo que tardó
"""
#Autor:Isabel Granados Rebollar 


class movimientoRectilineoUniforme:
    """
    Esta clase calculará la distancia recorrida de un movil
    """
    # Declarar atributos
    # Sintaxis es:
    # ___nombreAtributo = tipo (valor)

    __distanciaRecorrida=float(0)
    __velocidad=float(0)
    __tiempo=float(0)

    # Declarar metodos
    # Sintáxis es :
    # def nombreMetodo (self, parametros):
    # """
    # Documentación 
    # """
    # Instrucciones:

    def calcularDistanciaRecorrida (self,velocidad,tiempo):
        """
        El sistema calculará la ditancia recorrida multiplicando la
        velocidad recorrida por el tiempo de desplazamiento.

        Parámetros de entrada:
            velocidad: Es el valor medido en km/h
            tiempo: Es el valor medido en horas (h)
        
        Salida:
            Mostrar el resultado de la multiplicación de la velocidad 
            por el tiempo. 
        """

        self.__velocidad = velocidad
        self.__tiempo=  tiempo 
        self.__distanciaRecorrida = self.__velocidad*self.__tiempo
        return self.__distanciaRecorrida
    

if __name__ == "__main__":
    import doctest 
    doctest.testmod()