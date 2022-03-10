"""
>>> cantidad = Numero()
>>> cantidad.calcularCifra(45)
2
"""

"""
Diseñe un programa que lea un número entero (positivo o negativo) de 
máximo 4 cifras (validar) y determine si tiene 1, 2, 3 o 4 cifras imprimiendo 
lo que corresponda

Autor: Luis Donaldo
"""

class Numero:
    """
    Saber el numero que el usuario ingresó
    """

    # Declarar atributos
    # Sintaxis es:
    #   _ _nombreAtributo = Tipo(valor)
    
    __cifra = int(0)
    __totalDigito =  int(0)

    # Declarar los métodos
    # Sintaxis es:
    #    def nombreMetodo(self, parametros):

    def calcularCifra(self, cifra):
        """
        Diseñe un programa que lea un número entero (positivo o negativo) de 
        maximo 4 cifras (validar) y determine si tiene 1, 2, 3 o 4 cifras imprimiendo
        lo que corresponda

        Parámetros de entrada:
            cifra = Ingresa una cifra 
        Salida:
           El total de cifras que tiene el número
        """
        self.__cifra = cifra

        if (self.__cifra < 0 or self.__cifra > 9999):
            self.__totalDigito = 0
        elif (self.__cifra < 10):
            self.__totalDigito = 1
        elif (self.__cifra < 100 and self.__cifra >= 10):
            self.__totalDigito = 2
        elif (self.__cifra < 1000 and self.__cifra >= 100):
            self.__totalDigito = 3
        elif (self.__cifra < 10000 and self.__cifra >= 1000):
            self.__totalDigito = 4
        return self.__totalDigito

if __name__== '__main__':
    import doctest
    doctest.testmod()



    


            
           





        



