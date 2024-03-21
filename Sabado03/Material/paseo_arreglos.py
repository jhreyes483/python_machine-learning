import numpy as np # importar la libreria de NumPy
#Declarando arreglo
lista = list(range(10))
lista1 = list(range(20))
lista2=list()
print("Lista 1:")
print(lista)
print("Lista 2:")
print(lista1)
lista2=lista + lista1 # este procedimento lo que hace es concatenar las listas
print("Unión de la lista 1 y 2:")
print(lista2)
x = 3
lista2=lista1*x # este procedimento hace que se repita la lista x numero de veces
print("Repetición de lista2:")
print(lista2)


arr = np.arange(0,10) # crear un arreglo de 10 elementos
print("Arreglo crreado")
print(arr)
arr + arr # Suma elemento a elemento de los arreglos
# Suma de valores uno a uno con arreglos
aa = np.arange(5)
bb = np.arange(10) # este arreglo es mas grande que el anterios
print("Suma Arreglos")
print(aa+bb[:5]) # deben tener el mismo tamaño para realizar la suma
print("Mulyiplicación Arreglos")
print(arr * arr) # Multiplicacion elemento a elemento
print("Resta Arreglos")
print(arr - arr) # Resta elemento a elemento
print("División Arreglos")
print(arr/arr) # division elemento a elemento
print("1 dividio arreglo")
# Observar el primer elemento del arreglo
print(1/arr)
print("Arreglo elevado al cubo")
print(arr**3) # eleva al cubo cada elemento del arreglo
#Calcular la raiz cuadrada de cada elemento
print("raiz cuadrada")
print(np.sqrt(arr))
#Calcular el exponencial (e^) de cada elemento
print("Exponencial")
print(np.exp(arr))
# Obtener el valor maximo como una funcion
print("Valor maximo")
print(np.max(arr)) #lo mismo arr.max()
# Calcular el Sin de cada elemento
print("Seno")
print(np.sin(arr))
# Calcular el Logaritmo de cada elemento
print("Logaritmo")
print(np.log(arr))
# Calcular el valor absoluto
print("Valor absoluto")
print(np.abs(arr))
#Estadistica
# Desviacion estandar
print("Desviacion estandar")
print(np.std(arr))
# Promedio de los valores
print("Promedio")
print(np.mean(arr))
# Media
print("Media:")
print(np.median(arr))
# Varianza
print("Varianza")
print(np.var(arr))
#Operaciones de Matrices
#creacion de una matriz de ejemplo
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)
# transpuesta de una matriz
print("Traspuesta")
print(arr_2d.T) # tambien puede ser arr_2d.transpose()
# Multiplicacion de vectores
a = np.array([1,4,3]) # vector = arreglo de 1 dimension
b = np.array([2,-1,5]) # vector = arreglo de 1 dimension
print("Multiplicación de vectores")
print(a@b)
# Multiplicacion de matrices
# Producto Punto
print("Multiplicación de matrices")
a = np.array(([2,0,1],[3,0,0],[5,1,1]))
b = np.array(([1,0,1],[1,2,1],[1,1,0]))
print(a@b)
#Tambien puede ser de esta forma
print(np.dot(a,b))
# Producto Cruz
a = np.array([1,4,3]) # vector = arreglo de 1 dimension
b = np.array([2,-1,5]) # vector = arreglo de 1 dimensi
print("Prodcuto cruz")
print(np.cross(a,b))