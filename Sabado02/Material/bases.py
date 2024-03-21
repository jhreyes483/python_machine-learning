# Las Listas son Variables Mutables
H = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
P = H[:] # copiar todo el contenido de H a P
P[0] = 333
print("Observar el que ocurre con 'H' cuando se cambia el valor de 'P', si P= H[:]")
print(f"P = {P}") # uso de f-strings para imprimir los resultados
print(f"H = {H}") # uso de f-strings para imprimir los resultados
print("Dirección de memoria de H: ",id(H))#Dirección de memoria de H
print("Dirección de memoria de P: ",id(P))#Dirección de memoria de P
#Indexacion anidada
nest = [1,2,3,[4,5,['target']]] # Lista con otra lista al interior
print("Se presenta dos listas anidadas")
print(nest)
# obtener el string
print(nest[3][2][0][:2]) # De la lista que es el elemento 4, obtener el elemento 3, y obtener el valor de esa lista
print("Dato de la lista anidada en la posición 3 2 0: ", (nest[3][2][0]))
# De la lista que es el elemento 4, obtener el elemento 3, y obtener el valor de esa lista
# obtener otro elemento de la lista
print("De la lista que es el elemento 4, obtener el elemento 3, y obtener elvalor de esa lista")
print("obtener otro elemento de la lista")
print(nest[3][:2][1])
#Agregar datos en una lista
#Agregar elementos a una lista se hace con los metodos: .insert() .append()
#.insert()
#Inserta un ítem x en una posición i, los otros elementos despues de la posicion se mueven hacia la derecha.
#control+k+c comentarea control +k+u qwuita comentario d euna linea seleccionada
nest = [1,2,3,[4,5,['target']]] # Lista con otr,)a lista al interior
print(nest)
nest.insert(2,'Amo Python')
print(nest)
#.append()

print("Agrega los elementos al final de la lista nest[4][2].append(8)")
# se agrega un dato al final de la lista utilizando el metodo append()
nest[4][2].append(8)
print(nest)

print("nest[4].append('Pandas')")
nest[4].append('Pandas')
print(nest)

#Asignar valores a una posición
nest[2] = 'Casa' # reasignar el valor a una posicion de una lista
print(nest)
len(nest) #obtener el tamaño de la lista
#Borrar Elementos de una lista
nest[1:3] = [] # Borrar elementos de una lista
print("original nest")
print(nest)
print("Borrar elementos de una lista conociendo su index del(nest[2][2][0])")
del(nest[2][2][0])
print(nest) # observar que el valor esta dentro de una lista

print("Concatenar listas new_list = nest + my_list")
my_list=["hola"]
new_list = nest + my_list
#Concatenar listas
print(nest)
print(my_list)
# agregar una lista al final
nest.append(my_list)
print(nest)
# Repetir varias veces una lista
repetida = my_list*4
print(new_list)
print(repetida)