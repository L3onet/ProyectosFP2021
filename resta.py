#Esta clase es para iniciar en el mundo de la programacion
"""
>>> result=resta()
>>> result.resultado(1,9,8)
True
>>> result.resultado(1,2,3)
False
"""

"""

Escribir un algoritmo que dado tres numeros indique si el
tercero es el resultado de la resta de los dos primeros el
primero menos el segundo y el segundo menos el primero.

Autor: Enrique Ruiz Peralta 
"""




class resta:
    """
    Esta clase realiza las restas entre los dos primeros numeros 
    """

    #declarar atributos
    #sintaxis es:
    #_nombreAtributo=tipo (valor)

    
    __numero1 = float(0.0)
    __numero2 = float(0.0)
    __numero3 = float(8.0)
    __rest1 = float(0.0)
    __rest2 = float(0.0)


    #declarar metodos
    #sintaxis es:
    #    def nombredelmetodo(self,parametro)       
        

    def resultado(self, numero1, numero2, numero3):
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.__rest2 = self.__numero2 - self.__numero1
        self.__rest1 = self.__numero1 - self.__numero2
        if numero3 == self.__rest1 or self.__numero3 == self.__rest2:
            return True
        
        else:
            return False

if __name__ == '__main__':
      import doctest
      doctest.testmod()
