"""
>>> Elmer = Fecha ()
>>> Elmer.getEdad (1976, 2021, 4, 12, 23, 19, 14, 21)
547, 3, 5, 7
"""
"""
Realice un algoritmo que determine aproximadamente (i.e., asuma que todos los años tienen 365 días
y que todos los meses tienen 30 días) cuántos meses, semanas, días y horas ha vivido una persona
dada la fecha y hora (no minutos) de nacimiento. Realice el diagrama de flujo y pseudocódigo del
programa.

Elmer Goiccohea Pineda 1A6
"""


class Fecha:

    __anioNacimiento = int (0)
    __anioActual = int (0)
    __mesNacimiento = int (0)
    __mesActual = int (0)
    __diaNacimiento = int (0)
    __diaActual = int (0)
    __horaNacimiento = int (0)
    __horaActual = int (0)

    def getEdad (self, anioNacimiento, anioActual, mesNacimiento, mesActual, diaNacimiento, diaActual, horaNacimiento, horaActual,):
        self.__anioNacimiento = anioNacimiento
        self.__anioActual = anioActual
        self.__mesNacimiento = mesNacimiento
        self.__mesActual = mesActual
        self.__diaNacimiento = diaNacimiento
        self.__diaActual = diaActual
        self.__horaNacimiento = horaNacimiento
        self.__horaActual = horaActual
        """
        Definimos todas las variables que vamos a usar en nuestra resolucion del problema
        las cuales seran las fechas actuales y las de nacimiento de la persona con las que
        haremos las operaciones.
        """
        horasEdad = self.__horaActual - self.__horaNacimiento
        if (horasEdad <= 0):
            horasEdad += 24
            if (horasEdad + 24):
                self.__diaActual -= 1 
        elif (horasEdad > 0):
            horasEdad += 0
        """
        calcularemos la edad en horas de una persona 

        Parametros de entrada:
            horaActual: es la hora actual del momento de hacer a operacion
            horaNacimiento: es la hora del nacimiento de la persona

        Parametros de salida:
            horaEdad: los cuales nos dara la edad de la persona en horas

        Solo se hace una simple resta que si el resultado es 0 o menor se le sumaran 24
        y se le restara 1 a los dias
        """
        diasEdad = self.__diaActual - self.__diaNacimiento
        if (diasEdad <= 0):
            diasEdad += 30 
            if (diasEdad + 30):
                self.__mesActual -= 1
        elif (diasEdad > 0):
            diasEdad += 0
        
        semanasEdad  = diasEdad // 7
        
        dias = semanasEdad * 7
        diasEdadTotal = diasEdad - dias
        """
        Calcularemos la edad en dias de una persona

        Parametros de entada:
            diaActual: es el dia actual al momento de hacer la operacion
            diaNacimiento:  es el dia de nacimiento de la persona

        parametros de salida:
            semanasEdad: son las semanas edad de la persona
            diasEdadTotal: los cuales son los dias de edad de la persona

        Para llegar al resultado primero hacemos una resta de los dias y si el resultado es 0 o menor
        se hara la condicon de sumarle 30 y se restara 1 mes a los meses

        El resultado se dividira en 7 para obtener el resultado de las semanas

        El resto de la divicion seran los dias edad de la persona     
        """
        meses = self.__anioActual - self.__anioNacimiento
        mesesTotal = meses * 12
        total = self.__mesActual - self.__mesNacimiento
        mesEdad = total + mesesTotal
        """
        Calcularemos la edad en meses de una persona

        Parametros de entrada:
            mesActual: es el mes actual al momento de hacer la operacion
            mesNacimiento: es el mes de nacimiento de la persona

        Parametros de salida:
            mesEdad: son los meses de edad de la persona

        Se hace la resta de lo años actuales menos los de nacimieto y el resultado se multiplica por 
        12 y se suma lo que sale del resultado de la resta entre los meses actuales menos los de 
        nacimiento.
        """
        return mesEdad, semanasEdad, diasEdadTotal, horasEdad

    if __name__ ==  '__main__ ':
        import doctest
        doctest.testmod()