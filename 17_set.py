#set(Conjuntos):Los conjuntos se utilizan para almacenar varios elementos en una sola variable. Es una colección desordenada (Los elementos establecidos pueden aparecer en un orden diferente cada vez que los usa y no se puede hacer referencia a ellos por índice o clave.) , inmutable (Los elementos establecidos no se pueden modificar, pero puede eliminar elementos y agregar elementos nuevos.) y no indexada .


#CREACIÓN DE UN SET(CONJUNTO)

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Nota: Los conjuntos no están ordenados, por lo que no puede estar seguro en qué orden aparecerán los elementos.

thisset = {"apple", "banana", "cherry"}
print(thisset)#Resultado:{'apple', 'cherry', 'banana'} 

#NO DUPLICADOS: Los conjuntos no pueden tener dos artículos con el mismo valor. Ingora a los valores duplicados  

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)#Salida: {'apple', 'cherry', 'banana'}

#Nota: Los valores True y 1 se consideran el mismo valor en conjuntos y se tratan como duplicados:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)# Resultado: {True, 2, 'banana', 'apple', 'cherry'}

#OBTENER LONGITUD DE UN SET
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#TIPOS DE DATOS: Los elementos establecidos pueden ser de cualquier tipo de datos:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(f'{set1}\n{set2}\n{set3}')

#Un conjunto puede contener diferentes tipos de datos:
set1 = {"abc", 34, True, 40, "male"}
print(set1)# Resultado: {True, 34, 'male', 40, 'abc'}

#¿Cuál es el tipo de datos de un conjunto?
myset = {"apple", "banana", "cherry"}
print(type(myset))

#El constructor set(): También es posible usar el constructor set() para hacer un conjunto.
thisset = ["apple", "banana", "cherry"]
print(thisset)#Lista
thisset = set(thisset) #Convertimos a set
print(thisset)

#ACCESO A LOS ELEMENTOS DE UN CONJUNTO(set)
#No puede acceder a los elementos de un conjunto haciendo referencia a un índice o una clave.Pero puede recorrer los elementos del conjunto usando un for bucle, o preguntar si un valor específico está presente en un conjunto, usando la inpalabra clave.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Compruebe si "banana" está presente en el conjunto:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#AGREGAR ELEMENTOS:
#Una vez que se crea un conjunto, no puede cambiar sus elementos, pero puede agregar nuevos elementos.

#Método add():
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Método update(): Para agregar elementos de otro conjunto al conjunto actual.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#El objeto en el método update() no tiene que ser un conjunto, puede ser cualquier objeto iterable (tuplas, listas, diccionarios, etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#REMOVER ELEMENTOS DEL CONJUNTO(set)
# Método remove()
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Nota: Si el elemento a eliminar no existe, remove()generará un error.

# Método discard()
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Nota: Si el elemento a eliminar no existe, NO discard() generará un error.

# El método pop() para eliminar un elemento, pero este método eliminará un elemento aleatorio, por lo que no puede estar seguro de qué elemento se eliminará. El valor de retorno del pop()método es el elemento eliminado.
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#Nota: los conjuntos no están ordenados , por lo que al usar el pop()método, no sabe qué elemento se elimina.

#El método clear()  vacía el conjunto:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#La palabra clave "del" eliminará el conjunto por completo:
thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset) #Error, el elemento no existe.

# UNIR CONJUNTOS:

#Hay varias formas de unir dos o más conjuntos en Python. 

#método union(): devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos, o el update()método que inserta todos los elementos de un conjunto en otro:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#El método update() inserta los elementos de set2 en set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Nota: Ambos union() y update() excluirán cualquier elemento duplicado.

#Guarde SOLO los duplicados:

#El método intersection_update() mantendrá solo los elementos que están presentes en ambos conjuntos.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#El método intersection() devolverá un nuevo conjunto, que solo contiene los elementos que están presentes en ambos conjuntos.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#Conservar todo, pero NO los duplicados:

#El método symmetric_difference_update() mantendrá solo los elementos que NO están presentes en ambos conjuntos.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#El método symmetric_difference() devolverá un nuevo conjunto, que contiene solo los elementos que NO están presentes en ambos conjuntos.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#Nota: Los valores True y 1 se consideran el mismo valor en conjuntos y se tratan como duplicados:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

#COPIAR CONJUNTO
#Método copy()
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

#El método isdisjoint() devuelve True si ninguno de los elementos está presente en ambos conjuntos; de lo contrario, devuelve False.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#El método issubset() devuelve True si todos los elementos del conjunto existen en el conjunto especificado; de lo contrario, devuelve False.

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

z = x.issubset(y)

print(z)

#El método issuperset() devuelve True si todos los elementos del conjunto especificado existen en el conjunto original; de lo contrario, devuelve False.

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

