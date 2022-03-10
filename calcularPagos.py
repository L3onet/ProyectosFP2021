"""
>>> carritoCompras = totaldecompras()
>>> carritoCompras.calculartotalapagar(1000,15)
850.0
"""
#calcular el total a pagar

"""
el usuario desea saber el total de su compra,
el usuario solo conoce el totsl de su compra
sin saber cuanto pagara con el descuento aplicado
"""
#Christopher Alexis Cruz Rosales

class totaldecompras:
    """"
    Esa clase sacara el total a pagar del comprador
    """

    # Declarar Atributos
    # Sintaxis es:
    #__nombreAtributo = tipo(valor)
    __totaldecompra=float(0)
    __descuento=float(0)
    __totalapagar=float()
    # Declarar metodos:
    # Sintaxis es:
    # def nombre metodo (self, total)
    #"""
    #Dcoumentacion
    #"""
    # Instrucciones:
     
    def calculartotalapagar(self,totaldecompra,descuento):
        """
        El sistema calculara el total a pagar, multiplicando 
        el total por el descuento
        parametros de entrada:
            total de compras: es el resultado de la compra 
        descuento: es el descuento que se le aplicara al total de compra

        salida: 
            se calculara el total de la compra
        """
        self.__totaldecompra = totaldecompra
        self.__descuento = descuento / 100
        self.__totalapagar = self.__totaldecompra - (self.__totaldecompra * self.__descuento)
        return self.__totalapagar
if __name__ == "__main__":
    import doctest
    doctest.testmod() 



    
