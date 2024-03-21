def captura():
   num=int(input("Digite un numero"))
   return num

def factorial(num):
   res=1
   if(num==0):
        res=1
   else:
      for i in range(1,num+1):
        res=res*i
   return res

def mostrar1(n1, n2,sw):
    if (sw==1):
       print("El mayor de : ",n1, " y ", n2," es: ",n1)
    else:
        if(sw==2):
            print(n1, " y ", n2," son iguales")
        else:
            print("El mayor de : ",n1, " y ", n2," es: ",n2)


def mostrar(num,res):
   print("El factorial de: ",num, " es: ",res)

def captura1():
   mdo=int(input("Digite cuantas tablas desea"))
   return mdo

def captura2():
   mdor=int(input("Hasta dónde desea multipliar cada tabla"))
   return mdor

def captura3():
   mdo=int(input("Digite un número\t"))
   return mdo

def captura4():
   mdor=int(input("Digite otro número\t"))
   return mdor

def tablas(mdo, mdor):
   for i in range(1,mdo+1):
       print("Tabla del",i)
       for j in range(1,mdor+1):
          print(i," * ",j," = ",i*j)

def maymin(n1,n2):
    if(n1>n2):
      sw =1
    elif(n1==n2):
      sw=2
    else:
        sw=3
    return sw

def salir():
    print("CHAO")

def error():
    print("Opción errada")

def menu():
   opc=1
   while(opc!=4):
    print("Opweraciones")
    print("============")
    print("1. Factorial")
    print("2. Tablas")
    print("3. Mayor o menor")
    print("4. Salir")
    opc=int(input("Digite su opción"))
    match(opc):
        case 1: 
                num=captura()
                res=factorial(num)
                mostrar(num,res)
        case 2: 
                mdo=captura1()
                mdor=captura2()
                tablas(mdo,mdor)
        case 3: 
                n1=captura3()
                n2=captura4()
                sw=maymin(n1,n2)
                mostrar1(n1,n2,sw)
        case 4: 
                salir()
        case other:
                error()

#bloque principal
menu()