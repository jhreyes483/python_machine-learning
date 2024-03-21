# Apreciado Estudiante:
# Haciendo uso de diccionarios, tuplas, sets  y listas realizar un programa python que permita el cambio de divisas
# Se recomienda al menos 5 tipos de divisas

# Se debe informar la ganancia para el comprador y para el vendedor
import numpy as np
from urllib.request import urlopen
import json


class Divisa:
    def __init__(self): # Constructor
        self.pais, self.coins = [], []
        self.D1 = 5
        self.D2 = 5
        self.priceUno = np.zeros((self.D1,self.D2))
        self.abr    = {0:"USD",1:"EUR",2:"JPY",3:"GBP",4:"COP" }
        self.coins2 = {0:'Dolar',1:'Euro', 2:'Yen',3:'Libra',4:'Peso'}


        self.refreshDivisas()
        self.printPriceToDay()
        self.priceMax()
        self.menu()
        self.calculate()
        self.printResponse2()   
     
      
    """  
        self.priceUno[0][0] = 1.0        # Dolar a dolar
        self.priceUno[0][1] = 1.03       # Dolar a euro
        self.priceUno[0][2] = 1.03       # Dolar a Yen Japones
        self.priceUno[0][3] = 0.87       # Dolar a Libra eterlina
        self.priceUno[0][4] = 5146.00    # Dolar a peso
        self.priceUno[1][0] = 1.3        # Euro a Dolar
        self.priceUno[1][1] = 1.00       # Euro a Euro
        self.priceUno[1][2] = 144.9      # Euro a Jen Japones
        self.priceUno[1][3] = 0.85       # Euro a Libra esterlina
        self.priceUno[1][4] = 5146.00    # Euro a Peso
        self.priceUno[2][0] = 0.0071     # Yen Japones a dolar
        self.priceUno[2][1] = 0.0069     # Yen Japones a euro
        self.priceUno[2][2] = 1          # Yen Japones a Yen Japones
        self.priceUno[2][3] = 0.006      # Yen a Libra esterlina
        self.priceUno[2][4] = 35.51      # Yen a Peso
        self.priceUno[3][0] = 1.19       # Libra esterlina a Dolar 
        self.priceUno[3][1] = 1.15       # Libra esterlina a Euro
        self.priceUno[3][2] = 166.79     # Libra esterlina a Yen Japones
        self.priceUno[3][3] = 1          # Libra esterlina a Libra esterlina
        self.priceUno[3][4] = 5923.00    # Libra esterlina a Peso
        self.priceUno[4][0] = 0.0002     # Peso a Dolar
        self.priceUno[4][1] = 0.00019    # Peso a Euro 
        self.priceUno[4][2] = 0.028      # Peso a Yen Japones
        self.priceUno[4][3] = 0.00017    # Peso a Libra esterlina
        self.priceUno[4][4] = 1          # Peso a Peso
    """

      #  self.coins = {'Dolar':0,'Euro':1, 'Yen':2,'Libra':3,'Peso':4}


    # set
    def refreshDivisas(self):
        for pais1 in range(self.D1):
            for pais2 in range(self.D2):
                response   = self.consumeApi(self.abr[pais1]) # llamado a api rest "actualizacion en tiempo real"
                self.date  = response['date']
                self.priceUno[pais1][pais2] =  float(response["rates"][self.abr[pais2]]) 

    # captur
    def menu(self):
        for pais in range(self.D1):
            print( pais,'. ', self.coins2[pais] )
        self.c1       = int(input(f"Digite codigo de su divisa local: " ))
        self.c2       = int(input(f"Digite codigo de divisa que compro: "))
        self.valorIni = float(input(f"Digite el valor que compro en {self.coins2[self.c1]}: "))
        self.priceIni = float(input(f"Digite el valor del {self.coins2[self.c2]}  en  {self.coins2[self.c1]} cuando compro: "))
        self.priceFin = self.priceUno[self.c2][self.c1] # precio de moneda extrangera

    # Logic
    def priceMax(self):
        self.l = np.array(self.priceUno)
        self.max = np.where(self.l==np.max( self.l ))
        self.min = np.where(self.l==np.min( self.l )) 

    # Logic
    def calculate(self):
        self.quantityDivisa  = self.valorIni / self.priceIni   # encuentra cuantas unidades compro de la moneda extranjera
        self.newValueCoinLoc = self.quantityDivisa * self.priceFin # ya que tiene el valor en moneda extranjera vendera estas unidades en moneda local
        self.ganancia        =  (self.newValueCoinLoc -  self.valorIni)


    # print
    def printResponse2(self):
        self.separator()
        if(self.ganancia < 0):
            print( "\nSi realiza la venta de divisa en este momento perdera ", self.ganancia, "y el comprador ganara ", abs(self.ganancia), "(", self.coins2[self.c1] ,")"  )
        elif(self.ganancia > 0 ):
            print( "Si realiza la venta de divisa en este momento ganara ", self.ganancia, "y el comprador perdera ", self.ganancia, "(", self.coins2[self.c1] ,")" ) 
        else:
            print( "Si realiza la venta de divisa en este momento no tendra ganacia ni perdida" )
        print(  "El costo de su moneda local ", self.coins2[self.c1] , " a ", self.coins2[self.c2]  , "es de: ",self.priceUno[self.c1][self.c2],"su invercion esta evaluada en:" 
              , self.quantityDivisa, " (", self.coins2[self.c2],")" )
        print(f"""la divisa más alta actualmente es { self.coins2[int(self.max[0])]} con un valor {np.max(self.l)} ( { self.coins2[int(self.max[1])]} )""")
        self.separator()


    # print
    def printPriceToDay(self):
        self.separator()
        print("Valor de divisas para : ", self.date)
        for pais1 in range(self.D1):
            for pais2 in range(self.D2):
                print(self.abr[pais2],": ", self.priceUno[pais1][pais2]  )
        self.separator()

    # print 
    def separator(self):
        print("\n =============================== \n")


    # response  
    def consumeApi(self, abr):
        url = f"https://api.exchangerate-api.com/v4/latest/{abr}"
        response = urlopen(url)
        return json.loads(response.read())

cambio = Divisa()
        




