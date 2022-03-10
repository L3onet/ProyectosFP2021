""""
>>> determinante = determinarDesigualdades()
>>> determinante.determinarJubilaciones(70, 20)
1
"""
"""
El IMSS necesita clasificar a las personas que se jubilarán este año.
Existen tres tipos de jubilaciones: por edad, por antigüedad joven y por
antigüedad adulta. Las personas adscritas a la jubilación por edad deben
tener 60 años o más y una antigüedad en su empleo de menos de 25 años.
Las personas adscritas a la jubilación por antigüedad joven deben tener
menos de 60 años y una antigüedad en su empleo de 25 años o más. Las
personas adscritas a la jubilación por antigüedad adulta deben tener 60
años o más y una antigüedad en su empleo de 25 años o más. Determinar
en qué tipo de jubilación quedará adscrita una persona.

Autora: Joselynne Rodriguez Cruz
"""

class determinarDesigualdades:
    """
    Esta clase es para determinar las
    3 desigualdades que existen y darle
    al usuario una respuesta
    """

    #declarar atributos
    #sintaxis es:
    #_nombreAtributo-tipo(valor)
    
    __edad = int (0)
    __antiguedad=int(0)
    
    #declarar metodos
    #sintaxis es:
    # def nombredelmetodo(self,desigualdades

    def determinarJubilaciones(self,edad,antiguedad):
        #Se realizara la primera jubilacion

        if edad >= 60 & antiguedad < 25:
            return 1
        else:
            if edad < 60 & antiguedad >= 25:
                return 2
            else:
                if edad >= 60 & antiguedad >= 25:
                    return 3
                else:
                    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()