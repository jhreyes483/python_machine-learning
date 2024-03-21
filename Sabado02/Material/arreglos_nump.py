import numpy as np
#Creando un arreglo de ejemplo
arr = np.arange(0,11) # Generar un arreglo de enteros del 0 hasta el 10
print (arr)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
print(arr.dtype) # tipos de datos dentro del arreglo
#dtype('int64')
#Indexación y Selección con corchetes
#La forma más sencilla de elegir uno o algunos elementos de una matriz es similar a las listas de Python:
# Obtener un valor conociendo su indice (index)
print(arr[8])
#Obtener los valores en un rango [valor_inicial, valor_final -1]
print(arr[1:5])
#array([1, 2, 3, 4])
#Obtener los valores en un rango [valor_inicial, valor_final -1]
print(arr[0:5])
#array([0, 1, 2, 3, 4])
#Broadcasting (Difusion)
#Los arreglos de Numpy difieren de una lista normal de Python en su capacidad de Broadcasting, qeu es asignar un valor a un rango de posiciones:
# definiendo un valor para todo un rango de posiciones (Broadcasting)
arr[0:5]=100 # Asignar el numero 100 a las pocisiones desde el 0 hasta el 
print(arr)
#array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])
#crear nuevamente el arreglo con el que estabamos trabajando
arr = np.arange(0,11)
print(arr)
#array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
#NOTA importante en la seleccion de rangos (sclicing)
# los arreglos son mutables
slice_of_arr = arr[0:6]
print(slice_of_arr)
#array([0, 1, 2, 3, 4, 5])
#Cambiar todos los valores a 99
slice_of_arr[:]=99
print(slice_of_arr)
#array([99, 99, 99, 99, 99, 99])
#Observe que los cambios tambien ocurren en el arreglo original
print(arr)
#array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])
#Los datos no se copian, ¡es un puntero a el arreglo original! ¡Esto evita problemas de memoria!
# Para obtener una copia, se debe hacer explicito
arr = np.arange(0,11)
arr_copy = arr.copy()
arr_copy[:] = 99
print(arr_copy)
#array([99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99])
# Observe que el arreglo original no se modifico
print(arr)
#array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
#Indexacion de arreglos 2D (matrices)
#El formato general es arr_2d[fila][col] o arr_2d[fila,col]. Se recomienda usar la notacion con la coma por claridad.
# Creacion de una matriz de 3x3
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)
"""
array([[ 5, 10, 15],
       [20, 25, 30],
       [35, 40, 45]])
"""
#Indexando por filas
print(arr_2d[1]) # Obtener la fila 1 (recordar que el indice de python empieza en 0)
#array([20, 25, 30])
# El formato es **arr_2d[fila][col]** o **arr_2d[fila,col]**
# Obteniendo un elemento en especifico
print(arr_2d[1][0]) # elemento de la fila 1 columna 0
#20
# Obteniendo un elemento en especifico
print(arr_2d[1,0]) # elemento de la fila 1 columna 0
#20
# seleccion de rangos en arreglos 2D (slicing)
#dimensiones (2,2) desde la esquina superior derecha
print(arr_2d[:2,1:] )# filas [0,1] y columnas 1 hasta el final
"""
array([[10, 15],
       [25, 30]])
"""
# fila de indice 2
print(arr_2d[2])
#array([35, 40, 45])
# todos los elementos de las columnas que estan en la fila de posicion 2
print(arr_2d[2,:])
#array([35, 40, 45])
#Indexacion especial
#La indexación especial permite seleccionar filas o columnas enteras desordenadas
#Creando una matriz de zeros
arr2d = np.zeros((10,10))
print(arr2d)
"""
array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
"""
#Tamaño del arreglo
arr_length = arr2d.shape[1]
print(arr_length)
#10
# Creando una matriz con elementos que contienen el valor correspondiente a la posicion de la fila
for i in range(arr_length):
    arr2d[i] = i
print(arr2d)
"""
array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [2., 2., 2., 2., 2., 2., 2., 2., 2., 2.],
       [3., 3., 3., 3., 3., 3., 3., 3., 3., 3.],
       [4., 4., 4., 4., 4., 4., 4., 4., 4., 4.],
       [5., 5., 5., 5., 5., 5., 5., 5., 5., 5.],
       [6., 6., 6., 6., 6., 6., 6., 6., 6., 6.],
       [7., 7., 7., 7., 7., 7., 7., 7., 7., 7.],
       [8., 8., 8., 8., 8., 8., 8., 8., 8., 8.],
       [9., 9., 9., 9., 9., 9., 9., 9., 9., 9.]])
"""
#La indexacion especial permite:
# sacar las filas 2, 4 , 6, 8
print(arr2d[[2,4,6,8]]) # observe el uso de los dobles corchetes
"""
#array([[2., 2., 2., 2., 2., 2., 2., 2., 2., 2.],
       [4., 4., 4., 4., 4., 4., 4., 4., 4., 4.],
       [6., 6., 6., 6., 6., 6., 6., 6., 6., 6.],
       [8., 8., 8., 8., 8., 8., 8., 8., 8., 8.]])
"""
#Permite cualquier orden
print(arr2d[[6,4,2,7]])
"""
array([[6., 6., 6., 6., 6., 6., 6., 6., 6., 6.],
       [4., 4., 4., 4., 4., 4., 4., 4., 4., 4.],
       [2., 2., 2., 2., 2., 2., 2., 2., 2., 2.],
       [7., 7., 7., 7., 7., 7., 7., 7., 7., 7.]])
"""