# Importar la funcion de NumPy para crear arreglos de numeros enteros
import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101) # Inicializar el generador aleatorio
# Forma rapida de crear una lista de python desde strings
print('A B C D E'.split())
# Crear un dataframe con numeros aleatorios de 4 Columnas y 5 Filas
# Crear listas rapidamente usando la funcion split 'A B C D E'.split()
# Esto evita tener que escribir repetidamente las comas
df = pd.DataFrame(randn(5,4),
                  index='A B C D E'.split(),
                  columns='W X Y Z'.split())
print(df)
print("Número de filas y columans",df.shape)
# Informacion general de los datos de cada cloumna
# Indica el numero de filas del dataset
# Muestra el numero de datos No Nulos por columna (valores validos)
# Tipo de dato de cada columna
# Tamaño total del dataset
print(df.info())
# Tipos de datos que existen en las columnas del dataframe
print(df.dtypes)
"""
el metodo .describe() de los dataframes presenta un resumen de la estadistica descriptiva general de las columnas numericas del dataframe, presenta la informacion de:
•	Promedio (mean)
•	Desviacion estandard (std)
•	Valor minimo
•	Valor maximo
•	Cuartiles (25%, 50% y 75%)
"""
print(df.describe())
# Ver Primeros elementos del dataframe
print(df.head())
#Ver Ultimos elementos del dataframe
print(df.tail())
# Regresara todos los datos de la columna W
print(df['W'])
# Seleccionar dos o mas columnas
# Pasar una lista con los nombres de las columnas
print(df[['W','Z']])
# Seleccionar dos o mas columnas
# Pasar una lista con los nombres de las columnas
# Puedo indicar el orden de las columnas
print(df[['X','W','Z']])
#Las columnas de un DataFrame Columns son solo Series
print(type(df['W'])) # Tipos de datos
# Nueva columna igual a la suma de otras dos
# operacion vectorizada
df['new'] = df['W'] + df['Y']
print(df)
#Eliminando Columnas
df.drop('new',axis=1) # axis = 0 elimina filas(index) axis = 1 elimina columnas
print(df)
# No se aplica a el dataframe a menos que se especifique.
# Como se ve la operacion pasada no quedo grabada
# Para que quede grabado se puede hacer de dos formas
# df = df.drop('new',axis=1) # Forma 1
df.drop('new', axis=1, inplace=True) # Forma 2
print(df)
#También se puede sacar filas de esta manera:
df.drop('E',axis=0)
print(df)
# Otra manera de borrar las columnas es
del df['X'] # Esta funcion es INPLACE
print(df)
#Obtener los nombres de las columnas y los indices (index):
print(df.columns) # nombres de las columnas
print(df.index) # nombres de los indices
"""
Seleccionando Filas y Columnas
las dos formas de seleccion principal son:
•	DataFrame.loc[etiqueta_fila, etiqueta_columna] <- por etiquetas
•	DataFrame.iloc[indice_fila, indice_columna] <- por indices
"""
# la funcion loc busca por medio de los nombres de los indices y columnas
print(df.loc['A']) # se selecciona todos los valores de la fila 'A'
#O basado en la posicion (index) en vez de usar la etiqueta
print(df.iloc[2]) # Se seleccionan los valores de la fila con indice 2
#Seleccionar un subconjunto de filas y columnas
# Mediante etiquetas
# se selecciona el elemento que esta en la fila=B Col=Y
print(df.loc['B','Y']) # con etiquetas
# Mediante etiquetas
# se selecciona un subconjunto de datos que estan entre
# filas = A, B   Cols= W, Y
print(df.loc[['A','B'],['W','Y']])
print(df.loc[['B','A'],['Y','W']])
#condiciones
print(df>0)
# Esta operacion solo mostrara los valores del dataframe que cumplen la condicion
# los que no cumplen devuelve el valor NaN
print(df[df>0])
# seleccionar todas las filas donde el valor
# que esta en la columna 'W' sea mayor que cero
print(df[df['W']>0])
# Seleccionar las filas donde 'W' sea mayor que cero
# y de esas filas escoger los valores de la columna 'Y'
print(df[df['W']>0]['Y'])
# Seleccionar las filas donde 'W' sea mayor que cero
# y de esas filas escoger los valores de las columna 'Y' y 'X'
print(df[df['W']>0][['Y','Z']])
"""
Para dos condiciones, se usa los booleanos de esta forma
•	| en vez de or
•	& en vez de and
•	~ en vez de not
"""
# Seleccionar las filas donde 'W' sea mayor que cero
# y tambien donde 'Y' sea mayor que 0.5
print(df[(df['W']>0) & (df['Y'] > 0.5)])
# seleccionar todas las filas donde el valor
# que esta en la columna 'W' sea mayor que cero

#df[df['W']>0]
print(df.query('W>0'))
# Seleccionar las filas donde 'W' sea mayor que cero
# y de esas filas escoger los valores de la columna 'Y'
#df[df['W']>0]['Y']
print(df.query('W>0')['Y'])
"""
Ejercicio
Seleccionar las filas donde 'W' sea mayor que cero
y tambien donde 'Y' sea mayor que 0.5
"""
# Reinicializar el indice a su valor por defecto 0,1...n index
print(df)
df = df.reset_index()
print(df)
newind = 'CA NY WY OR CO'.split() # crear una lista con strings
print(newind)
# Agregar la lista creaada en el paso anterior al dataframe
df['States'] = newind
print(df)
# Redefinir la columna states como el indice
df.set_index('States')
print(df)
"""
Pregunta: Qué es una función inplace?
"""
# por que no queda establecido el indice?
print(df)
# para establecer el indice debe ser una funcion inplace
df.set_index('States',inplace=True)
#df = df.set_index('States') # otra forma de hacerlo
print(df)




