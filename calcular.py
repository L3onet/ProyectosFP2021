"""
>>> promocion = Papeleria() #estas son pruebas unitarias que nos permiten #realizar las pruebas necesarias sin tener que
>>> promocion.CalcularLapicesDeRegalo(12)#realizar las pruebas necesarias sin tener que crer otro archivo python para realizarlas mediante
0
>>> promocion = Papeleria()# esta tambien es prueba unitaria y en esta colocamos los parametro ocupados
>>> promocion.CalcularLapicesDeRegalo(20)# en esta parte le decimos que realice el metodo donde estan las acciones
5.0
>>> promocion = Papeleria()# esta tambien es prueba unitaria y en esta colocamos los parametro ocupados
>>> promocion.CalcularLapicesDeRegalo(32)# en esta parte le decimos que realice el metodo donde estan las acciones
16.0
>>> promocion = Papeleria()# esta tambien es prueba unitaria y en esta colocamos los parametro ocupados
>>> promocion.CalcularLapicesDeRegalo(40)# en esta parte le decimos que realice el metodo donde estan las acciones
(30.0, 1, 1)
"""

# crear la clase papeleria

""" Este es mi proyecto en python se simulara una calculadora que obtendra los lapices de regalo.

Autor: Rosa Lizbeth Barcenas Mancilla.
"""
class Papeleria:
    """ Esta clase calcula el numero de lapices que se regalaran en cada compra. """
    # Declarar atributos
    # Sintaxis es:
    # __nombreAtributo = tipo de (valor)
  
    __numeroDeCuadernos = int(0)
    __lapizDeRegalo = int(0)
    __lapizDeRegaloLucas = int(0)
    __lapizDeRegaloCross = int(0)
    __lapizDeRegaloNovo = int(0)
    # Declarar Metodos
    # Sintaxis es:
    # def nombreMetodo(parametros):
    # instrucciones
    
    def CalcularLapicesDeRegalo (self,numeroDeCuadernos):
      """
      Este metodo calcula la cantidad de regalos que se obtendran dependiendo de la cantidad 
      de cuadernos que se compren. 
 
      Parametros de entrada:  

      numeroDeCuadernos: Es la cantidad de cuadernos que compran.
      lapizDeRegaloLucas: Es la cantidad de lapices lucas a regalar.
      lapizDeRegaloCross: Es la cantidad de lapices cross a regalar.
      lapizDeRegaloNovo: Es la cantidad de lapices novo a regalar.

      Salida:

      lapices de Regalo del usuario.
    
      """
      self.__numeroDeCuadernos = numeroDeCuadernos
    
      if self.__numeroDeCuadernos <= 12:
        self.__lapizDeRegalo = 0
        return self.__lapizDeRegalo
        
      elif (self.__numeroDeCuadernos >12 and self.__numeroDeCuadernos <24):
        self.__lapizDeRegaloLucas = (self.__numeroDeCuadernos/4)
        return self.__lapizDeRegaloLucas

      elif (self.__numeroDeCuadernos >24 and self.__numeroDeCuadernos <36): 
        self.__lapizDeRegaloCross = ((self.__numeroDeCuadernos/4)*2)
        return self.__lapizDeRegaloCross

      elif self.__numeroDeCuadernos >36:
        self.__lapizDeRegaloNovo = ((self.__numeroDeCuadernos/4)*3)
        self.__lapizDeRegaloLucas = 1
        self.__lapizDeRegaloCross = 1
        return self.__lapizDeRegaloNovo, self.__lapizDeRegaloLucas, self.__lapizDeRegaloCross

if __name__ == '__main__':
    import doctest
    doctest.testmod()