"""
>>> Ecuacion = Coeficientes()
>>> Ecuacion.calcularCoeficientes(3, 8, 2)
-2.0
"""

class Coeficientes ():

    def calcularCoeficientes(self, a, b, c):
        
        if c == 0:
            x = "El resultado de la ecuacion es: " + str((-(b))/a)
        else:
            x = "El resultado de la ecuacion es: " + str((-(b) + c)/a)
        return x
                  
if __name__ == "__main__":
    import doctest
    doctest.testmod()
