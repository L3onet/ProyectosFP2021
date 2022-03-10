"""
>>> numero = Numerologia()
>>> numero.calcularEdad(2021, 11, 23, 2003, 11, 24)
17
>>> numero.convetrirEdadEnHoras()
148920
>>> numero.identificarSignoZodiacal()
'Sagitario'
>>> numero. calcularNumeroSuerte()
5
"""

"""
Desarrollar un algoritmo que pida el nombre del usuario, el día, mes y
año actual y el día, mes y año de nacimiento del usuario. En base a esos
datos el algoritmo indica el signo zodiacal, la edad en horas y el número
de la suerte del usuario.

Autor: Natalia Gutiérrez Pineda.
"""

class Numerologia:
    """
    Esta clase indica  la edad, signo sodiacal y numero de la suerte del 
    usuario.
    """

    # Declarar atributos
    # Sintaxis es:
    # __nombreAtributo = tipo(valor)
    __nombre = str(" ")
    __anioNacimiento = int(0)
    __mesNacimiento = int(0)
    __diaNacimiento = int(0)
    __anioActual= int(0)
    __mesActual = int(0)
    __diaActual = int(0)
    __edad = int(0)
    __edadHoras = int(0)
    __signoZodiacal = str(" ")
    __numeroSuerte = int(0)

    #Declarar metodos:
    # Sintaxis es:
    # def nombreMetodo(self, parametros):
    #     """
    #     Documentación
    #     """
    #     instrucciones

    def calcularEdad(self, anioActual, mesActual, diaActual, aniNacimiento, mesNacimiento, diaNacimiento):
        """
        Este metodo calcula la edad del usuario.

        Parametros de entrada:
            anioActual: Es el valor del año actual.
            anioNacimiento: Es el valor del año en que nacio el usuario.

        Salida:
            La edad del usuario.
        """
        self.__anioActual = anioActual
        self.__mesActual = mesActual
        self.__diaActual = diaActual
        self.__anioNacimiento = aniNacimiento
        self.__mesNacimiento = mesNacimiento
        self.__diaNacimiento = diaNacimiento
        self.__edad = self.__anioActual - self.__anioNacimiento
        if (self.__mesActual < self.__mesNacimiento) or (self.__mesActual == self.__mesNacimiento and self.__diaActual < diaNacimiento):
            self.__edad = self.__edad - 1

        return self.__edad
    
    def convetrirEdadEnHoras(self):
        """
        Este metodo convertirá la edad en años del usuario a horas a 
        partir de la equivalencia de años a horas.

        Parametros de entrada:
            edad: Es el valor de la edad del usuario.

        Salida:
            La edad del usuario en horas.
        """
        self.__edadHoras = self.__edad * 8760
        return self.__edadHoras

    def identificarSignoZodiacal(self):
        """
        Este metodo identificara el signo zodiacal del usuario.

        Parametros de entrada:
            mesNacimiento: Es el valor del mes de nacimiento del usuario.
            diaNacimiento: Es el valor del dia en que nacio el usuario.

        Salida:
            El signo zodiacal del usuario.
        """

        if (self.__mesNacimiento == 12 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 1 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = ('Capricornio')
        if (self.__mesNacimiento == 1 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 2 and self.__diaNacimiento <= 19):
            self.__signoZodiacal = ('Acuario')
        if (self.__mesNacimiento == 2 and self.__diaNacimiento >= 20) or (self.__mesNacimiento == 3 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = ('Piscis')
        if (self.__mesNacimiento == 3 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 4 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = ('Aries')
        if (self.__mesNacimiento == 4 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 5 and self.__diaNacimiento <= 20):
            self.__signoZodiacal = ('Tauro')
        if (self.__mesNacimiento == 5 and self.__diaNacimiento >= 21) or (self.__mesNacimiento == 6 and self.__diaNacimiento <= 21):
            self.__signoZodiacal = ('Géminis')
        if (self.__mesNacimiento == 6 and self.__diaNacimiento >= 22) or (self.__mesNacimiento == 7 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = ('Cáncer')
        if (self.__mesNacimiento == 7 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 8 and self.__diaNacimiento <= 23):
            self.__signoZodiacal = ('Leo')
        if (self.__mesNacimiento == 8 and self.__diaNacimiento >= 24) or (self.__mesNacimiento == 9 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = ('Virgo')
        if (self.__mesNacimiento == 9 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 10 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = ('Libra')
        if (self.__mesNacimiento == 10 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 11 and self.__diaNacimiento <= 22):
            self.__signoZodiacal = ('Escorpio')
        if (self.__mesNacimiento == 11 and self.__diaNacimiento >= 23) or (self.__mesNacimiento == 12 and self.__diaNacimiento <= 21):
            self.__signoZodiacal = ('Sagitario')
        return self.__signoZodiacal

    def calcularNumeroSuerte(self):
        """
        Este metodo calculara el Numero de la suerte del usuario.

        Salida:
            El numero de la suerte del usuario.
        """
     
        self.__primerDigito = self.__anioNacimiento % 10
        self.__primerCociente = self.__anioNacimiento // 10
        self.__segundoDigito = self.__primerCociente % 10
        self.__segundoCociente = self.__primerCociente // 10
        self.__tercerDigito = self.__segundoCociente % 10
        self.__tercerCociente = self.__segundoCociente // 10
        self.__cuartoDigito = self.__tercerCociente
        self.__numeroSuerte = self.__primerDigito + self.__segundoDigito + self.__tercerDigito + self.__cuartoDigito
        
        while self.__numeroSuerte > 9:
            self.__numeroSuerte = self.__numeroSuerte - 9
        
        return self.__numeroSuerte

if __name__ == "__main__":
    import doctest
    doctest.testmod()
