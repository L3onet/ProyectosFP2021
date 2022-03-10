"""
>>> CDCAV = CaidaDeCuerposAlVacio()
>>> CDCAV.E= 0.5*9.81*6(0.5*9.81*6)
58.56
"""

"""
Un usario quiere concer cual es la velocidad con la que cae un cuerpo al vacio.

Autor: Leticia Anette Borja Reynoso
"""

class CaidaDeCuerposAlVacio:
    """
    El sistema calculara cual es la velocidad con la que cae un cuerpo al vacio.
    """
    
    # Declarar atributos
    # Sintaxis es
    #    __nombreAtributo = tipo(valor)

    __tiempo= int (0)
    __gravedad= float(0.0)
    __E= float(0.0)

    #Declarar los metodos 
    #Sintaxis es:
    #    __def nombreMetodo (self, parametros)

    def CalcularE (self, tiempo, gravedad):
     """
     El metodo calculara E que es la velocidad con la que cae elcuerpo.

     Parametros de entrada:
     Tiempo: es el tiempo en que tarda en caer el cuerpo.
     Gravedad: es la gravedad de nuestro planeta.
     E: es la formula con la que se calcula la velocidad con la que cae el cuerpo.
    
     Salida:velocidad con la que cae el cuerpo.
     """
     self.__tiempo = tiempo
     self.__gravedad = gravedad
     self.__E = (0.5*self.__gravedad*self.__tiempo)(0.5*self.__gravedad*self.__tiempo)
     return self.__E 

if __name__== '__main__':
    import doctest
    doctest.testmod()