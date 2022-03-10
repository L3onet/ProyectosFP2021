#calcular cantidad minima de monedas de cambio
"""
>>>moneda
>>>monedas usadas 

"""
"""Partiendo de una cantidad de dinero menor a un dólar que se tiene que dar de cambio (vuelto),
 calcular el número  de monedas que hay que dar (suponiendo que se cuenta con todas las monedas necesarias)
  de 1, 5, 10, 25, 50 centavos. Debe dar la menor cantidad de monedas posible"""

class centavo:
    __centavos50:int(0)
    __centavos25:int(0)
    __centavos10:int(0)
    __moneda:int(0)
    __minmonedasusadas:int(0)

def restarcentavos50(self,centavos50,moneda):
        monedasusadasde50=centavos50-moneda
        return monedasusadasde50

def restarcentavos25(self,centavos25,moneda):
        monedaA=centavos25-moneda
        return monedaA

def restarcentavos10(self,centavos10,moneda):
        monedaC=centavos10-moneda
        return monedaC

def restarcentavos5(self,centavos5,moneda):
        monedaD=centavos5-moneda
        return monedaD

def sumarcentavosusados(self,mondeA,monedaB,monedaC,monedaD):
    monedasusadas=mondeA +monedaB + monedaC + monedaD
    return monedasusadas

if __name__ =='__main__':
    import doctest
    doctest.testmod()
