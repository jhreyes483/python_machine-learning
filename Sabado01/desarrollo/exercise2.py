# Problema de vectores
# La empresa "Margarita" vende papas fritas de 7 referencias distintas.
# Se necesita conocer las ventas pro referencia en un dia y el total general de ventas, tanto en cantidades como en dinero


#  por semana
# Totalizar cuanto se vende por:
# Por referencia        ---------------  ok
# Por dia               ---------------  ok
# Total general         ---------------  ok
# Saber cual fue la venta mayor con referencia y dia -- ok
# Saber cual fue la venta menor con referencia y dia -- ok
import numpy as np


class Calcula:

    def __init__(self): # Constructor
        self.R = 7 # 7 referencias 
        self.D = 5 # 5 dias de una semana 
        #import numpy as np

        self.canVentas,self.valReference,self.detalle = [], [], []
        # Declarar vector
        self.canVentas    = np.full((self.D,self.R),0)
        self.valReference = np.full((self.D,self.R),0)
        self.detalle      = np.full((self.D,self.R),0)
        self.valorTotal   = 0

        # Ejecuta acciones del objeto
        self.titulo()
        self.cantidadReferencia()
        self.valorReferencia()
        self.costos()
        self.minMax()
        self.salir()
        #############################################



    def cantidadReferencia(self):
        for dia in range(self.D):
            for referencia in range(self.R):
                self.canVentas[dia][referencia]= int(input(f"Digite la cantidad de ventas día {1+dia} referncia no. {referencia} :" ))


    def valorReferencia(self):
        for dia in range(self.D):
            for referencia in range(self.R):
                self.valReference[dia][referencia]= int(input(f"Digite valor de ventas de la referencia día {1+dia} referencia no. {referencia} :" ))


    def costos(self):
        for dia in range(self.D):
            for referencia in range(self.R):
                subtotal = np.sum(self.canVentas[dia][referencia]) *  np.sum(self.valReference[dia][referencia])
                self.detalle[dia][referencia] = subtotal
                self.valorTotal = self.valorTotal + subtotal
                # print(self.valorTotal)       

    def minMax(self):
        self.max = np.amax(self.detalle, axis=1) 
        self.max = np.max( self.max )

        self.min = np.amin(self.detalle, axis=1) 
        self.min = np.min( self.min )


    def mostrar(self):
        print("Valores ingresados")
        print('Matriz cantidades ventas')
        print(self.canVentas)
        print('Matriz valor referencias')
        print(self.valReference)
        print('Subtotal referencias')
        print(self.detalle)
        print("---------------------------")
  

        # VALOR TOTAL POR REFENCIA
        for referencia in range(self.R):
           # print(self.detalle[:,referencia: (referencia+1) ])
            sumRefencia = np.sum (self.detalle[:,referencia: (referencia+1) ])
            print(f"La referencia {referencia} tiene un valor total en ventas de: $ { sumRefencia } ")

    
        print(f"Valor total en ventas: $", str(self.valorTotal))

        # VALOR TOTAL POR DIA
        for dia in range(self.D):
            #print(self.detalle[dia]  )
            #print(np.sum(self.detalle[dia]))
            valorVentas = np.sum(self.detalle[dia])
            print(f"Valor total ventas del día {dia+1}: $", str(valorVentas))

        # VALOR MENOR
        for dia in range(self.D):
            for referencia in range(self.R):
                if(self.detalle[dia][referencia] == self.max):
                    print(f"Valor maximo en ventas fue el día {dia+1} de la referencia {referencia}: $",str(self.max) )
            
                if(self.detalle[dia][referencia] == self.min):
                    print(f"Valor manimo en ventas fue el día {dia+1} de la referencia {referencia}: $",str(self.min) )


    def titulo(self):
        print("Empresa Margarita")


    def salir(self):
        print("Salir Empresa Margarita")


papas = Calcula()
papas.mostrar()


