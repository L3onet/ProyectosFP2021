"""
>>> Ecuacion = EcuacionLineal()
>>> Ecuacion.calcularEcuacionesLinealesConDosIncognitas(2, 1, 3, 4, 8, 6) 
>>> Ecuacion.getDeterminante()
12
>>> Ecuacion.getVariableX()
23.5
>>> Ecuacion.getVariableY()
11.0
"""

# Esta clase es para entrar en el mundo de la programacion

"""
Se desea resolver un sistema de ecuaciones lineales con dos incógnitas,
plasmado en un algoritmo que pueda resolverlos de manera eficaz cualquier
ecuación que el usuario introduzca.
El método que se utilizará para resolver las ecuaciones será por
determinantes, tomando en cuenta que, si el determinante obtenido de los
valores es 0, el sistema no tendrá solución para la ecuacion.

Autor: Erick Domingo Nava Rodriguez
"""

class EcuacionLineal:
    """
    Esta clase permite comonocer los elementos que conforman la ecuacion
    """
    # Declarar los atributos
    # Sintaxis es:
    #    __ nombreAtributos=tipo(valor)
    
    __coeficienteA = float(0)
    __coeficienteB = float(0)
    __terminoIndependienteC = float(0)
    __coeficienteD = float(0)
    __coeficienteE = float(0)
    __terminoIndependienteF = float(0)
    __determinante = float(0)
    __variableX = float(0)
    __variableY = float(0)


    # Declarar metodos
    # Sintaxis es:
    #     def nombreMetodo(self, parametros):

    def calcularEcuacionesLinealesConDosIncognitas (self, coeficienteA, coeficienteB, terminoIndependienteC, coeficienteD, coeficienteE, terminoIndependienteF):
        """
        El sistema calculara ecuaciones lineales con dos incógnitas,
        donde identificará los valores de las incognitas mediante el metodo de determiantes

        Parametros de entrada:
            Determiantes: El determinante de nuestro sistema es el que
            nos ayudara  a conocer el valor de las incognitas

        Salida:
            El sistema dispondra de los valores de las incógnitas en la ecuacion
        """

        self.__coeficienteA = coeficienteA
        self.__coeficienteB = coeficienteB
        self.__terminoIndependienteC = terminoIndependienteC
        self.__coeficienteD = coeficienteD
        self.__coeficienteE = coeficienteE
        self.__terminoIndependienteF = terminoIndependienteF
        self.__determinante = self.__coeficienteA * self.__coeficienteE - self.__coeficienteB * self.__coeficienteD  
        self.__variableX = self.__coeficienteE * self.__terminoIndependienteC - self.__coeficienteB * self.__terminoIndependienteF / self.__determinante
        self.__variableY = self.__coeficienteA * self.__terminoIndependienteF - self.__coeficienteD * self.__terminoIndependienteC / self.__determinante

    def getDeterminante(self): 
        return self.__determinante

    def getVariableX(self):
         return self.__variableX
    
    def getVariableY(self):
        return self.__variableY





if __name__ == '__main__':
   import doctest
   doctest.testmod()