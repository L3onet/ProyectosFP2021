"""
>>> ecuacion = ecuacionlineal()
>>> ecuaion.calcularEcuacionLienal(5, 2, 2, 3, 7, 22)
>>> ecuacion.getdeterminante()
22.0
>>> ecuacion.getvariableX()
58.0
>>> ecuacion.getvariableY()
116
"""

"""
se desea crear un algoritmo que sea capas de reslver un sistema de ecuaciones 
lineales de tres incognitas con los valores que ingrese 
el usuario 
Autor:Julian Reynoso Zavaleta
"""

from _typeshed import Self


class EcuacionLineal2Incognitas:
    __coeficienteA = float(0)
    __coeficienteB = float(0)
    __terminoIndependienteC = float(0)
    __coeficienteD = float(0)
    __coeficienteE = float(0)
    __terminoIndependienteF = float(0)
    __determinante = float (0)
    __variableX = float(0)
    __variableY = float(0)



    def calcularSolucion (self, coeficienteA, coeficienteB, terminoIndependienteC, coeficienteD, coeficienteE, terminoIndependienteF):
        """
        Se busca que el codigo resuelva un sistema de ecuacones lineales de 2x2 o tambien conocido como 
        ecuacion lineal de 2 incognitas en este caso utlizaremos el metodo mas facil que seria el metodo de cramer 
 
        """
        self.__coeficienteA = coeficienteA
        self.__coeficienteB = coeficienteB
        self.__terminoIndependienteC = terminoIndependienteC
        self.__coeficienteD = coeficienteD
        self.__coeficienteE = coeficienteE
        self.__terminoIndependienteF = terminoIndependienteF
        self.__determinande = self.__coeficienteA * self.__coeficienteE - self.__coeficienteB * self.__coeficienteD
        self.__variableX = self.__coeficienteE * self.__terminoIndependienteC - self.__coeficienteB * self.__terminoIndependienteF/self.__determinante
        self.__variableY = self.__coeficienteA * self.__terminoIndependienteF - self.__coeficienteD * self.__terminoIndependienteC/self.__determinande 


        
    def getDeterminante(self): 
        return self.__determinante

    def getVariableX(self):
         return self.__variableX
    
    def getVariableY(self):
        return self.__variableY 
    

if __name__ == '__main__': 
    import doctest
    doctest.testmod()


