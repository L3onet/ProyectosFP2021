"""
>>> recibo = JornadaLaboral()
>>> recibo.calcularSalarioNormal(40, 100)
4000
>>> recibo.calcularCostoHorasExtras(5, 100)
750.0
>>> recibo.calcularSalarioSemanal()
4750.0
"""

#Crear la clase Jornada Laboral de un empleado

"""
    La jornada de trabajo normal de un empleado durante una semana comprende 40 horas.
    Por cada hora trabajada dentro de esas 40 horas un empleado recibe el salario normal. 
    Todas las horas trabajadas por encima de esas 40 horas se consideran horas extras. 
    Por cada hora extra el empleado recibe 1.5 veces el salario que recibe por una hora normal. 
    El usuario ingresa el salario normal por hora que gana un empleado y el número de horas 
    trabajadas durante la semana. Mostrar el salario total semanal que gana el empleado.
    
    Autor: Mariana Lilibeth Antúnez García
    """
class JornadaLaboral:
    """
    Esta clase calcula el salario que debe recibir un empleado después de una jornada laboral
    """

    #Declarar atributos
    #Sintaxis es:
    #__nombreatributo = tipo(valor)
    __nombreEmpleado = str("")
    __numeroSemana = str("")
    __horasTrabajadas = int (0)
    __horasExtras = int(0)
    __salario = float(0.0)
    __total = float(0.0)
    __totalHorasExtras = float(0.0)
    __salarioTotal = float(0.0)

    #Declarar métodos
    #Sintáxis es:
    #
    #def nombreMetodo(self,parametros):
    """ Documentación"""
    #instrucciones

    def calcularSalarioNormal(self, horasTrabajadas, salario):
        """ 
        El sistema calculará el salario normal de un empleado que trabaja en una jornada 
        de 40 horas sin contar horas extras.
        
        Parámetros de entrada:
        horasTrabajadas: Son las horas trabajadas en una Jornada Laboral.
        salario: El pago que se recibe por hora.

        Salida:
        El sistema dispondrá del salario que recibe el empleado. 
        """
        self.__horasTrabajadas = horasTrabajadas
        self.__salario = salario
        self.__total = self.__horasTrabajadas * self.__salario
        return self.__total

    def calcularCostoHorasExtras(self, horasExtras, salario):
        """  El sistema calculará el costo de las horas extras trabajadas sabiendo
        que a estas se le pagan 1.5 más que una hora normal. 
    
        Parámetros de entrada:
        horasExtras: Son las horas extras trabajadas por un empleado.
        salario: El pago que recibe por hora.

        Salida:
        El sistema dispondrá del costo total por las horas extras trabajadas. 
        """
        self.__horasExtras = horasExtras
        self.__salario = salario
        self.__totalHorasExtras = self.__horasExtras * (self.__salario*1.5)
        return self.__totalHorasExtras

    def calcularSalarioSemanal(self):
        """ El sistema calculará el salario semanal de un empleado mediante sus horas 
        totales trabajadas, tomando en cuenta si trabajó horas extras o no.

        Salida: El sistema dispondrá del salario semanal obtenido.
        """ 
        self.__salarioTotal = self.__total + self.__totalHorasExtras
        return self.__salarioTotal


if __name__ == "__main__":
    import doctest
    doctest.testmod()
