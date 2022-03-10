"""
>>> convertidor = ConvertidorDeTiempo()
>>> convertidor.convertirSegundosAHoras(3661)
[1,1,1]
 

>>> convertidor = convertidorDeTiempo()
>>> convertidor.convertirMinutosAhoras(241)
[4,1]

"""

 # Crear la Clase de Convertidor de horas,minutos y segundos

"""Dos Atletas recorren la misma distancia y se registran sus tiempos en
segundos (at1seg) y minutos (at2min) respectivamente.
a. Se desea saber el tiempo total utilizado por el primer atleta en horas
(at1horas), minutos (at1min) y segundos.
b. Se desea saber el tiempo total utilizado por el segundo atleta en horas
(at2horas), minutos y segundos (at2seg).

Autor: Eric Eduardo Rios Torres
"""



class ConvertidorDeTiempo:

    """ 
    Convertir los segundos que hizo en primer atleta  a horas
    
    """

    # Declarar atributos 
    # Sintaxis es:
    # __nombreAtributo = tipo(valor)

    __tiempoAtleta1 = float(0.0)
    __tiempoAtleta2 = float(0.0)
    __horasAtleta1 = float(0.0)
    __minutosAtleta1=float(0.0)
    __segundosAtleta1 = float(0.0)
    __tiempoSegundosAtleta1 = float(0.0)
    __minutosAtleta2 = float(0.0)
    __horasAtleta2 = float(0.0)
     
    __tiempoTotalAtleta1 = float(0.0)
    __tiempoTotalAtleta2 = float(0.0)


    def convertirSegundosAHoras(self,tiempoAtleta1):
        """
        Este metodo se va a Convertir los segundos a horas
        
        parametros de entrada:
             tiempoAtleta1: el tiempo en segundos que registro el atetla 1 
             
    salida: 
    El sistema dirá las horas que registro el atleta1
             
        """
        
        self.__tiempoAtleta1 = tiempoAtleta1
        self.__horasAtleta1=self.__tiempoAtleta1//3600
        self.__minutosAtleta1= (self.__tiempoAtleta1 % 3600) // 60 
        self.__segundosAtleta1 = (self.__tiempoAtleta1 % 3600) % 60
        self.__tiempoTotalAtleta1 = [self.__horasAtleta1,self.__minutosAtleta1,self.__segundosAtleta1]
        return self.__tiempoTotalAtleta1

    def convertirMinutosAhoras(self,tiempoAtleta2):
        """
        Este metodo se va a Convertir los minutos a horas y después a segundos
        
        parametros de entrada:
        tiempoDeAtleta2:el tiempo que registro el atleta 2
        
        salida:
        El sistema dirá las horas y minutos que registro el atetla2
        """

        self.__tiempoAtleta2 = tiempoAtleta2
        self.__horasAtleta2 = self.__tiempoAtleta2//60
        self.__minutosAtleta2 = self.__tiempoAtleta2 % 60
        self.__tiempoTotalAtleta2 = [self.__horasAtleta2,self.__minutosAtleta2]
        return self.__tiempoTotalAtleta2

if __name__=="__main__":
   import doctest
   doctest.testmod()