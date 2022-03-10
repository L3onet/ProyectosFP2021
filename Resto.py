"""
>>> resto = Numero()
>>> resto.evaluarOperacion(245,100,46)
False
"""

"""
Un usuario desea conocer si de tres números al efectuar 
la división entre el primer número y el segundo el resto 
corresponda al valor del tercer número. Se conocen el 
valor de los tres números. 

Autor: Ruht Noemi Catalan Angel 
"""
class Numero:
    """
    Esta clase evalua si el resto de la division de dos numeros es igual al tercer numero 
    """
    __sonIguales = bool(False)
    __numero1 = int(0)
    __numero2 = int(0)
    __numero3 = int(0)
    __resto = int(0)
    
    def evaluarOperacion(self, numero1, numero2, numero3): 
     """
    El metodo calculara la division entre el primer numero y el segundo para conocer si el 
    resto es igual al tercer numero.

    Parametros de entrada: 
        numero1: Es el primer numero 
        numero2: Es el segundo numero
        numero3: Es el tercer numero 

    Salida: 
        Evaluar si el resto es igual al tercer numero
     """
     self.__numero1 = numero1
     self.__numero2 = numero2
     self.__numero3 = numero3
     if self.__numero2 == 0:
        self.__sonIguales = False
     else: 
        self.__resto = self.__numero1 % self.__numero2
        self.__sonIguales = (self.__resto == self.__numero3)
     return self.__sonIguales
if __name__ == '__main__':
    import doctest
    doctest.testmod()
