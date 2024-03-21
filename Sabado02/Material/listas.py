# Crear un diccionario
d = {'key1':'item1','key2':'item2'}
print(d)
#aparece esto {'key1': 'item1', 'key2': 'item2'}
type(d)
# aparece dict
d['key1'] #acceder al elemento que tiene la clave `key1`
#aparece 'item1'

print("Un ejemplo de uso de los diccionarios")
pepito = {'edad':20,'nombre':'Pepito','Apellido':'Perez','estatura':1.77}
print(pepito)
#aparece {'edad': 20, 'nombre': 'Pepito', 'Apellido': 'Perez', 'estatura':1.77}
print(pepito['nombre'])
print(pepito['Apellido']) #Observar que esta clave empieza con Mayuscula,
# Python es case sensitive
print(pepito['edad'])
print(pepito['estatura'])
print (f"El nombre del paciente es {pepito['nombre']} {pepito['Apellido']},tiene {pepito['edad']} años y una estatura de {pepito['estatura']} ")
print (pepito.keys())
#aparece dict_keys(['edad', 'nombre', 'Apellido', 'estatura'])
# Que ocurre si quiero obtener todos los valores del diccionario?
# pepito[:]
#Booleans (Logicos)
# las palabras True y False son palabras restringidas
# valor Verdadero
#True
#True
# valor Falso
#False
#False
v1 = True
v2 = False
print(f"Valor de v1 = {v1} y v2 = {v2}")
#Valor de v1 = True y v2 = False
type(v1) # tipo de dato
#aparece bool