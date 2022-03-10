"""
>>> incentivo = operador()
>>> incentivo.calcularIncentivos(120,130,156,178,98,45)
True

"""
"""
 
Se tiene registrada la producción (unidades) logradas por un operario a lo largo de la semana (lunes a sábado).
Elabore un algoritmo que nos muestre o nos diga si el operario recibirá incentivos sabiendo que el promedio de 
producción mínimo es de 100 unidades. 
Realice el diagrama de flujo y el pseudocódigo.
 
Autor: Abisai Geronimo Ortiz
 
"""
class operador: 
    
    """
    Esta clase se encarga de ver los dias en los que el trabajador genero unidades, y la cantidad que genero, viendo si es o no acreedor a incentivos.
 
    """
    __lunes=float(0)
    __martes=float(0)
    __miercoles=float(0)
    __jueves=float(0)
    __viernes=float(0)
    __sabado=float(0)
    __cantidadUnidades=float(0) 
    __totalUnidades=float(0)
    def calcularIncentivos(self,lunes,martes,miercoles,jueves,viernes,sabado): 
        """
        El metodo se encargara de ver si el trabajador obtendra o no incentivos, basandose en las unidades generadas.
        
        Parametros de entrada:
            diasTrabajados: Se conocen los dias trabajados.
            cantidadUnidades: Se conocen las unidades generadas diariamente.
        
        Salida: El algoritmo nos debe mostrar si el operador es acreedor o no a incentivos.
        
        """
        self.__lunes = lunes
        self.__martes = martes
        self.__miercoles = miercoles
        self.__jueves = jueves
        self.__viernes = viernes
        self.__sabado = sabado
        self.__cantidadUnidades = self.__lunes+self.__martes+self.__miercoles+self.__jueves+self.__viernes+self.__sabado 
        self.__totalUnidades = self.__cantidadUnidades/6

        if self.__totalUnidades>=100:
            return True
        else:
            return False

    if __name__== '__main__':
        import doctest
        doctest.testmod()
