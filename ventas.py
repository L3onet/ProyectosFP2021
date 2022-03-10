"""
>>> ventas = venta()
>>> ventas.sueldoVendedorPorVenta(1000,2000,4000)
700.0
>>> ventas.comisionPorMesDeVenta(6700)
7400.0
"""

#falta definir formula en la depuracion 

"""
Calcular el total que recibirá un vendedor  en el mes tomando en 
cuenta su sueldo base y las comisión de sus tres ventas.
"""

# Crear la Clase ventas

"""
El  sistema  realizará  una operación para saber cuánto será el sueldo 
un vendedor, sumando la comisión obtenida de las tres ventas que 
realizo en él mes.
Autor: Jose Antonio Herrera Chamu
"""

class venta:

    """
    Calcular el sueldo del vendedor del primer mes 
    """

    # Declarar los atributos 
    # Sintaxis es: 
    # _nombreAtributo = tipo(valor)

    __venta = float (0.0)
    __sueldoVendedor = float (0.0)
    __comisionPorMes = float (0.0)

    def sueldoVendedorPorVenta(self,venta1,venta2,venta3): 

        """
        Este método calculará el sueldo del vendedor al mes por venta.
        Parametros de entrada:
        Identificar el sueldo base del vendedor.
        Identificar el sueldo del vendedor por venta.
        Salida:
        El  sistema  dispondrá  del sueldo total que recibirá un vendedor en
        un mes.
        """
        self.__venta = venta1 + venta2 + venta3
        self.__comisionPorMes = self.__venta * 0.10
        return self.__comisionPorMes

    def comisionPorMesDeVenta (self,sueldo):

        """
        Este método calculará la comisión del vendedor al mes por venta.
        Paraetros de entrada:
        Identificar las ganancias que el vendedor obtuvo por venta cada mes.
        Identiicar la comision que gano por mes.
        Salida:
        El sistema dispondrá la comisión que el vendedor obtuvo por mes.
        """ 
        self.__sueldoVendedor= sueldo + self.__comisionPorMes
        return self.__sueldoVendedor

if __name__ == '__main__':
    import doctest
    doctest.testmod () 

    